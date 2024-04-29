

import matplotlib.pyplot as plt
import numpy as np

# transform the given data into three variables
data_labels = ['Training', 'Recruiting', 'Performance Management', 'Compensation', 'Employee Relations', 'Organizational Development', 'Employee Wellness']
data = [43, 97, 17, 36, 96, 60, 68] 
line_labels = []

# create figure before plotting
plt.figure(figsize=(8, 8))

# set up the axes in polar coordinates
ax = plt.subplot(111, projection='polar')

# calculate the sector angle
sector_angle = (2 * np.pi) / len(data_labels)

# plot the data with the type of rose chart
for i, (r, l) in enumerate(zip(data, data_labels)):
    ax.bar(i * sector_angle, r, width=sector_angle, bottom=0.0, label=l, color=plt.cm.Set1(i / len(data_labels)))

# set the labels of each sector
ax.set_xticks(np.linspace(0, 2 * np.pi, len(data_labels), endpoint=False))
ax.set_xticklabels(data_labels)

# reposition the legend
ax.legend(bbox_to_anchor=(1, 0), loc='lower right')

# set the title of the figure
plt.title('Number of Human Resources Programs Implemented in 2021')

# use tight_layout() to automatically resize the image
plt.tight_layout()

# save the figure
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-070122_13.png')

# clear the current image state
plt.clf()