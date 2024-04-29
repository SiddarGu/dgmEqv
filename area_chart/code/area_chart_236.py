
# Import libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set data
data = {
    '2019': ['Q1', 'Q2', 'Q3', 'Q4'],
    'Facebook (Users)': [1000, 1200, 1500, 1800],
    'Instagram (Users)': [750, 900, 1200, 1500],
    'Twitter (Users)': [500, 600, 800, 1000],
    'YouTube (Users)': [1500, 1800, 2000, 2200],
    'Snapchat (Users)': [800, 1000, 1200, 1500]
}

# Convert data to pandas dataframe
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(10, 6))

# Plot stacked area chart
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], df.iloc[:, 4], df.iloc[:, 5], labels=df.columns[1:])

# Set x and y axis labels
ax.set_xlabel('Quarter')
ax.set_ylabel('Number of Users (Millions)')

# Set x and y axis limits
ax.set_xlim(0, len(df.index) - 1)
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value/100) * 100
ax.set_ylim(0, max_total_value)

# Set y axis ticks
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set grid lines
ax.grid(color='lightgrey', linestyle='--', linewidth=1, alpha=0.3)

# Set legend
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1))

# Set title
ax.set_title('Social Media Usage by Platform in 2019')

# Automatically resize image
fig.tight_layout()

# Save image
plt.savefig('output/final/area_chart/png/20231228-145339_81.png', bbox_inches='tight')

# Clear current image state
plt.clf()