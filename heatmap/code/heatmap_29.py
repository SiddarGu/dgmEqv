


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data as a dictionary
data = {"Crop": ["Wheat", "Corn", "Rice", "Soybeans", "Barley", "Potatoes"],
        "Water Usage (Cubic Meters per Hectare)": [850, 900, 1000, 800, 850, 1500],
        "Fertilizer Usage (Metric Tons per Hectare)": [1.2, 1.5, 1.4, 1.1, 1.3, 2.0],
        "Pesticide Usage (Metric Tons per Hectare)": [0.6, 0.7, 0.8, 0.5, 0.6, 1.0],
        "Crop Yield (Tonnes per Hectare)": [3.5, 4.0, 4.5, 3.0, 3.8, 6.0],
        "Labor Costs (USD per Hectare)": [1200, 1300, 1400, 1100, 1200, 1800]}

# Convert data to a pandas dataframe
df = pd.DataFrame(data)

# Set figure size
plt.figure(figsize=(10,8))

# Set x and y labels
x = df["Crop"]
y = ["Water Usage (Cubic Meters per Hectare)", "Fertilizer Usage (Metric Tons per Hectare)",
     "Pesticide Usage (Metric Tons per Hectare)", "Crop Yield (Tonnes per Hectare)",
     "Labor Costs (USD per Hectare)"]

# Set ticks and ticklabels for x and y axis
plt.xticks(range(len(y)), y, rotation=45, ha="right", rotation_mode="anchor")
plt.yticks(range(len(x)), x)

# Plot heatmap using ax
# import ipdb; ipdb.set_trace()
ax = plt.imshow(df.iloc[:,1:], cmap="Blues")

# Set colorbar
cb = plt.colorbar()

# Set title
plt.title("Agricultural Inputs and Outputs")

# Automatically resize the image
plt.tight_layout()

# Save figure to png
plt.savefig("output/final/heatmap/png/20231228-124154_0.png", bbox_inches="tight")

# Clear current image state
plt.clf()