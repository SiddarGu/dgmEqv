
import matplotlib.pyplot as plt
import numpy as np

# Restructure the data into two 2D lists
data = [[100,200,300,400,500],
        [150,250,350,450,550],
        [120,220,320,420,520],
        [90,160,220,280,370],
        [110,190,270,340,460]]
outlier = [[], [600], [640,680], [400,450], [480,550]]

# Plot the data
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
ax.boxplot(data, whis=1.5, patch_artist=True)
ax.set_xticklabels(["Recycling", "Solar Energy", "Wind Energy", "Energy Conservation", "Improved Efficiency"],
                   fontsize=12, rotation="vertical")
ax.set_ylabel("Energy Usage (Kwh)", fontsize=12)

# Plot the outliers
for i, outlier_list in enumerate(outlier):
    for outlier_value in outlier_list:
        ax.plot([i + 1] * len(outlier_list), outlier_list, 'ro')

# Adjust the settings
ax.grid(True, linestyle='--', linewidth=0.5, which='both', axis='both')
plt.title("Energy Usage Distribution for Eco-Friendly Practices in 2021", fontsize=14)
plt.tight_layout()

# Save the image
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/49_202312270030.png")

# Clear the current image state
plt.clf()