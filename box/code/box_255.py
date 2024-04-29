import matplotlib.pyplot as plt
import numpy as np

# Restructure the data
categories = ['Criminal Law', 'Family Law', 'Property Law', 'Immigration Law', 'Employment Law']
box_data = [[500, 1500, 2500, 3500, 4500], [400, 1200, 2000, 2800, 3600], 
            [600, 1800, 3000, 4200, 4800], [300, 900, 1500, 2100, 2700], 
            [700, 2100, 3500, 4900, 6300]]
outliers = [[6000], [5000], [5500], [3000], [7500]]

# Create the figure
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot()

# Box plot
bp = ax.boxplot(box_data, whis=1.5, vert=0, patch_artist=True, notch=True, labels=categories)

colors = ['#0000FF', '#00FF00', '#FFFF00', '#FF00FF','#FF0000']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Plot outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot(outlier, [i + 1] * len(outlier), "ro")

# Set title and labels
ax.set_title('Court Fees Dispersions across Typical Types of Law for the Year 2021')
ax.set_ylabel('Type of Law')
ax.set_xlabel('Court Fees ($)')

# Show grid
ax.grid(True)

# Save the figure and clear image state
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/144_202312270030.png')
plt.clf()
