


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Define data
data_dict = {"Year": [2018, 2019, 2020, 2021, 2022],
             "Number of Lawsuits": [500, 600, 700, 800, 900],
             "Legal Fees (in millions)": [15, 18, 20, 22, 24],
             "Court Cases Settled": [400, 450, 500, 550, 600]}

# Convert data to dataframe
data_df = pd.DataFrame(data_dict)

# Set figure size
fig, ax = plt.subplots(figsize=(10, 8))

# Plot heatmap using seaborn
import seaborn as sns
sns.heatmap(data_df.set_index("Year"), annot=True, cbar=False)

# Add title and label names
plt.title("Legal Activity and Costs")
plt.xlabel("Legal Metrics")
plt.ylabel("Year")

# Rotate x ticks
plt.xticks(rotation=45, ha="right", rotation_mode="anchor")

# Make y ticks in the center
ax.set_yticks(np.arange(len(data_df)))
ax.set_yticklabels(data_df["Year"].values)

# Automatically resize image
plt.tight_layout()

# Save image
plt.savefig("output/final/heatmap/png/20231228-163105_0.png", bbox_inches="tight")

# Clear current image state
plt.clf()