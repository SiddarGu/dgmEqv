

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data as dictionary
data = {"Category": ["North America", "Europe", "Asia", "South America", "Africa", "Oceania", "Antarctica", "Middle East", "Central America", "Caribbean"], 
"Trucking (tons)": [200000, 100000, 150000, 100000, 200000, 150000, 180000, 130000, 250000, 120000],
"Air Cargo (tons)": [150000, 120000, 180000, 200000, 180000, 200000, 150000, 100000, 130000, 100000],
"Rail Cargo (tons)": [180000, 150000, 200000, 250000, 150000, 100000, 100000, 150000, 100000, 200000],
"Maritime Cargo (tons)": [130000, 100000, 150000, 180000, 130000, 250000, 200000, 180000, 200000, 180000],
"Warehouse Storage (sq. ft.)": [250000, 200000, 250000, 150000, 100000, 120000, 170000, 200000, 150000, 150000]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
plt.figure(figsize=(12, 8))

# Set x and y axis ticks and ticklabels
ax = plt.axes()
ax.set_xlim(0, len(df.index) - 1)
ax.set_ylim(0, np.ceil(df.iloc[:, 1:].sum(axis=1).max() / 1000) * 1000)
ax.set_xticks(np.arange(len(df.index)))
ax.set_xticklabels(df.iloc[:, 0])
ax.set_yticks(np.linspace(0, ax.get_ylim()[1], np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Plot area chart
ax.stackplot(df.index, df.iloc[:, 1:].values.T, labels=df.columns[1:], colors=['#8EBA42', '#F0E442', '#0072B2', '#D55E00', '#CC79A7'], alpha=0.7)

# Set background grid lines
ax.grid(linestyle='dotted')

# Set legend and legend position
ax.legend(loc='upper right')

# Set title
ax.set_title('Cargo and Storage Distribution by Region')

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig('output/final/area_chart/png/20231228-145339_78.png', bbox_inches='tight')

# Clear current image state
plt.clf()