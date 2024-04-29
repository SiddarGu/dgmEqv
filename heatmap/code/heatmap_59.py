
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# create dataframe from given data
df = pd.DataFrame({"Product": ["Soft Drinks", "Snacks", "Frozen Foods", "Alcohol"],
                   "Cost per Unit ($)": [2.50, 1.25, 4.00, 6.00],
                   "Sales Revenue ($)": [500000, 250000, 300000, 700000],
                   "Profit Margin (%)": [40, 45, 35, 50],
                   "Market Share (%)": [15, 20, 10, 25],
                   "Customer Satisfaction (%)": [85, 90, 80, 95],
                   "Employee Turnover (%)": [10, 8, 12, 5]})

# set figure size
fig, ax = plt.subplots(figsize=(10, 6))

# create heatmap using seaborn
sns.heatmap(df.iloc[:, 1:], ax=ax, cmap="YlGnBu", annot=True, fmt=".0f")

# set x and y ticks and ticklabels
ax.set_xticks(np.arange(len(df.columns[1:])))
ax.set_xticklabels(df.columns[1:], rotation=45, ha="right", rotation_mode="anchor")
ax.set_yticks(np.arange(len(df["Product"])))
ax.set_yticklabels(df["Product"], wrap=True)

# set ticks and ticklabels in the center of rows and columns
ax.tick_params(axis="both", which="major", pad=0.5, labelsize=8)
ax.set_xticks(np.arange(len(df.columns[1:])) + 0.5, minor=True)
ax.set_yticks(np.arange(len(df["Product"])) + 0.5, minor=True)
ax.tick_params(axis="both", which="minor", length=0)

# add title and set font size
plt.title("Performance Metrics in the Food and Beverage Industry", fontsize=14)

# automatically resize image and save as png
plt.tight_layout()
plt.savefig("output/final/heatmap/png/20231228-124154_48.png", bbox_inches="tight")

# clear current image state
plt.clf()