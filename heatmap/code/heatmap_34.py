
# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create a dictionary with the given data
data_dict = {"Country": ["United States", "China", "India", "Brazil", "Russia"],
             "Carbon Emissions (tonnes)": [5.2*10**6, 10.5*10**6, 2.8*10**6, 1.9*10**6, 1.7*10**6],
             "Renewable Energy (%)": [20, 15, 10, 30, 25],
             "Waste Produced (tonnes)": [4.8*10**6, 5.6*10**6, 3.2*10**6, 1.5*10**6, 1.2*10**6],
             "Water Usage (cubic meters)": [40, 50, 30, 20, 35],
             "Deforestation (%)": [0.5, 1, 0.7, 1.5, 0.8]}

# Create a dataframe from the dictionary
df = pd.DataFrame(data_dict)

# Set the index of the dataframe to "Country" column
df.set_index("Country", inplace=True)

# Create a figure and axes
fig, ax = plt.subplots(figsize=(10,8))

# Plot the data as a heatmap
heatmap = ax.imshow(df, cmap="YlGnBu")

# Add the colorbar
cbar = fig.colorbar(heatmap)

# Set the ticks and ticklabels for x and y axis
ax.set_xticks(np.arange(len(df.columns)))
ax.set_xticklabels(df.columns)
ax.set_yticks(np.arange(len(df.index)))
ax.set_yticklabels(df.index)

# Rotate and align the x-axis ticklabels
ax.set_xticklabels(df.columns, rotation=45, ha="right", rotation_mode="anchor")

# Set the ticks to be in the center of each cell
ax.set_xticks(np.arange(len(df.columns)+1)-0.5, minor=True)
ax.set_yticks(np.arange(len(df.index)+1)-0.5, minor=True)
ax.grid(which="minor", color="w", linestyle="-", linewidth=3)
ax.tick_params(which="minor", bottom=False, left=False)

# Add the title
ax.set_title("Environmental Impact by Country")

# Show the values in each cell
for i in range(len(df.index)):
    for j in range(len(df.columns)):
        if len(df.index[i]) > 6 or len(df.columns[j]) > 6:
            wrap = True
        else:
            wrap = False
        if len(df.index[i]) > 12 or len(df.columns[j]) > 12:
            rotation = 45
        else:
            rotation = 0
        text = ax.text(j, i, df.iloc[i, j], ha="center", va="center", wrap=wrap, rotation=rotation, rotation_mode="anchor", color="w")

# Automatically resize the image and save it
fig.tight_layout()
plt.savefig("output/final/heatmap/png/20231228-124154_18.png", bbox_inches="tight")

# Clear the current image state
plt.clf()