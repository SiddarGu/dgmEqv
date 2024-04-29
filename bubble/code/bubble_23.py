

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize

# Transform data
data_labels = ['Ease of Access (Score)', 'Economic Impact (Billion $)', 'Political Impact (Score)', 'Environmental Impact (Score)']
line_labels = ['Healthcare', 'Education', 'Taxation', 'Immigration', 'Security', 'Trade']
data = np.array([[10, 800, 90, 400],
                 [8, 1000, 80, 600],
                 [7, 1300, 75, 500],
                 [8, 850, 85, 400],
                 [9, 500, 95, 300],
                 [6, 1200, 85, 200]])

# Create figure
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(1, 1, 1)

# Create bubble chart
cmap = plt.get_cmap('Set2')
norm = Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
for i in range(len(data)):
    ax.scatter(data[i, 0], data[i, 1], s=(data[i, 2] - data[:, 2].min()) / (data[:, 2].max() - data[:, 2].min()) * 5000 + 600, c=cmap(norm(data[i, 3])), label=None)
    ax.scatter([], [], c=cmap(norm(data[i, 3])), s=20, label=line_labels[i] + ' ' + str(data[i, 2]))

# Plot legend
ax.legend(title=data_labels[2])

# Create color bar
sm = ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
cbar = fig.colorbar(sm, ax=ax, fraction=0.046, pad=0.04)
cbar.set_label(data_labels[3])

# Set title and axes label
plt.title('Assessing the Effects of Government Policies on Economy, Politics and Environment')
plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])

# Adjust figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/11_2023122261440.png')
plt.clf()