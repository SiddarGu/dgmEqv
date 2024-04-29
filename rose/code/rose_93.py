

import matplotlib.pyplot as plt
import numpy as np

# transform the data into three variables
data_labels = ['Psychology','Sociology','Philosophy','Literature','Art\nHistory','History','Anthropology','Political\nScience','Linguistics']
data = [1200,1000,850,900,600,800,250,400,300]
line_labels = []

# create figure
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, polar=True)

# set the number of categories
num_categories = len(data_labels)

# calculate the sector angle
sector_angle = (2 * np.pi) / num_categories

# set up the colors
cmap = plt.get_cmap('tab20')
colors = [cmap(i) for i in range(num_categories)]

# draw the sectors
for i in range(len(data_labels)):
    ax.bar(i * sector_angle, data[i], width=sector_angle,
           label=data_labels[i], color=colors[i])

# reposition the legend
ax.legend(data_labels, bbox_to_anchor=(1.05, 0.0), loc='lower left')

# set the title
ax.set_title('Number of Students Enrolled in Social Science and Humanities Courses in 2021')

# set the ticks
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=14, rotation=45, wrap=True)

# adjust plot size and save
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_81.png')

# clear the current image state
plt.clf()