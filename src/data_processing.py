import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
def load_data(path):
    return pd.read_csv(path)
class CreditRiskFeatureEngineer:
    def __init__(self):
        self.processor = None
    def extract_datetime_features(self, df):
        df = df.copy()
        df["TransactionStartTime"] = pd.to_datetime(df["TransactionStartTime"])
        return df.drop(columns=["TransactionStartTime"])
    def aggregate_customer_features(self, df):
        agg = df.groupby('CustomerId').agg(
            total_amount = ('Amount', 'sum'),
            avg_amount = ('Amount', 'mean'),
            transaction_count = ('Amount', 'count'),
            std_amount = ('Amount', 'std'),
        ).reset_index()
        return agg
    def build_processor(self):
        numerical_features = ["total_amount",
            "avg_amount",
            "transaction_count",
            "std_amount"]
        categorical_features = [
            "ProductCategory",
            "ChannelId",
            "ProviderId",
            "PricingStrategy"
        ]
        numerical_pipeline = Pipeline(
            steps=[('imputer', SimpleImputer(strategy='median')),
                   ('scaler', StandardScaler())]
        )
        categorical_pipeline = Pipeline(steps=[
            ('onehot', OneHotEncoder(handle_unknown='ignore'))
        ])
        self.processor = ColumnTransformer(
            transformers=[
                ('num', numerical_pipeline, numerical_features),
                ('cat', categorical_pipeline, categorical_features)
            ]
        )
    def fit_transform(self, df):
        df = self.extract_datetime_features(df)
        agg_df = self.aggregate_customer_features(df)
        cat_cols = [
        "CustomerId",
        "ProductCategory",
        "ChannelId",
        "ProviderId",
        "PricingStrategy"
        ]
        cat_df = df[cat_cols].drop_duplicates('CustomerId')
        final_df = agg_df.merge(cat_df, on='CustomerId', how='left')
        self.build_processor()
        x = self.processor.fit_transform(final_df)
        return x, final_df
    def transform(self, df):
        df = self.extract_datetime_features(df)
        agg_df = self.aggregate_customer_features(df)
        cat_cols = [
        "CustomerId",
        "ProductCategory",
        "ChannelId",
        "ProviderId",
        "PricingStrategy"
        ]
        cat_df = df[cat_cols].drop_duplicates('CustomerId')
        final_df = agg_df.merge(cat_df, on='CustomerId', how='left')
        x = self.processor.transform(final_df)
        return x, final_df
        