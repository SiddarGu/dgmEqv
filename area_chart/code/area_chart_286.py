
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create dictionary of data
data = {'Category': ['Energy Sector', 'Agriculture', 'Transportation', 'Manufacturing', 'Construction', 'Retail', 'Hospitality', 'Healthcare', 'Education', 'Government'],
        'Energy Consumption': [40, 25, 30, 35, 40, 20, 15, 10, 5, 5],
        'Water Usage': [35, 40, 20, 25, 15, 30, 35, 40, 45, 50],
        'Waste Production': [20, 20, 25, 20, 25, 25, 25, 30, 30, 25],
        'Pollution Emissions': [5, 15, 25, 20, 20, 25, 25, 20, 20, 20]}

# Convert data to pandas dataframe
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig = plt.figure(figsize=(12, 8))

# Set axis
ax = plt.subplot(111)

# Calculate max total value for y axis
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 10) * 10

# Set y limit
ax.set_ylim(0, max_total_value)

# Set y ticks
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set x limit
ax.set_xlim(0, len(df.index) - 1)

# Set x ticks
ax.set_xticks(np.arange(len(df.index)))

# Set x tick labels
ax.set_xticklabels(df['Category'])

# Set background grid lines
ax.grid(color='grey', linestyle='-', linewidth=0.5, alpha=0.5)

# Plot data as stacked area chart
ax.stackplot(df.index, df.iloc[:, 1:].T, labels=df.columns[1:], colors=['#FED976', '#DA9D00', '#CC4C02', '#993404'], alpha=0.8)

# Add legend
plt.legend(loc='upper left')

# Set title
plt.title('Environmental Impact by Industry')

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig('output/final/area_chart/png/20231228-155112_54.png', bbox_inches='tight')

# Clear current image state
plt.clf()