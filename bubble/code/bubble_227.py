
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
from matplotlib.colors import Normalize

data_labels = ["Donations (Million $)", "Volunteers (Thousands)", "Reach (Million People)", "Impact (Score)"]
line_labels = ["UNICEF", "Red Cross", "World Vision", "Salvation Army", "OXFAM", "WWF"]
data = np.array([[1500, 50, 20, 9], [1000, 40, 40, 8], [500, 30, 10, 7], [250, 20, 5, 6], [100, 10, 2, 5], [50, 8, 1, 4]])

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(1, 1, 1)

for i in range(data.shape[0]):
    bubble_size = (data[i, 2] - data[:, 2].min()) / (data[:, 2].max() - data[:, 2].min()) * 5000 + 600
    bubble_color = (data[i, 3] - data[:, 3].min()) / (data[:, 3].max() - data[:, 3].min())
    ax.scatter(data[i, 0], data[i, 1], s=bubble_size, c=cm.jet(bubble_color), label=None)
    ax.scatter([], [], s=20, c=cm.jet(bubble_color), label=line_labels[i] + f" ({data[i, 2]})")

ax.legend(title=data_labels[2])

scalar_mappable = cm.ScalarMappable(cmap=cm.jet, norm=Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max()))
scalar_mappable._A = []
cbar = fig.colorbar(scalar_mappable, orientation="horizontal")
cbar.set_label(data_labels[3])

ax.set_title("Contributions of Nonprofit Organizations to Society")
ax.grid(True, alpha=0.3)
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/23_2023122270050.png')
plt.clf()