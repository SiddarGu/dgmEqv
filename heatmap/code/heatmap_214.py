
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# create data
data = {"Category":["Category 1", "Category 2", "Category 3", "Category 4", "Category 5", "Category 6", "Category 7", "Category 8", "Category 9", "Category 10"],
        "Education":[25,30,35,40,45,50,55,60,65,70],
        "Healthcare":[20,25,30,35,40,45,50,55,60,65],
        "Infrastructure":[15,18,20,22,25,28,30,32,35,38],
        "Taxes":[12,15,18,20,22,25,28,30,32,35],
        "Immigration":[8,10,12,14,16,18,20,22,24,26],
        "Environment":[20,20,20,20,20,20,20,20,20,20]}

# convert data to dataframe
df = pd.DataFrame(data)

# create figure and axis
fig, ax = plt.subplots(figsize=(10, 10))

# create heatmap using seaborn
import seaborn as sns
sns.heatmap(df.set_index('Category'), ax=ax, annot=True, fmt="d", cbar=False)

# set ticks and ticklabels
# ax.set_xticks(np.arange(len(df.columns[1:])) + 0.5)
# ax.set_yticks(np.arange(len(df["Category"])) + 0.5)
# ax.set_xticklabels(df.columns[1:], rotation=45, ha="right", rotation_mode="anchor")
# ax.set_yticklabels(df["Category"])

# set title and labels
plt.title("Government Policies and Priorities")
plt.xlabel("Policy Areas")
plt.ylabel("Categories")

# resize and save figure
fig.tight_layout()
plt.savefig("output/final/heatmap/png/20231228-134212_91.png", bbox_inches="tight")

# clear figure
plt.clf()