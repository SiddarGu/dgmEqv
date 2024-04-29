
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Renewable Energy','Non-renewable Energy','Distribution','Storage','Utilities','Maintenance','Regulatory']
data = [85,25,90,60,50,30,20]
line_labels = ['Type','Number']

num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(1, 1, 1, polar=True)

width = sector_angle
for i in range(len(data)):
    ax.bar(i * sector_angle, data[i], width=width, label=data_labels[i])

ax.set_xticks(np.arange(num_categories) * sector_angle)
ax.set_xticklabels(data_labels, fontsize=14)
ax.legend(bbox_to_anchor=(1.3, 1.05))
ax.set_title('Energy and Utilities: Number of Companies by Type', fontsize=18)

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231225-125808_21.png')
plt.clf()