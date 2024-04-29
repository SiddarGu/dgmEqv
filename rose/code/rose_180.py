
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Mathematics', 'Physics', 'Chemical Engineering', 'Mechanical Engineering', 'Computer Science', 'Civil Engineering', 'Electrical Engineering', 'Aerospace Engineering']
data = [50, 80, 60, 75, 90, 45, 70, 40]
line_labels = []

fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot(111, projection='polar')
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

for i in range(num_categories):
    line_labels.append(data_labels[i])
    ax.bar(i * sector_angle, data[i], width=sector_angle, label=data_labels[i], color=np.random.rand(3,))

ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, rotation=90, wrap=True)
ax.legend(bbox_to_anchor=(1.1, 1.05))
ax.set_title('Number of Students Pursuing Engineering and Science Degrees in 2021')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-112325_12.png')
plt.clf()