
# import the necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# convert data to dictionary
data = {"Production Area": ["Illinois", "Iowa", "Nebraska", "Kansas", "Minnesota", "North Dakota", "South Dakota", "Montana", "Wisconsin"], "Wheat (Acres)": [1000, 1500, 2000, 1800, 1200, 1000, 800, 500, 900], "Corn (Acres)": [1200, 1400, 1800, 2000, 1300, 1100, 900, 600, 1000], "Soybeans (Acres)": [1300, 1600, 2200, 2100, 1500, 1200, 1000, 700, 1100], "Rice (Acres)": [900, 1100, 1500, 1300, 1000, 800, 700, 400, 800], "Oats (Acres)": [800, 1000, 1300, 1200, 900, 700, 600, 300, 700]}

# convert dictionary to dataframe
df = pd.DataFrame(data)

# convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# set figure size
plt.figure(figsize=(10, 6))

# plot area chart
ax = plt.stackplot(df["Production Area"], df["Wheat (Acres)"], df["Corn (Acres)"], df["Soybeans (Acres)"], df["Rice (Acres)"], df["Oats (Acres)"], labels=["Wheat", "Corn", "Soybeans", "Rice", "Oats"])

# set ticks and ticklabels for x axis
plt.xticks(np.arange(len(df["Production Area"])), df["Production Area"], rotation=45, ha="right", rotation_mode="anchor")

# calculate max total value and set y limit
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 100) * 100
plt.ylim(0, max_total_value)

# set y ticks
plt.yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# set legend and adjust its position
legend = plt.legend(loc="upper left")
plt.setp(legend.get_texts(), color="black")

# set title and labels
plt.title("Crop Production by State")
plt.xlabel("Production Area")
plt.ylabel("Acres")

# add grid lines
plt.grid(color="lightgrey", linestyle="--")

# resize and save image
plt.tight_layout()
plt.savefig("output/final/area_chart/png/20231228-131755_54.png", bbox_inches="tight")

# clear current image state
plt.clf()