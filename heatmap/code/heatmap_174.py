
# Import necessary modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Define data
data = {"Country": ["United States", "China", "India", "Russia", "Brazil"],
        "CO2 Emissions (Mt)": [5.2, 10.5, 2.5, 7.8, 3.2],
        "Renewable Energy (%)": [12, 18, 8, 10, 15],
        "Deforestation (%)": [8, 10, 12, 16, 14],
        "Water Usage (gal per capita)": [120, 150, 90, 200, 100],
        "Recycling Rate (%)": [45, 30, 25, 35, 28],
        "Air Quality Index": [78, 65, 60, 70, 75]
        }

# Create a dataframe from the data
df = pd.DataFrame(data)

# Set the country column as the index
df.set_index("Country", inplace=True)

# Create a heatmap using seaborn
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(df, annot=True, cmap="Blues", linewidths=0.5, cbar=False)

# Set the x and y ticks and ticklabels to be in the center of rows and columns
ax.set_xticks(np.arange(len(df.columns)) + 0.5)
ax.set_yticks(np.arange(len(df.index)) + 0.5)
ax.set_xticklabels(df.columns, rotation=45, ha="right", rotation_mode="anchor")
ax.set_yticklabels(df.index, rotation=0, ha="right", rotation_mode="anchor")

# Add a title to the figure
plt.title("Environmental Impact by Country")

# Automatically resize the image and save it
plt.tight_layout()
plt.savefig("output/final/heatmap/png/20231228-134212_18.png", bbox_inches="tight")

# Clear the current image state
plt.clf()