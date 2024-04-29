

import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Hunger', 'Education', 'Health', 'Environment', 'Poverty', 'Animal Rights', 'Homelessness']
data = [20, 30, 50, 40, 15, 10, 25]
line_labels = ['Category','Number of Organizations']

num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

fig = plt.figure(figsize=(14,14))
ax = fig.add_subplot(111, projection='polar')
ax.set_theta_direction(-1)
ax.set_theta_zero_location('N')
ax.set_title('Number of Nonprofit Organizations Supporting Different Causes')

# Plotting each sector
for i in range(num_categories):
    ax.bar([sector_angle * i], [data[i]], width=sector_angle, edgecolor='k', linewidth=1, label=data_labels[i])

# Setting the angle and labels of x-axis
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels)

# Setting the legend
ax.legend(data_labels,bbox_to_anchor=(1.45, 0.6))

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_14.png')
plt.clf()