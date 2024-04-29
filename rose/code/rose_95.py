
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Automation', 'Robotics', '3D Printing', 'Power Sources', 'Metalworking', 'Electronics', 'Woodworking', 'Plastics', 'Textiles']
data = [85, 108, 128, 62, 90, 76, 48, 32, 20]
line_labels = ['Category', 'Number']

fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot(111, projection='polar')

num_categories = len(data)
sectors_angle = (2 * np.pi) / num_categories

for i in range(num_categories):
    ax.bar(i * sectors_angle, data[i], width=sectors_angle, label=data_labels[i], color=plt.cm.jet(i/num_categories))

ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=12)
ax.legend(bbox_to_anchor=(1.1, 1.05), fontsize=14)
ax.set_title('Trends in Manufacturing and Production in 2021', fontsize=18)

fig.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_83.png')
plt.clf()