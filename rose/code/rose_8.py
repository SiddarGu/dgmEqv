
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Beach Resort', 'Mountain Resort', 'Ski Resort', 'Historical Sites', 'Religious Sites', 'National Parks', 'Urban Areas']
data = np.array([1000, 800, 600, 400, 200, 100, 50])
line_labels = ['Destination', 'Number of Tourists']

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='polar')
ax.set_title("Number of Tourists Visiting Different Destinations in 2021")
sector_angle = (2 * np.pi) / len(data_labels)
colors = ['b', 'g', 'm', 'r', 'c', 'y', 'k']

for i in range(len(data_labels)):
    ax.bar(i*sector_angle, data[i], width=sector_angle, bottom=0.0, color=colors[i], label=data_labels[i])

ax.set_xticks(np.linspace(0, 2*np.pi, len(data_labels), endpoint=False))
ax.set_xticklabels(data_labels, fontsize=8, rotation=30, wrap=True)
ax.legend(bbox_to_anchor=(1, 1), fontsize=8)

plt.tight_layout()
fig.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231225-125808_14.png")
plt.clf()