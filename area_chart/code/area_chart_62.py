
# Solution

# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create dictionary to represent data
data = {'Category': ['California', 'New York', 'Florida', 'Texas', 'Illinois', 'Pennsylvania', 'Ohio'],
        'Single Family Homes (Units)': [20000, 15000, 25000, 30000, 20000, 15000, 25000],
        'Multi-Family Homes (Units)': [15000, 10000, 20000, 25000, 15000, 10000, 20000],
        'Apartments (Units)': [30000, 20000, 35000, 40000, 25000, 20000, 30000],
        'Condos (Units)': [25000, 25000, 30000, 35000, 20000, 15000, 25000],
        'Townhouses (Units)': [10000, 8000, 12000, 15000, 10000, 8000, 12000]
        }

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig = plt.figure(figsize=(10, 6))

# Set background color and grid lines
ax = plt.gca()
ax.set_facecolor('#f4f4f4')
ax.grid(color='white', linestyle='-', linewidth=1, alpha=0.5)

# Calculate max total value
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
# Round up to the nearest multiple of 10, 100 or 1000
if max_total_value < 100:
    max_total_value = 100
elif max_total_value < 1000:
    max_total_value = 1000
else:
    max_total_value = np.ceil(max_total_value / 1000) * 1000

# Set x and y axis ticks and ticklabels
ax.set_xlim(0, len(df.index) - 1)
ax.set_xticks(np.arange(len(df.index)))
ax.set_xticklabels(df.iloc[:, 0], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set colors and transparency
colors = ['#d7191c', '#fdae61', '#ffffbf', '#abdda4', '#2b83ba']
alpha = 0.8

# Plot the data with area chart
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], df.iloc[:, 4], df.iloc[:, 5],
             labels=['Single Family Homes (Units)', 'Multi-Family Homes (Units)', 'Apartments (Units)',
                     'Condos (Units)', 'Townhouses (Units)'], colors=colors, alpha=alpha)

# Set legend position and labels
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
ax.set_ylabel('Housing Units')

# Set title
ax.set_title('Housing Market Trends by State')

# Automatically resize image and save
plt.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-131755_43.png', bbox_inches='tight')

# Clear current image state
plt.clf()