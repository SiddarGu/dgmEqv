
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Solar Power', 'Wind Power', 'Hydroelectric', 'Natural Gas', 'Petroleum', 'Nuclear']
data = [87, 66, 48, 35, 21, 12]
line_labels = ['Type of Energy', 'Number of Customers']

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='polar')

num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

for i in range(num_categories):
    ax.bar(x=i * sector_angle, 
           width=sector_angle, 
           bottom=0.0, 
           height=data[i],
           color=plt.cm.Set1(i / num_categories),
           label=data_labels[i])

ax.legend(bbox_to_anchor=(1.2, 1.0))
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=12, rotation=90)
ax.set_title('Energy Usage by Type of Source in 2021', fontsize=14)
plt.tight_layout()

plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/1.png')
plt.clf()