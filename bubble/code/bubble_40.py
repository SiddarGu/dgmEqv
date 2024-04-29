
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import Normalize
import numpy as np

data_labels = ['Average House Price ($)', 'Average Rental Price ($)', 'Average Days on Market', 'Vacancy Rate (%)']
data = np.array([[400000, 3000, 30, 2], [350000, 2500, 45, 4], [250000, 2000, 60, 6], [450000, 3500, 90, 2], [300000, 3000, 120, 8]])
line_labels = ['Downtown', 'Suburbs', 'Countryside', 'Coastal', 'Hilly']

fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot(111)
for i in range(data.shape[0]):
    size = (data[i, 2] - data[:, 2].min()) / (data[:, 2].max() - data[:, 2].min()) * 5000 + 600
    norm_c = Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
    c = cm.ScalarMappable(norm=norm_c, cmap=cm.jet).to_rgba(data[i, 3])
    ax.scatter(data[i, 0], data[i, 1], s=size, c=c, label=None)
    ax.scatter([], [], s=20, c=c, label=line_labels[i] + ' ' + str(data[i, 2]))
ax.legend(title=data_labels[2])
cb = plt.colorbar(cm.ScalarMappable(norm=norm_c, cmap=cm.jet), ax=ax, orientation='horizontal', fraction=0.05)
cb.set_label(data_labels[3])
ax.grid(True)
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.set_title('Real Estate Prices and Market Conditions by Area')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/27_2023122261326.png')
plt.cla()