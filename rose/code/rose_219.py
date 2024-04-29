
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Humanitarian', 'Environment', 'Education', 'Social', 'Animal Welfare', 'Health', 'Arts and Culture']
data = [40, 30, 50, 60, 20, 10, 5]
line_labels = None

num_categories = len(data)
sector_angle = (2 * np.pi) / num_categories

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

# Plot each sector as a bar
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i])

# Add legend and set the position to prevent overlapping with charts
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', labels=data_labels)

# Set the ticks at the center of each sector
ax.set_xticks(np.arange(sector_angle / 2, 2 * np.pi, sector_angle))
ax.set_xticklabels(data_labels, fontsize=10, rotation=90)

# Set the title
ax.set_title('Number of Nonprofit Organizations by Type in 2021', fontsize=20)

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-032010_32.png')
plt.clf()