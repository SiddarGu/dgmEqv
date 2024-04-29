
# Import necessary modules
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Create dictionary of data
data = {"Year": [2019, 2020, 2021, 2022, 2023],
        "Accommodation (Bookings)": [200, 220, 240, 260, 280],
        "Transportation (Bookings)": [150, 160, 170, 180, 190],
        "Food & Beverage (Bookings)": [180, 190, 200, 210, 220],
        "Activities (Bookings)": [130, 120, 110, 100, 90],
        "Attractions (Bookings)": [250, 240, 230, 220, 210]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Create figure and axes
fig, ax = plt.subplots(figsize=(12, 8))

# Plot data as stacked area chart
ax.stackplot(df["Year"], df["Accommodation (Bookings)"], df["Transportation (Bookings)"], df["Food & Beverage (Bookings)"], df["Activities (Bookings)"], df["Attractions (Bookings)"], labels=["Accommodation", "Transportation", "Food & Beverage", "Activities", "Attractions"])

# Set x and y limits
ax.set_xlim(0, len(df.index) - 1)
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 10) * 10
ax.set_ylim(0, max_total_value)

# Set yticks
yticks = np.random.choice([3, 5, 7, 9, 11])
ax.set_yticks(np.linspace(0, max_total_value, yticks, dtype=np.int32))

# Set background grid lines
ax.grid(True, linestyle="--", alpha=0.5)

# Set colors and transparency
colors = ["#84A59D", "#F9B1E5", "#F0C987", "#E0F7D4", "#C5E99B"]
alpha = 0.7

# Set legend position
ax.legend(loc="upper left")

# Set title
ax.set_title("Bookings by Tourism and Hospitality Sector from 2019 to 2023")

# Automatically resize image
fig.tight_layout()

# Save figure
fig.savefig("output/final/area_chart/png/20231228-131755_93.png", bbox_inches="tight")

# Clear current image state
plt.clf()