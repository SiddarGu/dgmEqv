
# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Create a dictionary to store the data
data = {"Country": ["United States", "China", "India", "Russia", "Japan"], "Coal (MW)": [500, 400, 300, 200, 100], "Natural Gas (MW)": [1000, 800, 600, 400, 200], "Hydro (MW)": [1500, 1200, 900, 600, 300], "Nuclear (MW)": [2000, 1600, 1200, 800, 400], "Solar (MW)": [2500, 2000, 1500, 1000, 500], "Wind (MW)": [3000, 2400, 1800, 1200, 600]}

# Convert the dictionary into a pandas dataframe
df = pd.DataFrame(data)

# Set the index to be the "Country" column
df.set_index("Country", inplace=True)

# Create a figure and axes with the figsize parameter set to (10, 6) to prevent content from being displayed
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the heatmap chart using sns.heatmap()
sns.heatmap(df, annot=True, cmap="viridis", fmt=".0f", ax=ax)

# Set the title of the figure
ax.set_title("Energy Production by Country and Source")

# Set the ticks and ticklabels for x and y axis, and make them in the center of rows and columns
ax.set_xticks(np.arange(len(df.columns)) + 0.5)
ax.set_yticks(np.arange(len(df.index)) + 0.5)
ax.set_xticklabels(df.columns, rotation=45, ha="right", rotation_mode="anchor")
ax.set_yticklabels(df.index, rotation=0, ha="right", rotation_mode="anchor")

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the figure as a png file with the desired name and path
plt.savefig("output/final/heatmap/png/20231228-134212_11.png", bbox_inches="tight")

# Clear the current image state
plt.clf()