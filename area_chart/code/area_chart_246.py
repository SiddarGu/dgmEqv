

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Data
data = {"Category": ["Food & Beverage", "Retail", "Manufacturing", "E-commerce", "Healthcare", "Construction", "Automotive", "Energy", "Chemical", "Agriculture", "Pharmaceuticals", "Government", "Aerospace", "Logistics"],
        "Truck (Volume)": [500, 200, 300, 400, 200, 100, 300, 200, 100, 200, 100, 100, 100, 200],
        "Rail (Volume)": [300, 400, 100, 100, 100, 100, 200, 200, 300, 200, 100, 100, 300, 200],
        "Air (Volume)": [100, 500, 300, 200, 200, 200, 100, 200, 200, 100, 100, 200, 100, 200],
        "Ship (Volume)": [200, 200, 400, 300, 100, 200, 100, 100, 100, 200, 400, 300, 200, 200]}

# Convert data to pandas dataframe
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
plt.figure(figsize=(10, 6))

# Calculate max total value
max_total_value = df.iloc[:, 1:].sum(axis=1).max()

# Round up max total value to nearest multiple of 10, 100, or 1000
if max_total_value < 100:
    max_total_value = np.ceil(max_total_value / 10) * 10
elif max_total_value < 1000:
    max_total_value = np.ceil(max_total_value / 100) * 100
else:
    max_total_value = np.ceil(max_total_value / 1000) * 1000

# Set y-axis ticks and labels
yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
plt.yticks(yticks)

# Create area chart
ax = plt.stackplot(df.index, df.iloc[:, 1:].T, labels=df.iloc[:, 0])

# Set colors and transparency
colors = ['lightblue', 'lightgreen', 'lightpink', 'wheat']
for i, patch in enumerate(ax):
    patch.set_facecolor(colors[i])
    patch.set_alpha(0.7)

# Add background grid lines
plt.grid(axis='y', alpha=0.5)

# Set legend position
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Set x-axis tick labels
plt.xticks(df.index, df.iloc[:, 0])

# Set x-axis tick label rotation
plt.xticks(rotation=45, ha='right', rotation_mode='anchor')

# Set title
plt.title("Transportation and Logistics Volume by Industry Category")

# Automatically resize image
plt.tight_layout()

# Save image
plt.savefig("output/final/area_chart/png/20231228-145339_93.png", bbox_inches='tight')

# Clear figure
plt.clf()