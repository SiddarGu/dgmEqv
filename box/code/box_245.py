import matplotlib.pyplot as plt
import numpy as np

# Data sample
data = [
    ['Cheese', [7, 14, 21, 30, 45], []],
    ['Milk', [2, 5, 7, 10, 13], [20]],
    ['Bread', [3, 5, 7, 9, 10], [14, 15]],
    ['Apples', [21, 28, 35, 42, 49], [10, 12]],
    ['Wine', [365, 730, 1095, 1460, 1825], [2500]]
]

fig = plt.figure(figsize=(10,6)) 
ax = fig.add_subplot(111) 

# Extract box plot data and outliers
box_plot_data = [d[1] for d in data]
outliers = [d[2] for d in data]
labels = [d[0] for d in data]

# Create box plots
bp = ax.boxplot(box_plot_data, notch=False, sym='', vert=1, whis=1.5)
plt.setp(bp['boxes'], color='black')
plt.setp(bp['whiskers'], color='black')
plt.setp(bp['fliers'], color='red', marker='+')

# Plot outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, 'ro')

# Set labels and title
ax.set_xticklabels(labels, rotation=45, ha='right')
ax.set_ylabel('Shelf Life (Days)')
plt.title('Shelf Life Distribution in Food and Beverage Items (2021)')

# Miscellaneous settings
plt.grid()
plt.tight_layout()

# Save image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/131_202312270030.png', dpi=300)

# Clear current figure
plt.clf()
