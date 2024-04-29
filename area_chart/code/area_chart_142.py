
# Import necessary modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# Define data dictionary
data_dict = {"Year": [2019, 2020, 2021, 2022, 2023],
             "Administration (Employees)": [200, 180, 220, 210, 250],
             "Sales (Employees)": [280, 300, 320, 310, 290],
             "IT (Employees)": [270, 250, 230, 240, 260],
             "HR (Employees)": [150, 160, 170, 180, 190],
             "R&D (Employees)": [180, 200, 210, 190, 230]}

# Convert first column to string type
df = pd.DataFrame(data_dict)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Create figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Plot data as stacked area chart
ax.stackplot(df["Year"], df.iloc[:, 1:].T, labels=df.columns[1:], colors=["#4286f4", "#42f46b", "#f442a6", "#f4c642", "#7842f4"], alpha=0.7)

# Set x and y axis limits
ax.set_xlim(0, len(df.index) - 1)
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value/10)*10 # Round up to nearest multiple of 10
ax.set_ylim(0, max_total_value)

# Set y axis ticks
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set background grid lines
ax.grid(linestyle='--', alpha=0.3)

# Set legend
ax.legend(loc="upper left", bbox_to_anchor=(1,1))

# Set title and labels
ax.set_title("Employee Distribution by Department from 2019 to 2023")
ax.set_xlabel("Year")
ax.set_ylabel("Number of Employees")

# Automatically resize image
fig.tight_layout()

# Save figure
fig.savefig("output/final/area_chart/png/20231228-140159_57.png", bbox_inches="tight")

# Clear image state
plt.clf()