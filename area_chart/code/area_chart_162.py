
# Import necessary modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create dictionary with data
data = {"Field": ["Chemistry", "Physics", "Biology", "Engineering", "Computer Science"],
        "2019": [200, 150, 180, 130, 250],
        "2020": [100, 120, 150, 100, 200],
        "2021": [150, 180, 200, 150, 250],
        "2022": [100, 200, 250, 180, 150],
        "2023": [200, 180, 150, 130, 100]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig = plt.figure(figsize=(10, 6))

# Plot the data with area chart
ax = fig.add_subplot(111)
ax.stackplot(df["Field"], df["2019"], df["2020"], df["2021"], df["2022"], df["2023"], alpha=0.5)

# Set x-axis label
ax.set_xlabel("Field")

# Set y-axis label
ax.set_ylabel("Number of Publications")

# Set title
plt.title("Number of Publications by Field from 2019 to 2023")

# Set ticks and tick labels for x-axis
ax.set_xticks(np.arange(len(df.index)))
ax.set_xticklabels(df["Field"], rotation=45, ha="right", rotation_mode="anchor")

# Set ticks and tick labels for y-axis
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 10) * 10
yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
ax.set_yticks(yticks)
ax.set_yticklabels(yticks)

# Set background grid lines
ax.grid(True, axis="y", linestyle="--")

# Set legend
ax.legend(["2019", "2020", "2021", "2022", "2023"], loc="upper center", bbox_to_anchor=(0.5, -0.15), ncol=5)

# Automatically resize image
plt.tight_layout()

# Save image
plt.savefig("output/final/area_chart/png/20231228-140159_82.png", bbox_inches="tight")

# Clear current image state
plt.clf()