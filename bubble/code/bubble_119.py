import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as colors

# formatted data
data_labels = ['Average Property Price (Million $)', 'Rental Yields (%)', 'Number of Properties Sold (Thousands)', 'Affordability Index']
data = np.array([[1.5, 4, 12, 15], [1.3, 3, 20, 12], [2.1, 5, 15, 16], [2.0, 5.5, 10, 10], [3.5, 3, 8, 6], [1.8, 4.5, 15, 13], [2.5, 4, 9, 8], [2, 5, 14, 11]])
line_labels = ['New York 12', 'Los Angeles 20', 'London 15', 'Sydney 10', 'Hong Kong 8', 'Tokyo 15', 'Singapore 9', 'Paris 14']

# normalization
bubble_size = 600 + 4400 * (data[:, 2] / np.max(data[:, 2]))
cmap = plt.get_cmap("viridis")
norm = colors.Normalize(data[:, 3].min(), data[:, 3].max())

figure = plt.figure(figsize=(14, 8))
ax = figure.add_subplot()
scatter = ax.scatter(data[:, 0], data[:, 1], c=data[:, 3], cmap=cmap, norm=norm, s=bubble_size, alpha=0.6, edgecolors='w', linewidth=1.0, label=None)

for i, line_label in enumerate(line_labels):
    ax.scatter([], [], c=cmap(norm(data[:, 3][i])), s=20, label=line_label)
ax.legend(title=data_labels[2], loc='upper left', borderaxespad=0.)

plt.colorbar(mappable=scatter, ax=ax, label=data_labels[3])

ax.grid(True)
ax.set_xlabel(data_labels[0], fontsize=12)
ax.set_ylabel(data_labels[1], fontsize=12)
ax.set_title('Comparative Analysis of Global Real Estate Markets', fontsize=16)
figure.tight_layout()

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/163_202312310045.png', format='png')

plt.clf()
