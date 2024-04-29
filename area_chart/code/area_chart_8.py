
# Solution:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Data
data = {"2019": ["January", "February", "March", "April", "May"],
        "Electricity (kWh)": [25000, 24000, 26000, 28000, 30000],
        "Natural Gas (m³)": [5000, 4800, 5200, 5400, 5600],
        "Coal (tons)": [1000, 950, 1100, 1200, 1300],
        "Water (gal)": [50000, 52000, 48000, 49000, 51000]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Calculate max total value
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
# Round up max total value to nearest multiple of 10, 100 or 1000
if max_total_value < 100:
    max_total_value = np.ceil(max_total_value / 10) * 10
elif max_total_value < 1000:
    max_total_value = np.ceil(max_total_value / 100) * 100
else:
    max_total_value = np.ceil(max_total_value / 1000) * 1000

# Set figure size
fig, ax = plt.subplots(figsize=(12, 8))
# Set background grid lines
plt.grid(linestyle='dotted')

# Plot area chart
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], df.iloc[:, 4], labels=["Electricity", "Natural Gas", "Coal", "Water"])

# Set ticks and ticklabels for x axis
ax.set_xticks(np.arange(len(df.index)))
ax.set_xticklabels(df.iloc[:, 0])

# Set ticks and ticklabels for y axis
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set legend
ax.legend(loc='upper left')

# Set title
plt.title("Monthly Energy Usage by Source in 2019")

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig("output/final/area_chart/png/20231226-103019_16.png", bbox_inches='tight')

# Clear current image state
plt.clf()