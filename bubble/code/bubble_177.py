import matplotlib.pyplot as plt
import numpy as np
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize

data_labels = ['Annual Sales (Billions $)', 'Market Share (%)', 'Consumer Rating (Out of 10)', 'Number of Products']
data_lines = [['Coca-Cola', 40, 43, 8, 100],
              ['Pepsi', 32, 37, 7.5, 90],
              ['Nestle', 29, 30, 7, 200],
              ['Starbucks', 26, 28, 8.5, 50],
              ['McDonald\'s', 21, 22, 7, 30],
              ['Burger King', 19, 20, 6.5, 25],
              ['Subway', 17, 18, 7, 35],
              ['KFC', 15, 16, 7, 20]]

data = np.array([line[1:] for line in data_lines])
line_labels = [f"{line[0]} {line[2]}" for line in data_lines]

fig, ax = plt.subplots(figsize=(12, 8))

colors = Normalize(data[:, 3].min(), data[:, 3].max())
sizes = np.interp(data[:, 2], (data[:, 2].min(), data[:, 2].max()), (600, 5000))

scatter = ax.scatter(data[:, 0], data[:, 1], c=data[:, 3], s=sizes, alpha=0.6, 
                     edgecolors='w', linewidth=1, cmap='viridis', label=None)

for i in range(len(line_labels)):
    ax.scatter([], [], c='k', alpha=0.3, s=20, label=line_labels[i])

ax.legend(title=data_labels[2])

cbar = plt.colorbar(ScalarMappable(norm=colors))
cbar.set_label(data_labels[3])

ax.grid(True)
plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])
plt.title('Market Performance of Major Brands in Food and Beverage Industry 2023')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/158_202312310045.png', dpi=300)
plt.clf()
