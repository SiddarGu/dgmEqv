
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Represent data using a dictionary
data = {"Department": ["Administration", "Sales", "IT", "HR", "R&D"],
        "2019": [70, 80, 75, 85, 65],
        "2020": [75, 85, 80, 90, 70],
        "2021": [80, 90, 85, 95, 75],
        "2022": [85, 95, 90, 100, 80],
        "2023": [90, 100, 95, 105, 85]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(12, 8))

# Set background grid lines
ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)

# Plot area chart
ax.stackplot(df["Department"], df["2019"], df["2020"], df["2021"], df["2022"], df["2023"], labels=["2019", "2020", "2021", "2022", "2023"])

# Set legend position
ax.legend(loc='upper left')

# Set title
ax.set_title("Employee Satisfaction by Department from 2019 to 2023")

# Set x and y axis ticks and ticklabels with 70% probability
if np.random.rand() < 0.7:
    ax.set_xticks(np.arange(len(df["Department"])))
    ax.set_xticklabels(df["Department"], rotation=45, ha="right")
if np.random.rand() < 0.7:
    ax.set_ylim(0, np.ceil(df.iloc[:, 1:].sum(axis=1).max()/10)*10)
    ax.set_yticks(np.linspace(0, np.ceil(df.iloc[:, 1:].sum(axis=1).max()/10)*10, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Automatically resize image
fig.tight_layout()

# Save image
fig.savefig("output/final/area_chart/png/20231228-155112_23.png", bbox_inches='tight')

# Clear image state
plt.clf()