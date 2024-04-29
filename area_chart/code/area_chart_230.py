
# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data as a dictionary
data = {'Region': ['North America', 'South America', 'Europe', 'Asia', 'Africa', 'Oceania', 'Middle East', 'Carribean', 'Central America', 'South Pacific', 'Antarctica'],
        'Hotels (Available)': [200, 180, 250, 300, 150, 170, 200, 220, 160, 180, 0],
        'Vacation Rentals (Available)': [180, 160, 200, 250, 160, 180, 210, 200, 170, 190, 0],
        'Attractions (Available)': [150, 170, 180, 150, 200, 170, 190, 150, 160, 200, 0],
        'Restaurants (Available)': [160, 180, 160, 140, 170, 150, 180, 120, 150, 210, 0],
        'Transportation (Available)': [300, 250, 210, 280, 180, 200, 300, 250, 180, 250, 0]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Create figure and axes
fig, ax = plt.subplots(figsize=(12, 6))

# Set background grid lines
ax.grid(True, linestyle=':', color='lightgrey')

# Plot the data as area chart
ax.stackplot(df['Region'], df.iloc[:, 1:].values.T, labels=df.columns[1:], colors=['#FFDAB9', '#90EE90', '#87CEFA', '#FFA07A', '#C0C0C0'], alpha=0.5)

# Set x and y axis ticks and tick labels
if np.random.choice([0, 1], p=[0.3, 0.7]):
    ax.set_xticks(np.arange(len(df.index)))
    ax.set_xticklabels(df['Region'], rotation=45, ha='right', rotation_mode='anchor')
if np.random.choice([0, 1], p=[0.3, 0.7]):
    max_total_value = df.iloc[:, 1:].sum(axis=1).max()
    if max_total_value > 1000:
        max_total_value = np.ceil(max_total_value / 1000) * 1000
    elif max_total_value > 100:
        max_total_value = np.ceil(max_total_value / 100) * 100
    else:
        max_total_value = np.ceil(max_total_value / 10) * 10
    ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set legend and its position
ax.legend(loc='lower left', bbox_to_anchor=(0, 1), ncol=5)

# Set title
ax.set_title('Tourism and Hospitality Availability by Region')

# Automatically resize the image
fig.tight_layout()

# Save figure
fig.savefig('output/final/area_chart/png/20231228-145339_74.png', bbox_inches='tight')

# Clear current image state
plt.clf()