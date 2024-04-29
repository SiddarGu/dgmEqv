
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Primary School', 'Secondary School', 'College', 'University', 'Postgraduate', 'Doctorate']
data = np.array([1000, 800, 600, 400, 200, 100])
line_labels = ['Level of Education']

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

num_categories = len(data)
sector_angle = (2 * np.pi) / num_categories

for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle,
           label=data_labels[i], color=plt.cm.hsv(i / num_categories))

ax.set_xticks(np.arange(0, 2 * np.pi, sector_angle))
ax.set_xticklabels(data_labels, fontsize=15, rotation=45, ha='right', wrap=True)

ax.set_title("Student Numbers in Different Levels of Education in 2021", fontsize=20)

ax.legend(data_labels, bbox_to_anchor=(1.05, 0.5))

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_97.png')
plt.clf()