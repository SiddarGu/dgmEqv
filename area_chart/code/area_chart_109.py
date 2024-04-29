
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data
data = {'Product Type': ['Type 1', 'Type 2', 'Type 3', 'Type 4', 'Type 5'],
        'Production (Units)': [2000, 2500, 3000, 3500, 4000],
        'Quality (Defects)': [50, 75, 100, 125, 150],
        'Sales (Units)': [1500, 1750, 2000, 2250, 2500],
        'Returns (Units)': [50, 75, 50, 100, 125]}

# Convert data to dataframe
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(10, 8))

# Set x and y axis ticks and ticklabels using random probability
if np.random.choice([True, False], p=[0.7, 0.3]):
    ax.set_xticks(np.arange(0, len(df.index)))
    ax.set_xticklabels(df.iloc[:, 0])
    ax.set_xlim(0, len(df.index) - 1)
if np.random.choice([True, False], p=[0.7, 0.3]):
    ax.set_yticks(np.linspace(0, df.iloc[:, 1:].sum(axis=1).max(), np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Calculate max total value and set y-axis ticks and ticklabels
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
if max_total_value < 10:
    ax.set_ylim(0, 10)
    ax.set_yticks(np.arange(0, 11))
    ax.set_yticklabels(np.arange(0, 11))
elif max_total_value < 100:
    ax.set_ylim(0, np.ceil(max_total_value / 10) * 10)
    ax.set_yticks(np.arange(0, ax.get_ylim()[1] + 1, 10))
    ax.set_yticklabels(np.arange(0, ax.get_ylim()[1] + 1, 10))
elif max_total_value < 1000:
    ax.set_ylim(0, np.ceil(max_total_value / 100) * 100)
    ax.set_yticks(np.arange(0, ax.get_ylim()[1] + 1, 100))
    ax.set_yticklabels(np.arange(0, ax.get_ylim()[1] + 1, 100))

# Set suitable colors and transparency
colors = ['lightblue', 'lightgreen', 'lightyellow', 'pink', 'lightgrey']
alpha = 0.5

# Plot data as stacked area chart
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], df.iloc[:, 4], colors=colors,
             alpha=alpha, labels=['Production', 'Quality', 'Sales', 'Returns'])

# Set grid lines
ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)

# Set legend and adjust position
ax.legend(loc='upper left', bbox_to_anchor=(1.01, 0.9))

# Set title and labels
ax.set_title('Manufacturing and Sales Performance by Product Type')
ax.set_xlabel('Product Type')
ax.set_ylabel('Units')

# Automatically resize image by tight_layout()
fig.tight_layout()

# Save figure
fig.savefig('output/final/area_chart/png/20231228-140159_17.png', bbox_inches='tight')

# Clear current image state
plt.clf()