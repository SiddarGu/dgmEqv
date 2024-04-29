
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Accommodation', 'Restaurants', 'Sightseeing', 'Shopping', 'Events', 'Nightlife']
data = [50, 30, 20, 15, 10, 5]
line_labels = ['Category', 'Number']

fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

sector_angle = (2 * np.pi) / len(data_labels)

for i, value in enumerate(data):
    ax.bar(
        sector_angle * i,
        value,
        width=sector_angle,
        edgecolor='black',
        label=data_labels[i],
    )

ax.set_xticks(np.arange(0, 2 * np.pi, sector_angle))
ax.set_xticklabels(data_labels, wrap=True)
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title=line_labels[0])
plt.title('Number of Tourist Attractions in 2021')
fig.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_148.png')
plt.clf()