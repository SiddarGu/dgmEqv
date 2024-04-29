
# Import modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set data as dictionary
data = {"Category": ["Home", "Business", "Manufacturing", "Transportation", "Agriculture", "Education", "Healthcare", "Hospitality", "Government"],
        "Energy Consumption (kWh)": [5000, 8000, 10000, 3000, 6000, 4000, 7000, 9000, 10000],
        "Water Usage (gal)": [4000, 7000, 9000, 2000, 5000, 3000, 6000, 8000, 9000],
        "Waste Production (lbs)": [2000, 3000, 4000, 5000, 6000, 1000, 2000, 3000, 4000]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(10, 6))

# Plot area chart
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], labels=["Energy Consumption (kWh)", "Water Usage (gal)", "Waste Production (lbs)"])

# Set x-axis limits
ax.set_xlim(0, len(df.index) - 1)

# Calculate max total value and set y-axis range and ticks
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 100) * 100  # Round up to nearest multiple of 100
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set labels and legend
ax.set_xlabel("Category")
ax.set_ylabel("Total Resource Usage")
ax.legend(loc="upper left")

# Set background grid lines
ax.grid(linestyle="--")

# Set rotation and wrap for x-axis labels
ax.set_xticklabels(df.iloc[:, 0], rotation=45, ha="right", rotation_mode="anchor", wrap=True)

# Set title
ax.set_title("Resource Usage by Industry Category")

# Automatically resize image and save
plt.tight_layout()
plt.savefig("output/final/area_chart/png/20231228-131755_74.png", bbox_inches="tight")

# Clear current image state
plt.clf()