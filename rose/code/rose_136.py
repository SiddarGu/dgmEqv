
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Fast Food", "Italian", "Chinese", "Mexican", "Japanese", "Indian", "Mediterranean", "Thai", "French"]
data = [200, 180, 150, 120, 100, 70, 50, 30, 20]
line_labels = ["Food Type", "Number of Restaurants"]

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='polar')

num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

for i in range(num_categories):
    ax.bar(i * sector_angle, data[i], width=sector_angle, color=plt.cm.tab20(i), label=data_labels[i])

ax.legend(data_labels, bbox_to_anchor=(1.25, 1), fontsize='large')
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories + 1)[:-1])
ax.set_xticklabels(data_labels, fontsize='large', wrap=True, rotation=45)
ax.set_title("Number of Restaurants by Cuisine in 2021", fontsize='xx-large')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_146.png')
plt.close(fig)