import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

class RFMBasedTargetBuilder:
    def __init__(self, n_clusters=3, random_state=42):
        self.n_clusters = n_clusters
        self.random_state= random_state
        self.scaler = StandardScaler()
        self.kmeans = KMeans(n_clusters=self.n_clusters, random_state=self.random_state, n_init=10)

    def compute_rfm(self, df):
        df = df.copy()
        df["TransactionStartTime"] = pd.to_datetime(df["TransactionStartTime"])
        snapshot_date = df['TransactionStartTime'].max() + pd.Timedelta(days=1)
        rfm = (df.groupby('CustomerId').agg(
            recency = ('TransactionStartTime', 
                       lambda x: (snapshot_date - x.max()).days),
            frequency=('TransactionStartTime', 'count'),
            monetary=('Amount', 'sum')).reset_index())
        return rfm
    def assign_high_risk_label(self, rfm_df):
        rfm_df = rfm_df.copy()
        rfm_scaled = self.scaler.fit_transform(rfm_df[["recency", "frequency", "monetary"]])
        rfm_df['cluster'] = self.kmeans.fit_predict(rfm_scaled)
        cluster_summary = (rfm_df.groupby('cluster')[["recency", "frequency", "monetary"]].mean())
        cluster_summary["risk_score"] = (cluster_summary["frequency"] + cluster_summary["monetary"])
        high_risk_cluster = cluster_summary["risk_score"].idxmin()
        rfm_df['is_high_risk'] = (rfm_df['cluster'] == high_risk_cluster).astype(int)
        return rfm_df[['CustomerId', 'is_high_risk']]