
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels.
data_labels = ['Number of Employees','Hours Worked (Thousands)', 'Average Wage (Dollars)', 'Average Work Week (Hours)']
line_labels = ['Administrators', 'Managers', 'Accountants', 'Human Resources', 'Maintenance Workers', 'Customer Service Reps', 'Security Guards', 'Data Entry Clerks', 'Sales Associates', 'Clerks', 'Janitors']
data = np.array([[788,4808,32,45],
                [1230,5200,50,48],
                [790,3311,25,40],
                [490,2123,30,42],
                [1220,4890,20,40],
                [2890,14000,15,38],
                [690,2540,18,40],
                [789,2590,12,35],
                [1020,4890,25,40],
                [1000,4489,19,38],
                [320,1209,15,35]])

# Create figure before plotting
fig=plt.figure(figsize=(25,10))
ax1=fig.add_subplot(111)

# Plot the data with the type of multi-axes chart
ax1.bar(line_labels,data[:,0],width=0.2,color='red',alpha=0.7)
ax2=ax1.twinx()
ax2.plot(line_labels,data[:,1],color='b',marker='o',linestyle='--',linewidth=2.0)
ax3=ax1.twinx()
ax3.plot(line_labels,data[:,2],color='g',marker='*',linestyle='-.',linewidth=2.0)
ax4=ax1.twinx()
ax4.plot(line_labels,data[:,3],color='y',marker='.',linestyle=':',linewidth=2.0)

# Label all axes, and match their colors with the data plotted against them
ax1.set_xlabel('Category', fontsize=15)
ax1.set_ylabel(data_labels[0], fontsize=15, color='red')
ax2.set_ylabel(data_labels[1], fontsize=15, color='b')
ax3.set_ylabel(data_labels[2], fontsize=15, color='g')
ax4.set_ylabel(data_labels[3], fontsize=15, color='y')

# Using spine() and set_position() for ax3, ax4, ... to seperate different y-axes
ax3.spines['right'].set_position(('outward',90))
ax4.spines['right'].set_position(('outward',180))

# Show the legends of all plots at different positions
ax1.legend(data_labels[0],loc=1)
ax2.legend(data_labels[1],loc=2)
ax3.legend(data_labels[2],loc=3)
ax4.legend(data_labels[3],loc=4)

# Drawing techniques such as background grids can be used
ax1.grid(linestyle='--',linewidth=0.5)

# Use Autolocator for all ax, i.e., ax1, ax2, ax3, ..., to adjust the range of all y-axes
ax1.yaxis.set_major_locator(plt.AutoLocator())
ax2.yaxis.set_major_locator(plt.AutoLocator())
ax3.yaxis.set_major_locator(plt.AutoLocator())
ax4.yaxis.set_major_locator(plt.AutoLocator())

# The title of the figure should be 
plt.title('Human Resources and Employee Management: Workforce Composition and Labor Trends', fontsize=15)

# Automatically resize the image by tight_layout()
plt.tight_layout()

# The image must be saved as
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/5_202312251608.png')

# Clear the current image state at the end of the code.
plt.clf()