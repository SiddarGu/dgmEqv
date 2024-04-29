

import matplotlib.pyplot as plt
import numpy as np

# restructure data 
data = [[20, 50, 85, 120, 150],
        [80, 120, 180, 250, 320],
        [50, 95, 125, 175, 220],
        [100, 150, 225, 300, 400],
        [30, 60, 95, 130, 200]]

outliers = [[], [350], [30, 60], [5], [300]]

# plotting
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

ax.boxplot(data, whis=1.5)

# add labels and title
ax.set_xticklabels(["Home Appliances", "Automobile Parts", "Electronics", 
                    "Industrial Machinery", "Food Processing Equipment"], 
                   rotation=30, wrap=True)
ax.set_ylabel("Cost (USD)")
ax.set_title("Pricing Range Distribution for Manufacturing & Production Products in 2021")

# plot outliers
for i, o in enumerate(outliers):
    if o:
        ax.plot([i+1] * len(o), o, "ro")

# draw grids
ax.grid(which="major", axis="y", linestyle="--")

# adjust image size
plt.tight_layout()

# save image
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/19_202312251608.png")

# clear current image state
plt.clf()