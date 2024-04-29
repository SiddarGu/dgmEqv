
# Import necessary modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define data as a dictionary
data = {'Category': ['1st Quarter', '2nd Quarter', '3rd Quarter', '4th Quarter'], 'Alcoholic Beverages (Sales)': [15000, 20000, 18000, 19000], 'Soft Drinks (Sales)': [20000, 22000, 23000, 24000], 'Snacks (Sales)': [25000, 26000, 27000, 28000], 'Frozen Foods (Sales)': [18000, 19000, 20000, 21000]}

# Create dataframe from data
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(12,8))

# Calculate max total value
max_total_value = df.iloc[:, 1:].sum(axis=1).max()

# Round up max total value to nearest multiple of 100
if max_total_value < 100:
    max_total_value = np.ceil(max_total_value / 10) * 10
elif max_total_value < 1000:
    max_total_value = np.ceil(max_total_value / 100) * 100
else:
    max_total_value = np.ceil(max_total_value / 1000) * 1000

# Set y limits and ticks
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Plot data as stacked area chart
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1:].T, labels=df.iloc[:, 1:].columns, colors=['#3498db','#f1c40f','#e74c3c','#9b59b6'], alpha=0.7)

# Set x ticks and labels
ax.set_xticks(np.arange(len(df.index)))
ax.set_xticklabels(df.iloc[:, 0])

# Rotate x-tick labels by 45 degrees
plt.xticks(rotation=45, ha='right', rotation_mode='anchor')

# Set grid lines
ax.grid(linestyle='--', alpha=0.3)

# Set legend
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1))

# Set title
plt.title('Quarterly Sales of Food and Beverage Products')

# Automatically resize figure
plt.tight_layout()

# Save figure
plt.savefig('output/final/area_chart/png/20231228-131755_72.png', bbox_inches='tight')

# Clear current figure
plt.clf()