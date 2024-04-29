
# Import necessary modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a dictionary to represent the data
data = {'Category': ['Automotive', 'Electronics', 'Pharmaceuticals', 'FMCG', 'Textiles', 'Chemicals', 'Food & Beverage', 'Construction', 'Mining', 'Energy'], 'Production (Units)': [10000, 8000, 5000, 12000, 6000, 10000, 15000, 8000, 5000, 10000], 'Inventory (Units)': [5000, 4000, 3000, 6000, 2000, 4000, 7000, 2000, 1000, 3000], 'Waste (Units)': [1000, 500, 200, 2000, 500, 1000, 3000, 500, 100, 500], 'Defects (Units)': [50, 40, 20, 100, 30, 50, 200, 50, 10, 50], 'Efficiency (%)': [80, 85, 90, 75, 90, 80, 70, 85, 90, 80]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set the figure size
plt.figure(figsize=(12, 8))

# Calculate the max total value and set yticks
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
if max_total_value <= 100:
    max_total_value = np.ceil(max_total_value / 10) * 10
elif max_total_value <= 1000:
    max_total_value = np.ceil(max_total_value / 100) * 100
else:
    max_total_value = np.ceil(max_total_value / 1000) * 1000
yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)

# Plot the chart using ax.stackplot()
ax = plt.gca()
ax.stackplot(df['Category'], df.iloc[:, 1:-1].values.T, labels=df.columns[1:-1], colors=['#ff7f0e', '#1f77b4', '#2ca02c', '#9467bd', '#d62728'], alpha=0.7)

# Set background grid lines
ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5)

# Set x and y axis ticks and ticklabels
if np.random.rand() < 0.7:
    ax.set_xticks(np.arange(len(df['Category'])))
    ax.set_xticklabels(df['Category'], rotation=45, ha='right', rotation_mode='anchor')
if np.random.rand() < 0.7:
    ax.set_yticks(yticks)
    ax.set_yticklabels(yticks)

# Set legend and title
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), frameon=False)
ax.set_title('Manufacturing and Production Metrics')

# Automatically resize the image and save
plt.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-131755_9.png', bbox_inches='tight')