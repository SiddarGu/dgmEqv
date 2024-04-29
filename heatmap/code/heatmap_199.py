
# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create a dictionary to store the data
data = {"Product Category": ["Electronics", "Apparel", "Home Goods", "Beauty", "Toys", "Food", "Books", "Health/Nutrition", "Music/n"],
        "Revenue": [300, 500, 200, 400, 250, 350, 150, 250, 100],
        "Profit Margin": [20, 25, 15, 22, 19, 18, 12, 24, 17]}

# Convert the dictionary into a pandas dataframe
df = pd.DataFrame(data)
df.set_index("Product Category", inplace=True)

# Set figure size
fig = plt.figure(figsize=(12, 8))

# Plot the heatmap
ax = plt.axes()
heatmap = ax.imshow(df, cmap="YlGnBu")

# Set x and y ticks and ticklabels in the center of rows and columns
ax.set_xticks(np.arange(len(df.columns)))
ax.set_xticklabels(df.columns, rotation=45, ha="right", rotation_mode="anchor")
ax.set_yticks(np.arange(len(df.index)))
ax.set_yticklabels(df.index, wrap=True)

# Show the value of each cell
for i in range(len(df.index)):
    for j in range(len(df.columns)):
        text = ax.text(j, i, df.iloc[i, j], ha="center", va="center", color="k")

# Add colorbar
cb = fig.colorbar(heatmap, ax=ax)
cb.ax.tick_params(labelsize=12)

# Set title
plt.title("Profitability by Product Category", fontsize=16)

# Automatically resize the image
plt.tight_layout()

# Save the chart
plt.savefig("output/final/heatmap/png/20231228-134212_71.png", bbox_inches="tight")

# Clear the current image state
plt.clf()

# Check the generated code to make sure it doesn't report errors and save path is relative path which is completedly the same as output/final/heatmap/png.