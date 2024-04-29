
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
import numpy as np

data_labels = ["Revenue (Million $)", "Customer Base (Millions)", "Average Spend per Customer (Dollars)", "Customer Satisfaction (Score)"]
line_labels = ["Electronics", "Apparel", "Home Furnishings", "Groceries", "Toys", "Books"]
data = np.array([[1200, 75, 200, 9], 
                 [800, 50, 100, 7], 
                 [500, 30, 120, 7], 
                 [400, 60, 50, 8], 
                 [300, 40, 90, 9], 
                 [200, 20, 40, 10]])

fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot(1, 1, 1)

# Normalize colors and bubble size
norm = plt.Normalize(data[:, 3].min(), data[:, 3].max())
cmap = get_cmap('jet')
bubble_size = np.linspace(600, 5000, data[:, 2].size)

for i, line_label in enumerate(line_labels):
    ax.scatter(data[i, 0], data[i, 1], c=cmap(norm(data[i, 3])), s=bubble_size[i], label=None)
    ax.scatter([], [], c=cmap(norm(data[i, 3])), s=20, label=f"{line_label} {data[i, 2]}")

# Add legend with title
ax.legend(title=data_labels[2])

# Add colorbar
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
plt.colorbar(sm, ax=ax, label=data_labels[3])

# Adjust parameters
ax.grid(True)
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
plt.title("Profitability of Different Retail Shopping Categories in E-commerce")

fig.tight_layout()
fig.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/30_2023122270050.png")
plt.cla()