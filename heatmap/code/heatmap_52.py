


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Data processing
data_dict = {"Price Range (in 1000s)": ["$0-100", "$100-200", "$200-300", "$300-400", "$400-500"],
             "Studio (%)": [10, 20, 25, 30, 35],
             "1 Bedroom (%)": [20, 25, 30, 35, 30],
             "2 Bedroom (%)": [30, 30, 30, 25, 20],
             "3 Bedroom (%)": [25, 20, 10, 5, 10],
             "4 Bedroom (%)": [15, 15, 5, 5, 5]}
df = pd.DataFrame(data_dict)

# Plotting the heatmap chart
fig, ax = plt.subplots(figsize=(10, 7))
plt.imshow(df.iloc[:, 1:], cmap='YlGnBu')

# Setting ticks and ticklabels
ax.set_xticks(np.arange(len(df.columns[1:])))
ax.set_xticklabels(df.columns[1:])
ax.set_yticks(np.arange(len(df["Price Range (in 1000s)"])))
ax.set_yticklabels(df["Price Range (in 1000s)"])

# Rotating and wrapping long tick labels
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor", wrap=True)
plt.setp(ax.get_yticklabels(), rotation=0, ha="right", rotation_mode="anchor", wrap=True)

# Adding a colorbar
cbar = plt.colorbar()
cbar.ax.set_ylabel("Percentage")

# Adding values to each cell
for i in range(len(df["Price Range (in 1000s)"])):
    for j in range(len(df.columns[1:])):
        plt.text(j, i, str(df.iloc[i, j+1]) + "%", ha="center", va="center", color="white")

# Setting title and labels
plt.title("Housing Market by Price Range")
plt.xlabel("Number of Bedrooms")
plt.ylabel("Price Range (in 1000s)")

# Automatically resizing the image
plt.tight_layout()

# Saving the figure
plt.savefig("output/final/heatmap/png/20231228-124154_4.png", bbox_inches="tight")

# Clearing the image state
plt.clf()