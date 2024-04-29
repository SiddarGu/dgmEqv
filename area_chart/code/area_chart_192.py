
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Convert data to dictionary
data = {
    'Sport': ['Football', 'Basketball', 'Baseball', 'Ice Hockey', 'Tennis', 'Golf'],
    'Total Revenue (%)': [25, 20, 15, 30, 10, 5],
    'Ticket Sales (%)': [35, 40, 30, 20, 25, 15],
    'Sponsorships (%)': [20, 10, 15, 25, 15, 10],
    'Merchandise Sales (%)': [15, 20, 25, 10, 30, 35],
    'Broadcasting Rights (%)': [5, 10, 15, 15, 20, 35]
}

# Create dataframe
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(12, 8))

# Calculate max total value and round up to nearest multiple of 10, 100 or 1000
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
if max_total_value < 10:
    max_total_value = 10
elif max_total_value < 100:
    max_total_value = np.ceil(max_total_value / 10) * 10
elif max_total_value < 1000:
    max_total_value = np.ceil(max_total_value / 100) * 100
else:
    max_total_value = np.ceil(max_total_value / 1000) * 1000

# Set y-axis tick labels
yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
ax.set_yticks(yticks)

# Set x-axis tick labels
xticks = np.arange(len(df.index))
ax.set_xticks(xticks)

# Set x-axis tick labels with rotation and alignment
ax.set_xticklabels(df.iloc[:, 0], rotation=45, ha='right', rotation_mode='anchor')

# Set y-axis limit
ax.set_ylim(0, max_total_value)

# Set background grid lines
ax.grid(linestyle='dashed', color='grey')

# Plot the data with an area chart
ax.stackplot(xticks, df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], df.iloc[:, 4], df.iloc[:, 5], labels=['Total Revenue', 'Ticket Sales', 'Sponsorships', 'Merchandise Sales', 'Broadcasting Rights'], colors=['blue', 'orange', 'green', 'red', 'purple'], alpha=0.7)

# Set legend
ax.legend(loc='upper left')

# Set title
ax.set_title('Revenue Breakdown of Major Sports Leagues')

# Automatically resize image
fig.tight_layout()

# Save figure
fig.savefig('output/final/area_chart/png/20231228-145339_23.png', bbox_inches='tight')

# Clear image state
plt.clf()