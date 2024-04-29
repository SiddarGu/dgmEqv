
import numpy as np
import matplotlib.pyplot as plt

data_labels = ['GDP Growth Rate (%)', 'Inflation Rate (%)', 'Unemployment Rate (%)', 'Interest Rate (%)']
line_labels = ['2019', '2020', '2021', '2022', '2023']
data = [[2.3, 1.5, 3.2, 2.4], [2.7, 2.2, 4.1, 2.8], [2.9, 2.4, 4.5, 3.1], [3.3, 2.7, 4.8, 3.4], [3.5, 2.9, 5.1, 3.7]]

X, Y = np.meshgrid(range(len(data_labels)), range(len(line_labels)))
Z = np.zeros(X.shape)

for i in range(len(line_labels)):
    for j in range(len(data_labels)):
        Z[i][j] = data[i][j]

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

ax.bar3d(X.ravel(), Y.ravel(), 0, 1, 1, Z.ravel(), alpha=0.4)
x_range = np.arange(len(data_labels))
ax.set_xticks(x_range)
ax.set_xticklabels(data_labels)
y_range = np.arange(len(line_labels))
ax.set_yticks(y_range)
ax.set_yticklabels(line_labels)
ax.set_title('Global Economic Indicators - 2019 to 2023')
ax.grid(visible=True, linestyle='-', color='lightgray')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/16.png')
plt.clf()