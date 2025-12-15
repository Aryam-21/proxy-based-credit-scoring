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
        df["TransactionStartTime"] = pd.to_datetime(df["TransactionStartTime"])
        snapshot_date = df['TansactionStartTime'].max() + pd.Timedelta(days=1)
        rfm = (df.groupby('CustomerId').agg(
            recency = ('TransactionStartTime', 
                       lambda x: (snapshot_date - x.max()).days),
            frequency=('TransactionId', 'count'),
            monetary=('Amount', 'sum')).reset_index())
        return rfm