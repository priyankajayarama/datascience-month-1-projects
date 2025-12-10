import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create plots folder if it doesn't exist
if not os.path.exists("plots"):
    os.makedirs("plots")

df = pd.read_csv('/Users/priyankaj/Downloads/all_projects-2/project_week4/dataset.csv')

# Scatter plot
plt.scatter(df['x'], df['y'])
plt.savefig('plots/scatter.png')
plt.close()

# Histogram
df['x'].plot.hist()
plt.savefig('plots/histogram.png')
plt.close()

# Heatmap
sns.heatmap(df.corr())
plt.savefig('plots/heatmap.png')
plt.close()

# Line plot
df.plot(x='x', y='value')
plt.savefig('plots/lineplot.png')
plt.close()
