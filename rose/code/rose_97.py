
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Public', 'Private', 'Technical', 'Liberal Arts', 'Online']
data = [50, 30, 20, 10, 5]
line_labels = ['Institution Type']

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='polar')

num_categories = len(data)
sector_angle = (2 * np.pi) / num_categories

for i, value in enumerate(data):
    ax.bar(i * sector_angle, value, width=sector_angle, color=plt.cm.jet(i / num_categories), edgecolor='white', label=data_labels[i])

ax.legend(bbox_to_anchor=(1.2, 0.7), loc="upper left")
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories+1)[:-1])
ax.set_xticklabels(data_labels, fontsize=12, rotation=90)
ax.set_title('Number of Institutions by Type in the Education System', fontsize=14)
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_86.png')
plt.clf()