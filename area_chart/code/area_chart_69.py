
# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create dictionary with data
data = {"2018": ["January", "February", "March", "April", "May", "June", "July", "August",
                 "September", "October", "November", "December"],
        "Single Family Homes ($)": [500000, 480000, 520000, 530000, 550000, 570000, 590000, 600000, 580000, 560000, 540000, 520000],
        "Condos ($)": [300000, 310000, 320000, 330000, 350000, 360000, 370000, 380000, 390000, 400000, 410000, 420000],
        "Townhomes ($)": [250000, 240000, 230000, 240000, 260000, 270000, 280000, 290000, 300000, 310000, 320000, 330000],
        "Apartments ($)": [200000, 210000, 220000, 190000, 180000, 170000, 160000, 150000, 140000, 130000, 120000, 110000]}

# Process data using pandas
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Create figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Plot area chart with stacked data
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], df.iloc[:, 4],
             labels=["Single Family Homes", "Condos", "Townhomes", "Apartments"],
             colors=["#FFA07A", "#87CEFA", "#90EE90", "#FFDAB9"],
             alpha=0.8)

# Set x and y axis ticks and labels
if np.random.random() < 0.7:
    ax.set_xticks(np.arange(len(df.iloc[:, 0])))
    ax.set_xticklabels(df.iloc[:, 0], rotation=45, ha="right", rotation_mode="anchor")
    ax.set_xlim(0, len(df.index) - 1)
    ax.set_yticks(np.linspace(0, np.ceil(df.iloc[:, 1:].sum(axis=1).max()), np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set background grid lines
ax.grid(alpha=0.2)

# Set title and legend
ax.set_title("Housing Market Trends in 2018")
ax.legend(loc="upper left")

# Automatically resize image
fig.tight_layout()

# Save figure
fig.savefig("output/final/area_chart/png/20231228-131755_50.png", bbox_inches="tight")

# Clear current image state
plt.clf()