
import matplotlib.pyplot as plt
import numpy as np

# Data
data = [[100000, 150000, 200000, 250000, 300000], [200000, 250000, 350000, 400000, 500000, 550000], [400000, 500000, 650000, 750000, 900000, 1000000, 1100000], [600000, 700000, 850000, 950000, 1100000, 1200000], [800000, 900000, 1000000, 1100000, 1200000]]
outliers = [data[i][5:] if len(data[i]) > 5 else [] for i in range(len(data))]

# Create figure
fig = plt.figure(figsize=(14, 8))

# Create axes
ax = fig.add_subplot(111)

# Plot data
ax.boxplot(np.array([data[i][:5] for i in range(5)]).T, notch=True, patch_artist=True, labels=['Low Range','Middle Range','High Range','Luxury Range','Super Luxury Range'])
for i, outlier in enumerate(outliers):
    if len(outlier) > 0:
        ax.plot([i+1] * len(outlier), outlier, 'go', alpha=0.3, markersize=8)
# Set title
ax.set_title('Home Price Distribution in Different Range in 2021')

# Set x and y axis labels
ax.set_xlabel('Price Range')
ax.set_ylabel('Price (USD)')

# Rotate x-axis labels
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# Resize image
plt.tight_layout()

# Save fig
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/22.png')

# Clear figure
plt.clf()