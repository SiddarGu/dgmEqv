import matplotlib.pyplot as plt
import numpy as np

# First, restructure the data into the required format
category_stats = [['Electronics', 100, 200, 250, 325, 375], 
                  ['Apparel', 120, 225, 275, 350, 420], 
                  ['Home & Kitchen', 180, 275, 325, 385, 450], 
                  ['Books', 50, 150, 230, 315, 390], 
                  ['Beauty & Personal Care', 80, 175, 230, 285, 355]]
outliers = [[], [85,440], [500], [430], [380,400]]

# Create figure and add subplot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

# Prepare data for boxplot
data_to_plot = [stats[1:] for stats in category_stats]

# Add boxplot
bp = ax.boxplot(data_to_plot, notch=True, patch_artist=True, whis=1.5)

colors = ['#0000FF', '#00FF00', '#FFFF00', '#FF00FF', '#FF69B4']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Manually add the outliers 
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, 'ro')

# Set axes properties
ax.set_xticklabels([stats[0] for stats in category_stats], rotation=15, wrap=True)
ax.set_xlabel('Product Category')
ax.set_ylabel('Sales Volume (Units)')
ax.set_title('Product Sales Volume Across Various Categories in E-commerce (2021)')
ax.grid(True)

# Save the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/207_202312310058.png')

# Clear the current figure
plt.clf()
