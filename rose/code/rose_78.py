
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Elementary School', 'High School', 'College', 'Graduate School', 'Doctoral Program']
data = [400, 750, 1500, 1000, 250]
line_labels = ['Level of Education', 'Number of Students']

fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')
ax.set_title('Number of Students by Level of Education in 2021')
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i], color=plt.cm.Set3(i))

ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, rotation=90)
ax.legend(bbox_to_anchor=(1, 1))

fig.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_51.png')
plt.clf()