import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ['Baked Goods', 'Fast Food', 'Dairy Products', 'Beverages', 'Fruits and Vegetables']
stats = [[80, 220, 350, 470, 650], [200, 450, 650, 850, 1100], [50, 190, 290, 390, 500], [10, 50, 90, 150, 200], [5, 30, 60, 90, 150]]
outliers = [[], [10, 1500], [10, 800], [400], [200]]

# Create figure and add subplot
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)

# Box plotting
flierprops = dict(marker='o', markersize=5, linestyle='none', markeredgecolor='r')
bp = ax.boxplot(stats, whis=1.5, labels=labels, patch_artist=True, flierprops=flierprops)

colors = ['pink', 'lightblue', 'lightgreen', 'lightyellow', 'lightgrey']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Plotting outliers
for i, outlier in enumerate(outliers):
    if outlier: # Check if there is any outlier
        ax.plot([i + 1] * len(outlier), outlier, 'x', color='black')

# Plot settings
ax.grid(True)
ax.set_title('Sodium Content Distribution in Food Categories (2020)')
ax.set_ylabel('Sodium Content (mg)')
ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)
ax.set_axisbelow(True)
plt.xticks(rotation = 45)  # rotate x-axis labels

# Save the image
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/226_202312310058.png')

# Clear the current figure
plt.clf()
