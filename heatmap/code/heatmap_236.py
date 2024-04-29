
           
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# import data
data = {"Category": ["Football", "Basketball", "Baseball", "Hockey"],
        "Revenue (Millions)": [500, 300, 200, 150],
        "Ticket Sales (Millions)": [300, 200, 150, 100],
        "Merchandise Sales (Millions)": [200, 150, 100, 50],
        "TV Rights (Millions)": [400, 250, 200, 150],
        "Sponsorship (Millions)": [250, 150, 100, 75],
        "Prize Money (Millions)": [150, 100, 50, 25]}

# convert data to dataframe
df = pd.DataFrame(data)

# set figure size
plt.figure(figsize=(10, 8))

# create heatmap using seaborn
ax = sns.heatmap(df.iloc[:, 1:], annot=True, fmt="g", cmap="Blues", cbar=False)

# set ticks and ticklabels for x and y axis
ax.set_xticks(np.arange(len(df.columns[1:])) + 0.5)
ax.set_yticks(np.arange(len(df["Category"])) + 0.5)
ax.set_xticklabels(df.columns[1:], rotation=45, ha="right", rotation_mode="anchor")
ax.set_yticklabels(df["Category"], rotation=0, ha="center")

# add colorbar
cbar = ax.figure.colorbar(ax.collections[0])
cbar.ax.set_ylabel("Revenue (Millions)", rotation=-90, va="baseline")

# set title
plt.title("Sports Revenue Breakdown")

# resize image
plt.tight_layout()

# save figure
plt.savefig("output/final/heatmap/png/20231228-155147_27.png", bbox_inches="tight")

# clear current image state
plt.clf()