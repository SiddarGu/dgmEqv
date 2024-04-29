
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data
data = {"Category": ["North America", "South America", "Europe", "Asia", "Africa", "Oceania", "Middle East"], 
        "Farms (acres)": [2000, 2500, 3000, 3500, 4000, 4500, 5000], 
        "Crops (tonnes)": [3500, 4000, 5000, 6000, 7000, 8000, 9000], 
        "Livestock (heads)": [5000, 4500, 6000, 7000, 8000, 9000, 10000], 
        "Fishery (tonnes)": [1000, 1200, 1500, 1800, 2000, 2200, 2500], 
        "Poultry (heads)": [3000, 3500, 4000, 4500, 5000, 5500, 6000]}

# Convert data to a dataframe
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Create figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Plot data as stacked area chart
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1:].T, labels=df.iloc[:, 1:].columns)

# Set x and y axis limits
ax.set_xlim(0, len(df.index) - 1)
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 100) * 100
ax.set_ylim(0, max_total_value * 1.1)

# Set y ticks and ticklabels
yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
ax.set_yticks(yticks)
ax.set_yticklabels(yticks)

# Set x and y axis labels
ax.set_xlabel("Category")
ax.set_ylabel("Production")

# Set title
ax.set_title("Agricultural Production by Region")

# Create legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[::-1], labels[::-1], loc='upper left')

# Set background grid lines
ax.grid(True)

# Automatically resize image and save
plt.tight_layout()
plt.savefig("output/final/area_chart/png/20231228-155112_20.png", bbox_inches="tight")

# Clear figure state
plt.clf()