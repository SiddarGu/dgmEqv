
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Music', 'Visual Arts', 'Dance', 'Literature', 'Theatre', 'Architecture', 'Film', 'Television', 'Video Games']
line_labels = ['Art Form', 'Number']
data = [[100, 90, 80, 70, 60, 50, 40, 30, 20]]

fig = plt.figure()
ax = fig.add_subplot(polar=True)
sector_angle = (2 * np.pi) / len(data_labels)

for i in range(len(data_labels)):
    ax.bar(sector_angle * i, data[0][i], width=sector_angle, label=data_labels[i])

ax.set_theta_direction(-1)
ax.set_theta_offset(np.pi/2.0)
ax.set_xticks(np.arange(0, 2 * np.pi, sector_angle))
ax.set_xticklabels(data_labels, fontsize=8, rotation=45, wrap=True, ha='center')
ax.set_title('Participation in Arts and Culture in 2021')
ax.legend(bbox_to_anchor=(1.15, 0.8))
ax.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_1.png')
plt.clf()