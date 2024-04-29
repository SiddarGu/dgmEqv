


# Solution

# Import necessary modules
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import pandas as pd
import seaborn as sns

# Set data
data = {"Team Name": ["Team A", "Team B", "Team C", "Team D"],
        "Employees": [50, 40, 30, 20],
        "Avg. Age (Years)": [35, 40, 45, 50],
        "Avg. Salary ($)": [75000, 65000, 55000, 45000],
        "Avg. Years of Experience (Years)": [8, 10, 12, 15],
        "Avg. Performance Rating (%)": [90, 85, 80, 75]}

# Convert data into dataframe
df = pd.DataFrame(data)

# Plot the heatmap chart
fig, ax = plt.subplots(figsize=(10, 6))
cmap = cm.get_cmap('Reds')
heatmap = sns.heatmap(df.iloc[:, 1:], annot=True, fmt=".0f", cmap=cmap, cbar=False, ax=ax)

# Set x and y ticks and labels
ax.set_xticks(np.arange(0.5, len(df.iloc[:, 1:].columns)+0.5))
ax.set_yticks(np.arange(0.5, len(df.iloc[:, 1:].index)+0.5))
ax.set_xticklabels(df.iloc[:, 1:].columns, rotation=45, ha="right", rotation_mode="anchor")
ax.set_yticklabels(df.iloc[:, 0], rotation=0)

# Set title and labels
plt.title("Employee Performance by Team")
plt.xlabel("Metrics")
plt.ylabel("Team Name")

# Automatically resize the image
plt.tight_layout()

# Save the chart
plt.savefig("output/final/heatmap/png/20231228-163105_29.png", bbox_inches='tight')

# Clear the current image state
plt.clf()