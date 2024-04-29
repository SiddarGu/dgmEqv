
# Import necessary modules 
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 

# Define data 
data = {"Category": ["Category 1", "Category 2", "Category 3", "Category 4", "Category 5", "Category 6", "Category 7", "Category 8"],
        "Corn Production (Tonnes)": [200, 175, 225, 150, 125, 100, 75, 50],
        "Wheat Production (Tonnes)": [150, 125, 175, 200, 150, 125, 100, 75],
        "Soybean Production (Tonnes)": [100, 150, 125, 100, 100, 75, 50, 75],
        "Rice Production (Tonnes)": [50, 75, 100, 150, 200, 150, 125, 100],
        "Potato Production (Tonnes)": [75, 100, 50, 100, 75, 125, 150, 175],
        "Barley Production (Tonnes)": [125, 100, 75, 50, 100, 150, 175, 200]
        }

# Convert data into a pandas dataframe 
df = pd.DataFrame(data)

# Set figure size 
fig, ax = plt.subplots(figsize=(12, 8))

# Plot heatmap chart 
heatmap = ax.imshow(df.iloc[:, 1:].values, cmap='coolwarm')

# Set title 
plt.title("Crop Production by Category")

# Set x and y ticks 
ax.set_xticks(np.arange(len(df.columns[1:])))
ax.set_yticks(np.arange(len(df["Category"])))

# Set x and y tick labels 
ax.set_xticklabels(df.columns[1:], rotation=45, ha="right", rotation_mode="anchor")
ax.set_yticklabels(df["Category"])

# Set ticks and tick labels in the center of rows and columns 
ax.tick_params(axis='both', which='both', length=0)
ax.set_xticks(np.arange(len(df.columns[1:]))+0.5, minor=True)
ax.set_yticks(np.arange(len(df["Category"]))+0.5, minor=True)
ax.tick_params(axis='both', which='minor', length=0)
ax.grid(which="minor", color="w", linestyle='-', linewidth=3)

# Add colorbar 
plt.colorbar(heatmap)

# Automatically resize the image 
fig.tight_layout()

# Save the image 
plt.savefig("output/final/heatmap/png/20231228-134212_5.png", bbox_inches='tight')

# Clear the current image state 
plt.clf()