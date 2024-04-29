
import matplotlib.pyplot as plt
import numpy as np

data = [[200000, 400000, 500000, 600000, 800000],
        [120000, 225000, 300000, 360000, 480000, 1800000],
        [150000, 275000, 320000, 400000, 550000, 101520],
        [90000, 175000, 250000, 300000, 420000, 650000],
        [210000, 425000, 502000, 600000, 750000, 800000]]
outliers = [data[i][5:] if len(data[i]) > 5 else [] for i in range(len(data))]

# Set figure size
plt.figure(figsize=(10,6))

# Set labels
labels = ['Single Family Home', 'Apartment', 'Townhouse', 'Condominium', 'Vacation Home']

# Create box plot
plt.boxplot(np.array([data[i][:5] for i in range(5)]).T, labels=labels)

for i, outlier in enumerate(outliers):
    if len(outlier) > 0:
        plt.plot([i+1] * len(outlier), outlier, 'go', alpha=0.3, markersize=8)

# Set title
plt.title('Real Estate Price Distribution in 2020', fontsize=14)

# Set grid
plt.grid(axis='y', alpha=0.75)

# Set y axis label
plt.ylabel('Price (USD)', fontsize=12)

# Set x axis label
plt.xticks(rotation=25, wrap=True)

# Adjust display
plt.tight_layout()

# Save plot
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/26.png')

# Clear image state
plt.clf()