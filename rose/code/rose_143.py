
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Air", "Water", "Rail", "Road", "Pipeline"]
data = [1000, 800, 600, 400, 200]
line_labels = ["Mode of Transport", "Volume"]

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection="polar")

num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i])

ax.legend(bbox_to_anchor=(1.05, 0.5), loc="center left")

ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, rotation=45)
ax.set_title("Volume of Goods Transported by Different Modes of Transport in 2021")

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_22.png')
plt.clf()