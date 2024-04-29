import matplotlib.pyplot as plt
import numpy as np

# Data
data = [
    ["Assembling",10,30,50,70,90,[]],
    ["Testing",15,35,55,75,95,[8, 150]],
    ["Packaging",20,40,60,80,100,[170]],
    ["Loading",5,25,45,65,85,[3,130]],
    ["Shipping",10,30,50,70,90,[200]]
]

# Restructure the data into two 2D list
categories = [x[0] for x in data]
box_data = [x[1:6] for x in data]
outliers = [x[6] for x in data]

# Plot the data with the type of box plot
fig, ax = plt.subplots(figsize=(10,6)) 
ax.boxplot(box_data, vert=False, patch_artist=True, medianprops={'linewidth': 2, 'color': 'purple'},  
           boxprops = {'facecolor': 'lightblue', 'color': 'blue', 'linewidth': 2}, 
           whiskerprops={'color': 'blue', 'linewidth': 2}, capprops={'color': 'blue', 'linewidth': 2}, whis=1.5)

ax.set_yticklabels(categories)

# Plot outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(outlier, [i + 1] * len(outlier), 'ro')

# Set title and labels
ax.set_xlabel('Time (Hours)')
ax.set_ylabel('Manufacturing Process')
ax.set_title('Production Time Distribution in Manufacturing Processes (2021)')

# Set grid
ax.grid(True, linestyle='--', which='major', color='gray', alpha=.6)

# Save figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/120_202312270030.png', format='png', dpi=300)

# Clear the current image state
plt.clf()
