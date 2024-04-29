
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Web Development', 'Cloud Computing', 'Cyber Security', 
               'Mobile Technology', 'Networking', 'Artificial Intelligence', 
               'Robotics', 'Virtual Reality']
line_labels = ['Category', 'Number']
data = np.array([[80, 120, 90, 100, 140, 60, 40, 20]])

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='polar')

colors = ['r', 'g', 'b', 'y', 'c', 'm', 'k', 'purple']
sector_angle = (2 * np.pi) / len(data_labels)

for i in range(len(data_labels)):
    ax.bar(sector_angle * i, data[0][i], width=sector_angle, label=data_labels[i], color=colors[i])

ax.set_xticks(np.linspace(0, 2*np.pi, len(data_labels), endpoint=False))
ax.set_xticklabels(data_labels, fontsize=10)

ax.legend(bbox_to_anchor=(1.2, 0.5))
ax.set_title('Number of Companies Working in Different Technology Fields in 2021')

fig.tight_layout()
fig.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-070122_37.png')

plt.clf()