
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# define data
data = {"City": ["Paris", "London", "New York City", "Tokyo", "Dubai", "Singapore"],
        "Occupancy Rate (%)": [80, 75, 85, 70, 90, 80],
        "Average Daily Rate ($)": [200, 180, 250, 150, 300, 175],
        "Revenue per Available Room ($)": [160, 135, 212.5, 105, 270, 140],
        "Room Revenue ($)": [32000, 27000, 42500, 21000, 54000, 28000],
        "Food and Beverage Revenue ($)": [8000, 6750, 10625, 5250, 13500, 7000],
        "Other Revenue ($)": [4000, 3375, 5312.5, 2625, 6750, 3500]}

# create dataframe from data
df = pd.DataFrame(data)

# set figure size
plt.figure(figsize=(10, 8))

# create heatmap chart using sns
sns.heatmap(df.iloc[:, 1:], annot=True, cmap="BuPu", cbar=False)

# set ticks and ticklabels for x and y axis
plt.xticks(np.arange(6)+0.5, df["City"], rotation=45, ha="right", rotation_mode="anchor")
plt.yticks(np.arange(6)+0.5, df["City"], rotation=0)

# set title
plt.title("Hotel Performance in Major Cities")

# resize image and save
plt.tight_layout()
plt.savefig("output/final/heatmap/png/20231228-163105_36.png", bbox_inches="tight")

# clear current image state
plt.clf()