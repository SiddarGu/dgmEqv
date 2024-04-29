
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Plant Cultivation', 'Animal Husbandry', 'Animal Breeding', 'Organic Farming', 'Irrigation', 'Aquaculture', 'Forestry', 'Livestock', 'Food Processing']
data = [67,90,23,43,56,12,34,18,89]
line_labels = np.arange(len(data_labels)) 

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='polar')

sector_angle = (2*np.pi) / len(data_labels)
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', '#ffa500', '#00aaff']

for i in range(len(data_labels)):
    ax.bar(line_labels[i]*sector_angle, data[i], width=sector_angle, label=data_labels[i], color=colors[i])

ax.set_xticks(line_labels*sector_angle)
ax.set_xticklabels(data_labels, fontsize=15, wrap=True)
ax.set_yticklabels([])
ax.set_title('Quantities of Agriculture and Food Production Fields in 2021', fontsize=20)
ax.legend(bbox_to_anchor=(1.2,0.8))

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_46.png')
plt.cla()