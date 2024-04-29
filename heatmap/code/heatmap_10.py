


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Process data using dict and pandas
data = {"Energy Source": ["Coal", "Natural Gas", "Hydroelectric", "Nuclear", "Wind", "Solar"],
        "United States": [45, 25, 10, 10, 5, 5],
        "China": [68, 15, 5, 10, 1, 1],
        "Russia": [45, 20, 10, 15, 5, 5],
        "India": [30, 30, 10, 10, 10, 10],
        "Japan": [8, 25, 30, 15, 15, 7],
        "Germany": [20, 15, 5, 25, 30, 5]}
df = pd.DataFrame(data)
df = df.set_index("Energy Source")

# Plot the heatmap chart
fig, ax = plt.subplots(figsize=(10, 8)) # Set the figure size
im = ax.imshow(df, cmap="Blues", vmin=0, vmax=100) # Set the color map, min and max values

# Set the ticks and tick labels for x and y axis
ax.set_xticks(np.arange(len(df.columns)))
ax.set_yticks(np.arange(len(df.index)))
ax.set_xticklabels(df.columns)
ax.set_yticklabels(df.index)

# Rotate the x-axis labels and align them to the right
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# Loop over data dimensions and create text annotations for each cell
for i in range(len(df.index)):
    for j in range(len(df.columns)):
        text = ax.text(j, i, df.iloc[i, j], ha="center", va="center", color="w") # Set the text color as white

# Set the title of the figure
ax.set_title("Energy Mix by Country")

# Automatically resize the image
fig.tight_layout()

# Add a colorbar of chart with 40% probability
if np.random.random() < 0.4:
    cbar = ax.figure.colorbar(im, ax=ax) # Add the colorbar
    cbar.ax.set_ylabel("%", rotation=-90, va="bottom") # Set the label for colorbar

# Save the figure as a png image
plt.savefig("output/final/heatmap/png/20231225-210514_32.png", bbox_inches="tight")

# Clear the current image state
plt.clf()
plt.close()