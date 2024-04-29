
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Convert data to dictionary
data_dict = {
    "Category": ["Anthropology", "Psychology", "Sociology", "Political Science", "History"],
    "2015": [100, 120, 150, 100, 200],
    "2016": [150, 180, 200, 150, 250],
    "2017": [100, 200, 250, 180, 150],
    "2018": [200, 180, 150, 130, 100],
    "2019": [150, 200, 100, 250, 120],
    "2020": [180, 150, 100, 200, 170],
    "2021": [130, 100, 150, 180, 200],
    "2022": [250, 130, 100, 200, 150],
    "2023": [120, 100, 200, 180, 150],
    "2024": [180, 200, 150, 100, 250],
    "2025": [150, 180, 130, 200, 100],
    "2026": [120, 150, 200, 170, 130]
}

# Process data using Pandas
df = pd.DataFrame(data_dict)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(12, 8))

# Plot area chart
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1:].T, labels=df.columns[1:])

# Set x and y axis ticks and tick labels
if np.random.rand() < 0.7:
    ax.set_xlim(0, len(df.index) - 1)
    ax.set_xticks(np.arange(0, len(df.index)))
    ax.set_xticklabels(df.iloc[:, 0], rotation=45, ha="right", rotation_mode="anchor")
else:
    ax.set_xticks([])

max_total_value = df.iloc[:, 1:].sum(axis=1).max()
if max_total_value <= 10:
    y_ticks = [0, np.ceil(max_total_value)]
elif max_total_value <= 100:
    y_ticks = np.linspace(0, np.ceil(max_total_value), np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
elif max_total_value <= 1000:
    y_ticks = np.linspace(0, np.ceil(max_total_value), np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
else:
    y_ticks = np.linspace(0, np.ceil(max_total_value), np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)

ax.set_ylim(0, np.ceil(max_total_value))
ax.set_yticks(y_ticks)
ax.set_yticklabels(y_ticks)

# Set background grid lines
ax.grid(axis="y", linestyle="--")

# Set legend
ax.legend(loc="upper left", bbox_to_anchor=(1.02, 1))

# Set title
ax.set_title("Publications in Social Sciences and Humanities by Category from 2015 to 2026")

# Automatically resize image and save
fig.tight_layout()
fig.savefig("output/final/area_chart/png/20231228-131755_45.png", bbox_inches="tight")

# Clear current image state
plt.clf()