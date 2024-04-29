import matplotlib.pyplot as plt
import numpy as np

# Data for the plot
cropTypes = ['Wheat', 'Corn', 'Rice', 'Soya', 'Potato']
summaryStats = [[1.2, 2.5, 3.0, 3.6, 4.3], [0.8, 2.0, 3.5, 4.2, 5.0], 
                [1.5, 3.0, 4.0, 5.0, 6.0], [0.7, 2.0, 3.0, 4.0, 5.5], 
                [0.9, 2.3, 3.5, 4.2, 4.8]]
outliers = [[], [0.4, 6.0], [0.7, 7.5], [6.8], [5.6]]

# Create the figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
ax.boxplot(summaryStats, whis=1.5)

# Add outliers
for i, outlier in enumerate(outliers):
    if outlier:
        x = [i + 1] * len(outlier)
        ax.plot(x, outlier, 'go')

# Title and labels
plt.title("Yield Distribution by Crop Type in 2025")
plt.ylabel('Yield (Tons)')
ax.set_xticklabels(cropTypes, rotation=30)

# Grid settings
ax.xaxis.grid(True)
ax.yaxis.grid(True)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/192_202312310058.png')
plt.close(fig)
