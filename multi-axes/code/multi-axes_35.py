

import matplotlib.pyplot as plt
import numpy as np 
import matplotlib.gridspec as gridspec 

data_labels = ['Number of Graduates (Thousands)', 'Number of Majors (Thousands)', 'Average Starting Salary (Thousands of Dollars)']
data = np.array([[150,200,75],[200,250,70],[220,300,68],[180,220,72],[140,190,77],[170,250,69],[230,320,66],[160,210,73],[130,190,75],[190,280,68]])
line_labels = ['Biomedical Engineering','Computer Science','Electrical and Computer Engineering','Chemical Engineering','Aerospace Engineering','Civil Engineering','Mechanical Engineering','Materials Science and Engineering','Environmental Engineering','Industrial Engineering']

# set the figure size
plt.figure(figsize=(12, 8))

# set the subplot and the position
ax1 = plt.subplot(111)

# plot the bar chart
ax1.bar(line_labels, data[:, 0], width=0.4, color='#0096FF', alpha=0.8)

# set the labels of x and y axis
ax1.set_xlabel('Category', fontsize=13)
ax1.set_ylabel('Number of Graduates (Thousands)', fontsize=13)
ax1.set_xticklabels(line_labels, fontsize=12, rotation=45, wrap=True)

# set the twinx to plot the line chart
ax2 = ax1.twinx()
ax2.set_ylabel('Number of Majors (Thousands)', fontsize=13)
ax2.set_ylim(0, 330)

# plot the line chart
ax2.plot(line_labels, data[:, 1], marker='o', linestyle='-', linewidth=2, markerfacecolor='#FF8C00', markersize=7)

# set the twinx to plot the scatter chart
ax3 = ax1.twinx()
ax3.set_ylabel('Average Starting Salary (Thousands of Dollars)', fontsize=13)
ax3.spines['right'].set_position(('axes', 1.1))
ax3.set_ylim(60, 80)

# plot the scatter chart
ax3.scatter(line_labels, data[:, 2], marker='o', color='#FF0000', alpha=0.7)

# set the twinx to plot the area chart
ax4 = ax1.twinx()
ax4.set_ylabel('Area Chart', fontsize=13)
ax4.spines['right'].set_position(('axes', 1.2))
ax4.set_ylim(0, 100)

# plot the area chart
ax4.fill_between(line_labels, data[:, 0], color='#00FF00', alpha=0.2)

# set the title of the chart
ax1.set_title('Performance of Science and Engineering Graduates: Graduation, Majoring, and Salaries', fontsize=14)

# add grid to the chart
ax1.grid(linestyle='dotted')

# set the legends
ax1.legend(['Number of Graduates (Thousands)'], loc='upper left', bbox_to_anchor=(0., 1.0))
ax2.legend(['Number of Majors (Thousands)'], loc='upper left', bbox_to_anchor=(0., 0.95))
ax3.legend(['Average Starting Salary (Thousands of Dollars)'], loc='upper right', bbox_to_anchor=(1, 1))
ax4.legend(['Area Chart'], loc='upper right', bbox_to_anchor=(1, 0.95))

# adjust the range of all y-axes
ax1.autoscale(enable=True, axis='y', tight=None)
ax2.autoscale(enable=True, axis='y', tight=None)
ax3.autoscale(enable=True, axis='y', tight=None)
ax4.autoscale(enable=True, axis='y', tight=None)

# resize the image
plt.tight_layout()

# save the image
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/19_2023122261325.png")

# clear the current image state
plt.clf()