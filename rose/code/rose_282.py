
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Beer', 'Wine', 'Spirits', 'Coffee', 'Tea', 'Soft Drinks', 'Juice']
line_labels = ['Item', 'Sales']
data = [[150, 100, 80, 50, 35, 20, 15]]

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='polar')
colors = ['#3399FF', '#FF99CC', '#FF6666', '#33FF99', '#FFCC99', '#CCFF66', '#FF9900']
sector_angle = (2 * np.pi) / len(data_labels)

for i, data_label in enumerate(data_labels):
    ax.bar(sector_angle*i, data[0][i], width=sector_angle, color=colors[i], label=data_label)

ax.set_xticks(np.linspace(0, 2 * np.pi, len(data_labels), endpoint=False))
ax.set_xticklabels(data_labels, rotation=45, fontsize=10)
ax.set_title('Sales Figures for Food and Beverage Supplies in 2020')

ax.legend(bbox_to_anchor=(1.3, 1.05))

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-070122_81.png')
plt.clf()