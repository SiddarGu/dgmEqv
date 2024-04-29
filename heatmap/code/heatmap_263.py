
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Process data using dict and pandas
data = {"Country": ["France", "Spain", "United States", "Italy", "China", "United Kingdom"], 
        "Hotel Occupancy (%)": [75, 70, 80, 65, 70, 75], 
        "Average Daily Rate ($)": [200, 185, 250, 180, 150, 220], 
        "Revenue per Available Room ($)": [150, 135, 200, 125, 100, 175], 
        "Tourist Arrivals (Millions)": [100, 95, 125, 85, 75, 110], 
        "Tourism Revenue (Billions)": [50, 45, 75, 40, 35, 60]}

df = pd.DataFrame(data)
df = df.set_index("Country")

# Set figure size
fig, ax = plt.subplots(figsize=(10, 6))

# Plot heatmap chart
heatmap = ax.imshow(df, cmap="YlGnBu")

# Add colorbar
cbar = plt.colorbar(heatmap, ax=ax)

# Set ticks and ticklabels for x and y axis
ax.set_xticks(np.arange(len(df.columns)))
ax.set_yticks(np.arange(len(df.index)))

ax.set_xticklabels(df.columns)
ax.set_yticklabels(df.index)

# Rotate x-axis ticklabels
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# Set ticks and ticklabels in the center of rows and columns
ax.tick_params(length=0, labelbottom=True, bottom=True, top=False, labeltop=False)

# Add title
ax.set_title("Tourism Statistics by Country")

# Show the value of each cell
for i in range(len(df.index)):
    for j in range(len(df.columns)):
        text = ax.text(j, i, df.iloc[i, j], ha="center", va="center", color="black")

# Automatically resize the image
fig.tight_layout()

# Save figure
plt.savefig("output/final/heatmap/png/20231228-162116_17.png", bbox_inches="tight")

# Clear current image state
plt.clf()