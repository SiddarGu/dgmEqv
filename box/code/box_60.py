import matplotlib.pyplot as plt
import numpy as np

figure, ax = plt.subplots(figsize=(10,6))

data=["New York", "Los Angeles", "San Francisco", "Chicago", "Boston"]
x = np.arange(len(data)) + 1
price_data = [[150000,220000,280000,340000,450000], 
              [130000,200000,260000,320000,390000], 
              [180000,250000,310000,370000,480000], 
              [100000,170000,230000,290000,350000], 
              [160000,210000,270000,330000,410000]]

outliers = [[], [500000,520000], [], [90,80,450000], [420000]]

bp = ax.boxplot(price_data, vert = True, patch_artist = True, notch = True, whis = 1.5)
colors = ['#0000FF', '#00FF00', '#FFFF00', '#FF00FF', '#FF4500']

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, "x")

ax.set_xticklabels(data, rotation=30)
ax.set_xlabel('City')
ax.set_ylabel('House Price (USD)')
ax.set_title('House Price Distribution in Major US Cities (2024)')
ax.grid(True)
figure.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/55_202312270030.png')
plt.clf()
