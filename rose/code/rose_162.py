
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Social Policy", "Economic Policy", "International Policy", "Environmental Policy", "Education Policy", "Health Policy", "Defense Policy", "Fiscal Policy"]
data = [45, 56, 87, 34, 76, 67, 29, 20]
line_labels = ["Policy Area", "Number of Policies"]

fig = plt.figure(figsize=(16, 9))
ax = fig.add_subplot(111, projection='polar')
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories
for i in range(num_categories):
    ax.bar([sector_angle * i], [data[i]], width=[sector_angle], label=data_labels[i])

ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax.set_title('Number of Policies Created by Government in 2021')
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, wrap=True, rotation=90)
plt.tight_layout()

plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_56.png')
plt.clf()