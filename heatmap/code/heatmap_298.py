


# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Create a dictionary for the data
data = {"Industry": ["Asia", "Europe", "North America", "South America"],
        "Steel Production (Million Metric Tons)": [250, 300, 200, 150],
        "Automobile Production (Million Units)": [50, 60, 40, 30],
        "Chemical Production (Billion Metric Tons)": [500, 600, 400, 300],
        "Textile Production (Billion Square Meters)": [400, 500, 300, 200],
        "Electronics Production (Billion Units)": [600, 700, 500, 400]
        }

# Convert the dictionary into a pandas dataframe
df = pd.DataFrame(data)

# Set the figure size
plt.figure(figsize=(8, 6))

# Plot the heatmap using seaborn
ax = sns.heatmap(df.iloc[:, 1:], cmap="Blues", annot=True, fmt="g", cbar=False)

# Set the title of the figure
ax.set_title("Production Volume by Region", fontsize=14)

# Set the x and y ticks and labels
ax.set_xticks(np.arange(5) + 0.5)
ax.set_xticklabels(df.columns[1:], rotation=45, ha="right", rotation_mode="anchor")
ax.set_yticks(np.arange(4) + 0.5)
ax.set_yticklabels(df["Industry"], rotation=0)

# Set the ticks and labels in the center of rows and columns
ax.tick_params(axis="both", which="both", length=0)
ax.tick_params(axis="x", which="major", pad=10)

# Automatically resize the image
plt.tight_layout()

# Save the figure in the specified path
plt.savefig("output/final/heatmap/png/20231228-163105_34.png", bbox_inches="tight")

# Clear the current image state
plt.clf()