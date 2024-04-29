
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Define the data as a dictionary
data = {"Year": [2017, 2018, 2019, 2020, 2021], "Legal Cases Filed": [100, 120, 130, 150, 160], "Legal Cases Won": [50, 60, 70, 80, 90], "Legal Cases Lost": [40, 40, 50, 50, 50], "Legal Cases Settled": [10, 20, 10, 20, 20]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set up the figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the data as an area chart
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], df.iloc[:, 4], labels=["Legal Cases Filed", "Legal Cases Won", "Legal Cases Lost", "Legal Cases Settled"], colors=["#6e9dff", "#00b3b3", "#ff6666", "#ffd966"])

# Set x and y limits
ax.set_xlim(0, len(df.index) - 1)
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
if max_total_value > 1000:
    max_total_value = round(max_total_value, -3)
elif max_total_value > 100:
    max_total_value = round(max_total_value, -2)
else:
    max_total_value = round(max_total_value, -1)
ax.set_ylim(0, max_total_value)

# Set y ticks and tick labels
yticks = np.linspace(0, max_total_value + 50, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
ax.set_yticks(yticks) 
ax.set_yticklabels(yticks, fontsize=12)

# Set x ticks and tick labels
xticks = df.iloc[:, 0]
ax.set_xticks(xticks)
ax.set_xticklabels(xticks, fontsize=12, rotation=45, ha="right", rotation_mode="anchor")

# Set grid lines
ax.grid(linewidth=0.5, color="#f2f2f2")

# Set legend
ax.legend(frameon=False, loc="upper right")

# Set title
ax.set_title("Legal Case Outcomes by Year", fontsize=16)

# Automatically resize the image
plt.tight_layout()

# Save the image
plt.savefig("output/final/area_chart/png/20231228-131755_21.png", bbox_inches="tight")

# Clear the current image state
plt.clf()