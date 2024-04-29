
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Vaccinations', 'Prevention', 'Diagnosis', 'Treatment', 'Rehabilitation', 'Research', 'Education', 'Mental Health', 'Nutrition']
data = [100, 90, 80, 70, 60, 50, 40, 30, 20]
line_labels = ['Category', 'Number']

num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(polar=True)

ax.set_title('Number of Healthcare and Health Services in 2021')

for i, data_value in enumerate(data):
    ax.bar(i * sector_angle, data_value, width=sector_angle,
           color=plt.cm.Set1(i / num_categories), label=data_labels[i])

ax.set_xticks(np.arange(0, 2*np.pi, sector_angle))
ax.set_xticklabels(data_labels, fontsize=9, wrap=True, rotation=-90)

ax.legend(bbox_to_anchor=(1, 1), loc='upper left')

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_51.png')
plt.clf()