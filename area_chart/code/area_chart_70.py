
# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data as a dictionary
data = {"Month": ["January", "February", "March", "April", "May", "June"],
       "Corporate Law (Cases)": [20, 25, 30, 35, 25, 15],
       "Criminal Law (Cases)": [30, 35, 25, 20, 30, 20],
       "Family Law (Cases)": [10, 15, 20, 25, 20, 15],
       "Environmental Law (Cases)": [15, 10, 20, 15, 10, 20],
       "Immigration Law (Cases)": [5, 10, 5, 10, 20, 25]}

# Process the data using pandas
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size and create subplot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the data as an area chart
ax.stackplot(df["Month"], df["Corporate Law (Cases)"], df["Criminal Law (Cases)"], df["Family Law (Cases)"], df["Environmental Law (Cases)"], df["Immigration Law (Cases)"], labels=["Corporate Law", "Criminal Law", "Family Law", "Environmental Law", "Immigration Law"], colors=["#00BFFF", "#FF1493", "#00FA9A", "#FFD700", "#8B4513"], alpha=0.6)

# Add background grid lines
ax.grid(color="gray", linestyle="--", linewidth=0.5, alpha=0.3)

# Set x-axis tick labels
ax.set_xticklabels(df["Month"], rotation=45, ha="right", rotation_mode="anchor")

# Set y-axis tick labels
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 10) * 10
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set axis limits
ax.set_xlim(0, len(df.index) - 1)
ax.set_ylim(0, max_total_value)

# Add legend and set its position
ax.legend(loc="upper left", bbox_to_anchor=(1, 1))

# Add title and labels
ax.set_title("Legal Cases by Month", fontsize=12)
ax.set_xlabel("Month", fontsize=10)
ax.set_ylabel("Number of Cases", fontsize=10)

# Automatically resize image and save
plt.tight_layout()
plt.savefig("output/final/area_chart/png/20231228-131755_51.png", bbox_inches="tight")

# Clear current image state
plt.clf()