import pandas as pd
import numpy as np
from src.data_processing import CreditRiskFeatureEngineer
from src.rmf_target import RFMBasedTargetBuilder
# -----------------------------
# Task 3: Feature Engineering
# -----------------------------
def test_feature_engineering_outputs_expected_columns():
    """
    Test that feature engineering creates expected aggregated features
    per CustomerId.
    """
    df = pd.DataFrame({
        "CustomerId": ['CustomerId_1', 'CustomerId_10', 'CustomerId_1002', 'CustomerId_1003'],
        "TransactionStartTime": [
            "2024-01-01 10:00:00",
            "2024-01-02 12:00:00",
            "2024-01-03 09:00:00",
            "2024-01-04 03:00:00"
        ],
        "Amount": [100, 200, 50, 150],
        "ProductCategory": ["airtime", "airtime", "financial_services", "financial_services"],
        "ChannelId": ["ChannelId_2", "ChannelId_2", "ChannelId_3", "ChannelId_3"],
        "ProviderId": ["ProviderId_4", "ProviderId_4", "ProviderId_5", "ProviderId_5"],
        "PricingStrategy": [2, 4, 4, 3]
    })
    fe = CreditRiskFeatureEngineer()
    x, final_df = fe.fit_transform(df)
    expected_columns = {
        "CustomerId",
        "total_amount",
        "transaction_count",
        "avg_amount"
    }

    assert expected_columns.issubset(final_df.columns)
def test_feature_engineering_row_count():
    """
    Feature engineering should return one row per CustomerId.
    """
    df = pd.DataFrame({
        "CustomerId": ['CustomerId_1', 'CustomerId_10', 'CustomerId_1002', 'CustomerId_1003'],
        "TransactionStartTime": [
            "2024-01-01 10:00:00",
            "2024-01-02 12:00:00",
            "2024-01-03 09:00:00",
            "2024-01-04 03:00:00"
        ],
        "Amount": [100, 200, 50, 150],
        "ProductCategory": ["airtime", "airtime", "financial_services", "financial_services"],
        "ChannelId": ["ChannelId_2", "ChannelId_2", "ChannelId_3", "ChannelId_3"],
        "ProviderId": ["ProviderId_4", "ProviderId_4", "ProviderId_5", "ProviderId_5"],
        "PricingStrategy": [2, 4, 4, 3]
    })
    fe = CreditRiskFeatureEngineer()
    X, final_df = fe.fit_transform(df)

    assert final_df["CustomerId"].nunique() == final_df.shape[0]
# -----------------------------
# Task 4: Proxy Target (RFM)
# -----------------------------

def test_rfm_computation_columns_exist():
    """
    RFM computation should return recency, frequency, and monetary.
    """
    df = pd.DataFrame({
        "CustomerId": [1, 1, 2],
        "TransactionStartTime": [
            "2024-01-01",
            "2024-01-05",
            "2024-01-03"
        ],
        "Amount": [100, 200, 50]
    })

    rfm_builder = RFMBasedTargetBuilder()
    rfm = rfm_builder.compute_rfm(df)

    assert {"recency", "frequency", "monetary"}.issubset(rfm.columns)

def test_is_high_risk_is_binary():
    """
    Proxy target must be binary (0 or 1).
    """
    rfm_df = pd.DataFrame({
        "CustomerId": [1, 2, 3],
        "recency": [10, 50, 90],
        "frequency": [5, 2, 1],
        "monetary": [1000, 300, 100]
    })

    rfm_builder = RFMBasedTargetBuilder()
    result = rfm_builder.assign_high_risk_label(rfm_df)

    assert set(result["is_high_risk"].unique()).issubset({0, 1})