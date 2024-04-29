
import matplotlib.pyplot as plt
import numpy as np

# transform data into variables
data_labels = ['Primary', 'Secondary', 'Tertiary', 'Postgraduate', 'Vocational']
data = [400,200,100,50,20]
line_labels = ['Education Level', 'Number of Students']

#plot data
plt.figure(figsize=(8, 8))
ax = plt.subplot(1, 1, 1, projection='polar')
num_categories = len(data)
colors = ['darkorange', 'b', 'g', 'r', 'm']
sector_angle = (2 * np.pi) / num_categories

# create sectors for each category
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i], color=colors[i])

# set the legend and label for each sector
ax.legend(loc='center', bbox_to_anchor=(1.3, 0.5), labels=data_labels, fontsize=14)
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories+1)[:-1])
ax.set_xticklabels(data_labels, fontsize=14, rotation=45, ha='center', va='top')
ax.set_title('Student Numbers by Education Level in 2021', fontsize=20)
ax.grid(color='gray', linestyle='-', linewidth=2)
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-112325_41.png')
plt.clf()