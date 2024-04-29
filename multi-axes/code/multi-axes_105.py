
import matplotlib.pyplot as plt 
import numpy as np 

#Transform the given data into three variables: data_labels, data, line_labels.
data_labels = ['Number of Tourists (in Thousands)', 'Average Stay (in Nights)','Revenue (in Millions of Dollars)']
line_labels = ['Hotels and Accommodations', 'Sightseeing','Outdoor Adventures', 'Local Cuisine', 'Shopping', 'Cultural Attractions', 'Wellness and Spa', 'Nightlife']
data = np.array([[1720,4.5,4460], 
                 [1040,2.9,980],
                 [530,3.2,660], 
                 [830,1.7,2120], 
                 [570,4.1,720],
                 [650,3.4,720],
                 [400,3.8,590],
                 [200,2.6,490]])

#Create figure before plotting, i.e., add_subplot(111) follows plt.figure(). The value of figsize should be set larger than 20 to prevent content from being displayed.
fig = plt.figure(figsize=(16,12))
ax1 = fig.add_subplot(111)

#The first column of data array, i.e., data[:,0] is plotted first, whose y-axis is unique to data[:,0] and defined as the primary y-axis in the multi-axes chart, while the x-axis is shared. 
ax1.bar(line_labels, data[:,0], label=data_labels[0], color='lightblue', width=0.3, alpha=0.8)
ax1.set_xlabel('Category')
ax1.set_ylabel(data_labels[0], color='lightblue')
ax1.tick_params('y', colors='lightblue')

#Then, the second column of data array, i.e. data[:,1], is plotted after using twinx to overlay a new ax, named as ax2 on the first plot, where the x-axis is reused from the first plot and the y-axis is unique for data[:, 1].
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], '-o', label=data_labels[1], color='red', alpha=0.8)
ax2.set_ylabel(data_labels[1], color='red')
ax2.tick_params('y', colors='red')

#After that, the third column of data array (if possible), i.e. data[:,2], is plotted after using another twinx, named as ax3 to overlay another new ax on the first plot, where the x-axis is reused from the first plot and the y-axis is unique for data[:, 2].
ax3 = ax1.twinx()
ax3.plot(line_labels, data[:,2], '-s', label=data_labels[2], color='green', alpha=0.8)
ax3.set_ylabel(data_labels[2], color='green')
ax3.tick_params('y', colors='green')

#By analogy, before plotting each column data, a new ax need to be created based on the first plot.
#The primary y-axis is naturally positioned on the left side of the chart, with other y-axes placed on the right side.
ax3.spines['right'].set_position(('axes', 1.1))

#If there are multiple bar charts, it's a must to seperate the bars of different charts by adjusting their positions, i.e., the first parameter in bar(). Other parameters in bar() like width, colors, alpha, etc, can be set differently for different bar charts to ensure they are distinct and non-overlapping.
#If there are area charts, set the alpha parameter smaller than 0.6 to avoid occlusion of other charts. The initial value of its y-axis should be positioned on the same level as x-axis.

#Label all axes, and match their colors with the data plotted against them. Using spine() and set_position() for ax3, ax4, ... to seperate different y-axes. The y-axes of ax1 and ax2 should not use spine() or set_position().

#Show the legends of all plots at different positions, ensuring it does not overlap with other legends and not interfere with data, title and axes.
ax1.legend(loc='upper left')
ax2.legend(loc='upper center')
ax3.legend(loc='upper right')

#Drawing techniques such as background grids can be used.
ax1.grid(alpha=0.3)

#Use Autolocator for all ax, i.e., ax1, ax2, ax3,..., to adjust the range of all y-axes.
ax1.autoscale(enable=True, axis='y', tight=False)
ax2.autoscale(enable=True, axis='y', tight=False)
ax3.autoscale(enable=True, axis='y', tight=False)

#The title of the figure should be  Tourism and Hospitality Industry Performance: Visitor Volume, Duration, and Revenues.
plt.title('Tourism and Hospitality Industry Performance: Visitor Volume, Duration, and Revenues', fontsize=20)

#Automatically resize the image by tight_layout() before savefig().
plt.tight_layout()
# Save figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/44_202312270030.png')

# Clear the current image state
plt.cla()