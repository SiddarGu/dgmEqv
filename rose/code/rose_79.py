

import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Furniture', 'Electronics', 'Toys', 'Clothing', 'Appliances', 'Automobiles', 'Textiles', 'Machinery']
data = [90, 150, 50, 80, 60, 120, 90, 70]
line_labels = ['Product Type', 'Number of Units']

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='polar')
sector_angle = (2 * np.pi) / len(data_labels)

for i in range(len(data_labels)):
    ax.bar(i * sector_angle, data[i], width=sector_angle, label=data_labels[i], color=plt.cm.Set2(i))

ax.set_xticks(np.arange(len(data_labels)) * sector_angle + sector_angle / 2)
ax.set_xticklabels(data_labels, fontsize=15, rotation=90)
ax.legend(bbox_to_anchor=(1.1, 1.1))
ax.set_title('Number of Units Manufactured in 2021', fontsize=20, y=1.1)
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_52.png')
plt.clf()