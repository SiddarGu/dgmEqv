
import matplotlib.pyplot as plt 
import numpy as np 

data_labels = ['Physics', 'Chemistry', 'Mathematics', 'Computer Science', 'Mechanical Engineering', 'Electrical Engineering', 'Aerospace Engineering']
line_labels = ['Number of Projects']
data = np.array([[50], [40], [30], [20], [15], [10], [5]])

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='polar')

num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i], color=f'C{i}')

ax.legend(bbox_to_anchor=(1, 0.5), loc='center left')
ax.set_xticks(np.arange(0, 2 * np.pi, sector_angle))
ax.set_xticklabels(data_labels, rotation=90)
ax.set_title('Number of Science and Engineering Projects in 2021')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-112325_44.png')
plt.clf()