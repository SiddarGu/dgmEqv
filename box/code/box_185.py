

import matplotlib.pyplot as plt
import numpy as np

# Restructure the data
Home_Type = ["Utility A", "Utility B", "Utility C", "Utility D", "Utility E"]
Min_Cost = [40, 50, 60, 35, 45]
Q1_Cost = [80, 85, 90, 75, 85]
Median_Cost = [120, 120, 120, 110, 105]
Q3_Cost = [160, 155, 150, 145, 145]
Max_Cost = [200, 190, 180, 175, 185]
Outliers = [[], [230], [10, 190], [210], [240]]

# Create figure
fig = plt.figure(figsize=(10,8))

# Plot the boxplot
ax = fig.add_subplot()
bp = ax.boxplot(np.array([Min_Cost, Q1_Cost, Median_Cost, Q3_Cost, Max_Cost]), labels=Home_Type, patch_artist=True, widths=0.7, medianprops=dict(linestyle='-', linewidth=2.5, color='black'))

# Set custom colors for boxplot elements
colors = ['#f2a0a0', '#f9b2b2', '#f9d3d3', '#fcf3f3', '#fcfbfc']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Plot outliers manually
for i in range(len(Outliers)):
    for outlier in Outliers[i]:
        ax.plot(i+1, outlier, marker='o', markersize=6, color="black")

# Set title
ax.set_title("Energy Cost Distribution Among Suppliers in 2021")

# Set x and y axis label
ax.set_xlabel('Home Type')
ax.set_ylabel('Cost (USD)')

# Automatically resize the image and save
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/20_202312251044.png')

# Clear the current image state
plt.clf()