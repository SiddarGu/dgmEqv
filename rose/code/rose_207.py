
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['North America','South America','Europe','Asia','Africa','Oceania']
line_labels = ['Region','Number of Tourists']
data = [[85000,70000,80000,95000,56000,45000]]

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='polar')

num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

for i in range(num_categories):
    ax.bar(i * sector_angle, data[0][i], width=sector_angle, label=data_labels[i], color=plt.cm.Set2(i))

ax.legend(bbox_to_anchor=(1.2, 0.5), loc="center left")

ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=9, color='black')

ax.set_title('Number of Tourists Visiting Different Regions in 2021', fontsize=15, color='black')

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-032010_13.png')
plt.clf()