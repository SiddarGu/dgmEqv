
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Air','Rail','Water','Road','Pipeline','Space']
data = [400, 350, 300, 250, 200, 150]
line_labels = ['Number of Trips']

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='polar')
ax.set_title('Number of Trips Taken Using Different Modes of Transportation in 2021')
sector_angle = (2 * np.pi) / len(data_labels)

for i in range(len(data_labels)):
    ax.bar(i * sector_angle, data[i], width=sector_angle, label=data_labels[i])

ax.legend(bbox_to_anchor=(1.25, 0.5))
ax.set_xticks(np.arange(0, 2*np.pi, sector_angle))
ax.set_xticklabels(data_labels,ha='center',rotation_mode='anchor')
ax.grid(alpha=0.3)
plt.tight_layout()
fig.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_40.png')
plt.clf()