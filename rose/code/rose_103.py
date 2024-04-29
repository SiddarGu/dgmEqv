
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Nature Tourism', 'Cultural Tourism', 'Adventure Tourism', 'Business Tourism', 'Religious Tourism', 'Eco Tourism', 'Medical Tourism']
data = [35, 42, 25, 21, 30, 18, 12]
line_labels = ["Type of Tourism", "Number"]

sector_angle = (2 * np.pi) / len(data_labels)

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, polar=True)

ax.set_theta_direction(-1)
ax.set_theta_zero_location('N')
ax.set_title("Types of Tourism and Their Popularity in 2021")

ax.set_xticks(np.linspace(0, 2 * np.pi, len(data_labels), endpoint=False))
ax.set_xticklabels(data_labels, rotation=90, wrap=True)

colors = ['r', 'g', 'b', 'y', 'm', 'k', 'c']

for i in range(len(data)):
    ax.bar(sector_angle * i, data[i], width=sector_angle, bottom=0.0, color=colors[i], label=data_labels[i])

ax.legend(bbox_to_anchor=(1.2, 1), loc='upper right')

plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_97.png')
plt.clf()