import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
class Ploter:
    def __init__(self):
        pass
    def plot_hist(self, df, column):
        plt.figure(figsize=(6, 4))
        sns.histplot(df[column], bins=50, kde=True)
        plt.title(f"Distribution of {column}")
        plt.xlabel(column)
        plt.ylabel("Frequency")
        plt.show()
    def plot_categorical(self,df, col):
        plt.figure(figsize=(8,4))
        sns.countplot(data=df, x=col, order=df[col].value_counts().index)
        plt.title(f'Distribution of {col}')
        plt.xticks(rotation=45)
        plt.ylabel('Frequency')
        plt.show()
    def corr_plot(self,df, num_cols):
        corr_matrix = df[num_cols].corr()
        mask = np.zeros_like(corr_matrix)
        up_tri = np.triu_indices_from(mask)
        mask[up_tri] = True
        plt.figure(figsize=(10, 6))
        sns.heatmap(corr_matrix, mask=mask, annot=True, fmt=".2f", cmap='coolwarm', cbar=True)
        plt.title("Correlation Matrix of Numerical Features")
        plt.show()
    def plot_box(self, df, col):
        plt.figure(figsize=(6, 4))
        sns.boxplot(x=df[col])
        plt.title(f'Boxplot of {col}')
        plt.show()


