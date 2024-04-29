

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define data
year = [2016, 2017, 2018, 2019, 2020]
production = [5000, 5200, 4500, 5100, 4800]
consumption = [4000, 4100, 4900, 3500, 3700]
export = [1000, 1100, 900, 1200, 1000]
import_val = [2000, 2100, 2300, 2500, 2200]

# Create dictionary
data = {"Year": year,
        "Production (tonnes)": production,
        "Consumption (tonnes)": consumption,
        "Export (tonnes)": export,
        "Import (tonnes)": import_val}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Plot chart using area chart
fig, ax = plt.subplots(figsize=(10, 6))
ax.stackplot(df["Year"], df["Production (tonnes)"], df["Consumption (tonnes)"], df["Export (tonnes)"], df["Import (tonnes)"],
             labels=["Production", "Consumption", "Export", "Import"],
             colors=["#a6cee3", "#1f78b4", "#b2df8a", "#33a02c"],
             alpha=0.7)

# Set ticks and ticklabels for x axis
if np.random.choice([True, False], p=[0.7, 0.3]):
    ax.set_xticks(np.arange(len(df.index)))
    ax.set_xticklabels(df["Year"])

    # Rotate x axis labels if length more than 6 characters
    if len(df["Year"][0]) > 6:
        ax.tick_params(axis="x", rotation=45, ha="right", rotation_mode="anchor")

# Set ticks and ticklabels for y axis
if np.random.choice([True, False], p=[0.7, 0.3]):
    # Calculate max total value and round up to nearest multiple of 10, 100, or 1000
    max_total_value = df.iloc[:, 1:].sum(axis=1).max()
    if max_total_value <= 10:
        max_total_value = np.ceil(max_total_value)
    elif max_total_value <= 100:
        max_total_value = np.ceil(max_total_value / 10) * 10
    elif max_total_value <= 1000:
        max_total_value = np.ceil(max_total_value / 100) * 100
    else:
        max_total_value = np.ceil(max_total_value / 1000) * 1000

    # Set y limit and ticks
    ax.set_ylim(0, max_total_value)
    ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

    # Set y label with unit
    ax.set_ylabel("Tonnes")

# Set background grid lines
ax.grid(color="gray", linestyle="--", alpha=0.3)

# Set legend position
ax.legend(loc="upper left", bbox_to_anchor=(1.02, 1))

# Set title
ax.set_title("Agricultural Trends and Trade Flows from 2016 to 2020")

# Automatically resize image and save
fig.tight_layout()
plt.savefig("output/final/area_chart/png/20231228-140159_79.png", bbox_inches="tight")

# Clear current image state
plt.clf()