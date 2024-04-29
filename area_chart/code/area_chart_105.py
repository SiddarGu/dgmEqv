

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data
data = {"Month": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
        "Country (Visitors)": [10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000],
        "City (Visitors)": [8000, 8500, 9000, 9500, 10000, 10500, 11000, 11500, 12000, 12500, 13000, 13500],
        "Beach (Visitors)": [12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000],
        "Mountain (Visitors)": [5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000, 10500],
        "Hotel (Visitors)": [15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000]
        }

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig = plt.figure(figsize=(12, 8))

# Set axis
ax = plt.axes()

# Plot data as stacked area chart
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], df.iloc[:, 4], df.iloc[:, 5], labels=["Country", "City", "Beach", "Mountain", "Hotel"], colors=["#FFA07A", "#87CEFA", "#98FB98", "#FFDAB9", "#FFC0CB"], alpha=0.8)

# Set background grid lines
ax.grid(linestyle='--', linewidth=0.5, color='#d9d9d9')

# Set x and y axis labels
ax.set_xlabel("Month")
ax.set_ylabel("Number of Visitors")

# Set x and y axis limits
ax.set_xlim(0, len(df.index) - 1)
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 100) * 100 # Round up to nearest multiple of 100
ax.set_ylim(0, max_total_value)

# Set y axis ticks and labels
yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
ax.set_yticks(yticks)
ax.set_yticklabels(yticks)

# Set x axis ticks and labels
xticks = np.arange(0, len(df.index))
ax.set_xticks(xticks)
ax.set_xticklabels(df.iloc[:, 0], rotation=45, ha='right', rotation_mode='anchor')

# Set legend
ax.legend(loc=2, fontsize=12)

# Automatically resize image and save
plt.tight_layout()
plt.savefig("output/final/area_chart/png/20231228-140159_0.png", bbox_inches='tight')

# Clear current image state
plt.clf()