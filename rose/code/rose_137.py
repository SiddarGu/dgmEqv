
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Rail", "Road", "Waterways", "Air", "Courier"]
data = [90, 85, 70, 45, 30]
line_labels = ["Mode of Transportation", "Number of Shipment"]

fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')

num_categories = len(data_labels)

sector_angle = (2 * np.pi) / num_categories

for idx, category in enumerate(data_labels):
    ax.bar(sector_angle * idx, data[idx], width=sector_angle, label=category, color=plt.cm.Set1(idx))

ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, rotation=90)
ax.set_title('Volume of Goods Transported by Different Modes in 2021')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_147.png')
plt.clf()