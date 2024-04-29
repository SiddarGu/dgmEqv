
# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create dictionary with data
data = {"Category": ["Dance (Events)", "Music (Events)", "Theatre (Events)", "Art (Events)", "Literature (Events)"],
        2017: [15, 20, 25, 10, 5],
        2018: [20, 25, 30, 15, 10],
        2019: [25, 30, 35, 20, 15],
        2020: [30, 35, 40, 25, 20],
        2021: [35, 40, 45, 30, 25]}

# Convert dictionary to pandas dataframe
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
plt.figure(figsize=(12, 8))

# Calculate max total value
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 10) * 10

# Set y-axis ticks
yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)

# Create list of colors
colors = ["#348ABD", "#A60628", "#7A68A6", "#467821", "#CF4457"]

# Set background grid lines
plt.grid(linestyle='dotted', alpha=0.5)

# Plot area chart
ax = plt.gca()
ax.stackplot(df["Category"], df[2017], df[2018], df[2019], df[2020], df[2021], labels=[2017, 2018, 2019, 2020, 2021], colors=colors, alpha=0.8)

# Set x-axis limit
ax.set_xlim(0, len(df.index) - 1)

# Set y-axis limit and ticks
ax.set_ylim(0, max_total_value)
ax.set_yticks(yticks)

# Set x-axis tick labels
ax.set_xticklabels(df["Category"], rotation=45, ha="right", rotation_mode="anchor", wrap=True)

# Set y-axis tick labels
yticklabels = ["{:,}".format(x) for x in yticks]
ax.set_yticklabels(yticklabels)

# Set legend
ax.legend(loc="upper center", ncol=5, bbox_to_anchor=(0.5, -0.2))

# Set title
plt.title("Events in the Arts and Culture Industry")

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig("output/final/area_chart/png/20231228-145339_43.png", bbox_inches="tight")

# Clear current image state
plt.clf()