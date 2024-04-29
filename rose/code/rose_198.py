
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['General Medicine', 'Surgery', 'Pediatrics', 'Psychiatry', 'Orthopedics', 'Dermatology', 'Neurology']
data = [43, 97, 17, 36, 96, 60, 68]
line_labels = ['Category', 'Number']

fig = plt.figure(figsize=(10, 10))

ax = fig.add_subplot(111, polar=True)

num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i], color=plt.cm.Set2(i))

ax.set_xticks(sector_angle * np.arange(num_categories))
ax.set_xticklabels(data_labels, fontsize=12, horizontalalignment='center')
ax.legend(bbox_to_anchor=(1.2, 0.9))

plt.title('Healthcare and Health: Number of Hospitals Specializing in Each Field', fontsize=14)

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-112325_42.png')

plt.clf()