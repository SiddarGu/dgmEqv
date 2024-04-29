import numpy as np
import matplotlib.pyplot as plt

data = np.array([[90, 85, 92, 88, 93, 90],
                 [85, 87, 86, 84, 82, 83],
                 [82, 84, 81, 85, 80, 83],
                 [90, 89, 88, 87, 92, 90],
                 [30, 28, 25, 15, 17, 20]])

data_labels = ['Chocolates', 'Soft Drinks', 'Bakery Items', 'Snacks', 'Ice-cream', 'Dairy Products']
line_labels = ['Taste Quality(Score)', 'Packaging Quality(Score)', 'Price Affordability(Score)', 'Product Availability(Score)', 'Market Share(%)']

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, polar=True)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
data = np.concatenate((data, data[:, 0:1]), axis=1)

for i in range(len(line_labels)):
    ax.plot(angles, data[i], 'o-', label=line_labels[i])

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper right', bbox_to_anchor=(1.2, 1))

ax.set_title('Food and Beverage Industry Product Analysis')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/199_202312310100.png')
plt.close(fig)