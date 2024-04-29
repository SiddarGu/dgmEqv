import numpy as np
import matplotlib.pyplot as plt

data_labels = ['Organic Grocer', 'Burger Joint', 'Vegan Café', 'Nightclub', 'Michelin Star Restaurant']
line_labels = ['Quality', 'Price Competitiveness', 'Location', 'Menu Variety', 'Customer Service']

data = np.array([[85, 80, 75, 90, 95], [80, 85, 90, 75, 70], [75, 80, 85, 90, 95], [90, 85, 80, 75, 70], [85, 90, 95, 80, 75]])

plt.figure(figsize=(10, 10))
ax = plt.subplot(111, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
data = np.concatenate((data, data[:, 0:1]), axis=1)

colors = ['red', 'blue', 'green', 'orange', 'purple']
for i, row in enumerate(data):
    ax.plot(angles, row, 'o-', color=colors[i], label=line_labels[i])

ax.set_xticks(angles[:-1])
ax.set_xticklabels(data_labels)
ax.set_yticks([20, 40, 60, 80, 100])

ax.set_rlim(0, np.max(data) + 20)
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper right')

ax.set_title('Food and Beverage Industry Evaluation')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/133_202312302350.png')
plt.clf()