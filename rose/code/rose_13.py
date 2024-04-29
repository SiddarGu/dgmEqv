
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Rice', 'Wheat', 'Corn', 'Soybean', 'Sunflower', 'Barley', 'Peanuts']
line_labels = ['Crop Type', 'Yield']
data = np.array([[300, 400, 200, 500, 100, 150, 75]])

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='polar')
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
sector_angle = (2 * np.pi) / len(data_labels)

for i in range(len(data_labels)):
    ax.bar(sector_angle * i, data[0][i], width=sector_angle, color=colors[i], label=data_labels[i])

ax.set_title('Global Crop Yields in 2021', fontsize=16)
ax.set_xticks(np.arange(0, 2 * np.pi, sector_angle))
ax.set_xticklabels(data_labels, fontsize=12, rotation=90)
ax.legend(bbox_to_anchor=(1.1, 1.1), fontsize=14)
plt.tight_layout()
fig.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231225-125808_20.png")
plt.clf()