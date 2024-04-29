
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['History', 'Languages', 'Economics', 'Psychology', 'Sociology', 'Anthropology', 'Political Science', 'Art','Philosophy']
line_labels = ['Number of Students']
data = np.array([[230, 180, 150, 130, 100, 90, 80, 50, 30]])

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='polar')
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

for i in range(num_categories):
    ax.bar(sector_angle * i, data[0][i], width=sector_angle, label=data_labels[i])

ax.set_xticks(sector_angle * np.arange(num_categories))
ax.set_xticklabels(data_labels, fontsize=10)
ax.legend(data_labels, bbox_to_anchor=(1.2,1.2), fontsize=10)
ax.set_title("Number of Students Enrolled in Social Science and Humanities Programs in 2021")
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_54.png')
plt.close()