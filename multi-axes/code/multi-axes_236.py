
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Number of Participants', 'Number of Attendees', 'Average Ticket Price (USD)']
line_labels = ['Music Festival', 'Ballet Performance', 'Art Exhibitions', 'Theater', 'Movie Showing', 'Opera', 'Comedy Shows', 'Dance Performance', 'Museum']
data = np.array([[5400, 352000, 45], [4200, 165000, 45], [6700, 250000, 50], [5100, 183000, 35], [7800, 270000, 25], [4500, 180000, 50], [5800, 220000, 30], [6200, 210000, 30], [5600, 250000, 45]])

# Create figure before plotting, i.e., add_subplot(111) follows plt.figure()
fig = plt.figure(figsize=(15,10))
ax1 = fig.add_subplot(111)

# The first column of data array, i.e., data[:,0] is plotted first, whose y-axis is unique to data[:,0] 
ax1.bar(line_labels, data[:,0], width=0.8, alpha=0.6, color='#006699')
ax1.set_ylabel(data_labels[0], color='#006699')
ax1.tick_params(axis='y', colors='#006699')

# The second column of data array, i.e. data[:,1], is plotted after using twinx 
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], color='#FF9933', marker='o', linestyle='--', linewidth=2.5, markersize=8)
ax2.set_ylabel(data_labels[1], color='#FF9933')
ax2.tick_params(axis='y', colors='#FF9933')

# The third column of data array, i.e. data[:,2], is plotted after using another twinx
ax3 = ax1.twinx()
ax3.spines['right'].set_position(('axes', 1.1))
ax3.plot(line_labels, data[:,2], color='#CC0066', marker='s', linestyle='-', linewidth=2.5, markersize=8)
ax3.set_ylabel(data_labels[2], color='#CC0066')
ax3.tick_params(axis='y', colors='#CC0066')

# Label all axes and match their colors with the data plotted against them 
ax1.set_xlabel('Category')
ax1.set_title('Arts and Culture Events: Participation, Attendance, and Ticket Pricing Trends')

# Show the legends of all plots at different positions
ax1.legend(['Number of Participants'], loc='upper center', bbox_to_anchor=(0.3, -0.05))
ax2.legend(['Number of Attendees'], loc='upper center', bbox_to_anchor=(0.5, -0.05))
ax3.legend(['Average Ticket Price (USD)'], loc='upper center', bbox_to_anchor=(0.7, -0.05))

# Drawing techniques such as background grids can be used
plt.grid(linestyle='--', linewidth=1, alpha=0.2)

# Use Autolocator for all ax, i.e., ax1, ax2, ax3, ..., to adjust the range of all y-axes
ax1.autoscale()
ax2.autoscale()
ax3.autoscale()

# Automatically resize the image by tight_layout() before savefig()
plt.tight_layout()

# The image must be saved as 
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/23_2023122270030.png')

# Clear the current image state at the end of the code
plt.clf()