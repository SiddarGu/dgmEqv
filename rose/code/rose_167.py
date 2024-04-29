
import matplotlib.pyplot as plt
import numpy as np

data = [['Hotels', 1000], ['Backpackers', 800], ['Bed and Breakfast', 400],
        ['Hostels', 200], ['Guesthouses', 100], ['Campgrounds', 50]]

data_labels = list(map(lambda x: x[0], data))
data = list(map(lambda x: x[1], data))
line_labels = ['']

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

num_categories = len(data)
sector_angle = (2 * np.pi) / num_categories

for i, v in enumerate(data):
    ax.bar((i * sector_angle) - (sector_angle / 2), v, width=sector_angle, bottom=0.0, label=data_labels[i])

ax.legend(data_labels, bbox_to_anchor=(1.2, 0.5))

ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=10)

ax.set_title('Number of Tourists Staying at Different Accommodations in 2021')

plt.tight_layout()
fig.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_7.png")

plt.clf()