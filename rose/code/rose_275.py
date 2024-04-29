
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Air', 'Rail', 'Road', 'Sea', 'Pipeline']
line_labels = ['Mode of Transport']
data = np.array([[78], [90], [123], [67], [45]])

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='polar')

num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

for i in range(num_categories):
    ax.bar(i * sector_angle, data[i], width=sector_angle, label=data_labels[i], color=np.random.rand(3,))

ax.set_xticks(np.arange(0, 2*np.pi, sector_angle))
ax.set_xticklabels(data_labels)

ax.legend(data_labels, bbox_to_anchor=(1.15, 1))
ax.set_title('Usage of Transport Modes in 2021')

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-070122_7.png')
plt.clf()