
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Physics', 'Chemistry', 'Engineering', 'Computer Science', 'Mathematics', 'Astronomy', 'Geology', 'Robotics', 'Nanotechnology']
data = np.array([780, 470, 1020, 320, 590, 120, 230, 220, 130])
line_labels = ['Field', 'Number of Researchers']

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(1, 1, 1, projection='polar')

num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i], color=plt.cm.Dark2(i))

ax.set_xticks(np.arange(0, 2 * np.pi, sector_angle))
ax.set_xticklabels(data_labels)
ax.legend(bbox_to_anchor=(1, 0.7), loc='center right')
ax.set_title('Number of Scientists and Engineers in Different Fields')

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-070122_63.png')
plt.clf()