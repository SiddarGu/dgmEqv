import matplotlib.pyplot as plt
import numpy as np

# Data
data = [[50, 105, 170, 220, 300], [75, 125, 195, 250, 320], [100, 135, 210, 265, 340], 
        [40, 95, 160, 210, 290], [60, 110, 175, 225, 310]]
outliers = [[], [450], [10, 20], [320, 420], [250]]

# Setting up the plot
plt.figure(figsize=(12, 8))
ax = plt.subplot()
ax.set_ylabel("Room Price (USD)")
ax.set_title("Room Price Distribution in Hotels in 2020")

# Creating separate box plots for each hotel
positions = range(1, len(data) + 1)
for i, (d, o) in enumerate(zip(data, outliers)):
    bp = ax.boxplot(d, positions=[positions[i]], patch_artist=True, boxprops=dict(facecolor="skyblue"), 
                    medianprops=dict(color="black"), whiskerprops=dict(color="black"), 
                    capprops=dict(color="black"), flierprops=dict(color="red", markeredgecolor="black"))

    # Handling outliers
    if o:
        ax.plot([positions[i]] * len(o), o, 'ro', markersize=7, markerfacecolor='b', 
                markeredgewidth=1.5, markeredgecolor="black")

# Setting x-axis labels
ax.set_xticklabels(["Hotel A", "Hotel B", "Hotel C", "Hotel D", "Hotel E"])

# Grid and layout settings
plt.grid(axis='y', alpha=0.75)
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/10_202312251520.png")
plt.clf()