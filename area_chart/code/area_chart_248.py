


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data as dictionary
data = {
    "Category": ["History", "Psychology", "Sociology", "Economics", "Literature"],
    "2019": [150, 200, 180, 250, 120],
    "2020": [180, 220, 150, 200, 170],
    "2021": [200, 250, 130, 180, 150],
    "2022": [220, 180, 200, 150, 250],
    "2023": [200, 150, 250, 180, 130]
}

# Convert data to dataframe
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig = plt.figure(figsize=(10,6))

# Create axes
ax = fig.add_subplot(111)

# Set x ticks and tick labels
ax.set_xticks(np.arange(len(df.index)))
ax.set_xticklabels(df.iloc[:, 0])

# Set y ticks and tick labels
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 10) * 10
yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
ax.set_yticks(yticks)

# Set background grid lines
ax.grid(color='grey', linestyle='-', linewidth=0.5, alpha=0.3)

# Plot area chart
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], df.iloc[:, 4], df.iloc[:, 5], labels=df.columns[1:])

# Set legend position and labels
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=5)

# Set title
plt.title("Publication Trends in Social Sciences and Humanities from 2019 to 2023")

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig("output/final/area_chart/png/20231228-145339_98.png", bbox_inches='tight')

# Clear current image state
plt.clf()