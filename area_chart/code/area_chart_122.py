
# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Represent data as a dictionary
data = {
    "Category": ["US", "Canada", "Mexico", "Brazil", "Argentina", "China", "Japan", "India", "Australia", "New Zealand"],
    "Restaurants (Locations)": [5000, 3000, 2000, 4000, 3000, 6000, 4000, 5000, 3000, 2000],
    "Supermarkets (Locations)": [4000, 2500, 1500, 3000, 2000, 5000, 3000, 4000, 2500, 1500],
    "Cafes (Locations)": [3000, 2000, 1000, 2000, 1000, 4000, 2000, 3000, 2000, 1000],
    "Bars (Locations)": [2500, 1500, 500, 1000, 500, 3000, 1500, 2000, 1500, 500],
    "Bakeries (Locations)": [2000, 1000, 200, 500, 200, 2000, 1000, 1500, 1000, 200]
}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
plt.figure(figsize=(12, 8))

# Use ax instead of plt to plot chart
ax = plt.gca()

# Plot the data with area chart
ax.stackplot(df["Category"], df["Restaurants (Locations)"], df["Supermarkets (Locations)"], df["Cafes (Locations)"], df["Bars (Locations)"], df["Bakeries (Locations)"], labels=["Restaurants", "Supermarkets", "Cafes", "Bars", "Bakeries"], colors=["#FF7F50", "#008080", "#D2691E", "#2E8B57", "#8B008B"], alpha=0.7)

# Set background grid lines
ax.grid(linestyle="--", linewidth=0.5, color="#A9A9A9")

# Set x and y axis ticks and ticklabels
if np.random.uniform(0, 1) < 0.7:
    ax.set_xticks(np.arange(len(df.index)))
    ax.set_xticklabels(df["Category"])

    # Set rotation for x axis
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

    # Set y axis ticks and tick labels
    max_total_value = df.iloc[:, 1:].sum(axis=1).max()
    if max_total_value < 10:
        max_total_value = 10
    elif max_total_value < 100:
        max_total_value = 100
    elif max_total_value < 1000:
        max_total_value = 1000
    else:
        max_total_value = np.ceil(max_total_value / 1000) * 1000

    # Set yticks
    ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

    # Set ytick labels
    ax.set_yticklabels(ax.get_yticks())

# Set legend's position
ax.legend(loc="upper left", bbox_to_anchor=(1, 1))

# Set title
ax.set_title("Food and Beverage Industry Locations by Country")

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig("output/final/area_chart/png/20231228-140159_33.png", bbox_inches="tight")

# Clear current image state
plt.clf()