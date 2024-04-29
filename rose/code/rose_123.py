
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Social Networking', 'Blogging', 'E-commerce', 'Online Gaming', 'Streaming Platforms', 'Video Sharing', 'Online Communities', 'Online News']
data = [[1000000, 700000, 600000, 500000, 400000, 300000, 200000, 100000]]
line_labels = ['Number of Users']

fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

num_categories = len(data_labels)

sector_angle = (2 * np.pi) / num_categories

colors = ['#FF6347','#FFA07A','#FFD700','#FF7F50','#FFC0CB','#DC143C','#F4A460','#C71585']

for i in range(num_categories):
    ax.bar(i * sector_angle, data[0][i], width=sector_angle, label=data_labels[i], color=colors[i])

ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, rotation=45)

ax.legend(bbox_to_anchor=(1.2,1.05))
ax.set_title('Number of Users Engaged in Different Online Platforms in 2021')

plt.tight_layout()
fig.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_123.png")

plt.clf()