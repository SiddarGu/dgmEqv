
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# import data
data = {"Field": ["Category.1", "Category.2", "Category.3", "Category.4", "Category.5", "Category.6", "Category.7", "Category.8", "Category.9"],
        "Political Science": [23, 18, 15, 10, 7, 5, 3, 2, 1],
        "Economics": [25, 20, 18, 15, 12, 10, 8, 5, 3],
        "Psychology": [29, 25, 22, 18, 15, 12, 10, 8, 6],
        "History": [22, 19, 17, 13, 10, 8, 6, 4, 2],
        "Linguistics": [24, 22, 20, 15, 12, 10, 8, 6, 4],
        "Anthropology": [28, 23, 21, 17, 15, 12, 10, 8, 6],
        "Sociology": [0, 0, 0, 0, 0, 0, 0, 0, 0], # added a row for the empty category
        }

# convert to dataframe
df = pd.DataFrame(data)


# set the index to the "Field" column
df.set_index("Field", inplace=True)

# create a figure and axes
fig, ax = plt.subplots(figsize=(8, 6))

# plot heatmap
sns.heatmap(df, cmap="Blues", annot=True, fmt="g", ax=ax, cbar=True)

# set ticks and ticklabels
ax.set_xticks(np.arange(len(df.columns)) + 0.5)
ax.set_yticks(np.arange(len(df.index)) + 0.5)
ax.set_xticklabels(df.columns, rotation=45, ha="right", rotation_mode="anchor")
ax.set_yticklabels(df.index)

# set tick positions and labels in the center of rows and columns
ax.tick_params(axis="both", which="both", length=0, pad=2.5)
ax.xaxis.set_ticks_position("none")
ax.yaxis.set_ticks_position("none")

# add title
ax.set_title("Social Sciences and Humanities Research Funding")

# resize the image
fig.tight_layout()

# save figure
fig.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/hancheng/heatmap/png_train/heatmap_40.png", bbox_inches="tight")

# clear the current image state
plt.clf()