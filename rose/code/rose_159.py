
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Primary School', 'Secondary School', 'Undergraduate', 'Graduate', 'Postgraduate', 'Doctoral']
data = [500, 400, 300, 200, 100, 50]
line_labels = ['Level of Education','Number of Students']

fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot(111, projection='polar')

num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle,
           label=data_labels[i], edgecolor='black', color=plt.cm.get_cmap('Set2')(i))

ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)
ax.set_xticks(sector_angle * np.arange(num_categories))
ax.set_xticklabels(data_labels, rotation=90)
ax.set_title('Number of Students at Different Education Levels in 2021')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_5.png')
plt.clf()