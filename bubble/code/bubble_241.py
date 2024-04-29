
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

data_labels = ["Cost (Billion $)", "Benefit (Score)", "Timeframe (Years)", "Carbon Footprint Reduction (Score)"]
line_labels = ["Renewable Energy", "Public Transportation", "Waste Management", "Recycling", "Organic Farming"]
data = np.array([[2.5, 80, 5, 90], [1.2, 70, 4, 85], [1.7, 75, 3, 90], [1.6, 70, 2, 95], [0.9, 65, 1, 100]])

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(1, 1, 1)

cmap = cm.get_cmap('RdBu')
norm = cm.colors.Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
scalar_map = cm.ScalarMappable(norm=norm, cmap=cmap)

for i in range(data.shape[0]):
    ax.scatter(data[i, 0], data[i, 1], label=None, s=data[i, 2] * 500 + 60, c=scalar_map.to_rgba(data[i, 3]))
    ax.scatter([], [], label=line_labels[i] + f' {data[i, 2]}', s=20, c=scalar_map.to_rgba(data[i, 3]))

ax.legend(title=data_labels[2])
fig.colorbar(scalar_map, ax=ax, label=data_labels[3])
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.set_title("Investing in Eco-Friendly Measures for Long-Term Sustainability")
ax.grid(True)
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/20_2023122270050.png")
plt.close()