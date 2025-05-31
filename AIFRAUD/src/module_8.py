"""
Visualizes transaction amount distributions.
"""
import matplotlib.pyplot as plt

def plot_histogram(df, column):
    plt.hist(df[column], bins=30)
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.title(f"Histogram of {column}")
    plt.show()

def plot_correlation_matrix(df):
    import seaborn as sns
    import matplotlib.pyplot as plt
    corr = df.corr()
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm")
    plt.title("Feature Correlation Matrix")
    plt.show()
