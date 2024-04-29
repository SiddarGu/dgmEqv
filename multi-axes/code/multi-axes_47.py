

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels.
data_labels = ['Category','Number of Participants','Number of Spectators','Average Ticket Price (USD)']
line_labels = ['Football','Basketball','Baseball','Hockey','Golf','Soccer','Tennis','Swimming','Volleyball','Skating']
data = [[2500,10000,25],[1000,4000,40],[3000,9000,20],[2000,7000,30],[1500,3000,50],[4000,9000,20],[800,3000,35],[2000,5000,30],[3000,8000,25],[1500,4000,45]]

# Split the data array from the second dimension to get the data correpsonding to each category.
x_labels = np.array(data_labels[1:])
data_array = np.array(data)
num_participants = data_array[:,0]
num_spectators = data_array[:,1]
avg_ticket_price = data_array[:,2]

# Plot the data with the type of multi-axes chart.
fig = plt.figure(figsize=(15, 10)) # set a larger figsize
ax1 = fig.add_subplot(111)

# The plot type of each category is sequentially decided by the following plot types, i.e., [ bar chart,bar chart,line chart].
# For the plot of each category, overlay the plot on one chart with a shared x-axis and an individual y-axis, a distinct color and marker style, ensuring the y-axes are visually distinct from the primary y-axis. All other y-axes should be positioned opposite the primary y-axis.
# For the plot of different bar charts, set different bar positions to avoid overlapping.
width = 0.2
x1 = np.arange(len(line_labels))
x2 = [i + width for i in x1]
x3 = [i + width for i in x2]
ax1.bar(x1, num_participants, width=width, color='#F08080', label='Number of Participants', alpha=0.6)

# Label each axis with the name of the category it represents, matching the color of the data plotted against it. Using ax.spine and set_position() for the third, fourth, ... y-axes to ensure each y-axis does not overlap with each other.
ax1.set_ylabel('Number of Participants', color='#F08080')
ax1.tick_params('y', colors='#F08080')
ax2 = ax1.twinx()
ax2.bar(x2, num_spectators, width=width, color='#90EE90', label='Number of Spectators', alpha=0.6)
ax2.set_ylabel('Number of Spectators & Average Ticket Price (USD)', color='#90EE90')
ax2.tick_params('y', colors='#90EE90')
ax3 = ax1.twinx()
ax3.spines['right'].set_position(('axes', 1.1))
ax3.plot(x3, avg_ticket_price, marker='o', color='#ADD8E6', linewidth=2.5, label='Average Ticket Price (USD)', alpha=0.6)
ax3.set_ylabel('Average Ticket Price (USD)', color='#ADD8E6')
ax3.tick_params('y', colors='#ADD8E6')

# Drawing techniques such as background grids can be used. Make sure the layout is clean, with no overlapping elements, and all labels and titles are easily readable.
ax1.set_xticks(x2)
ax1.set_xticklabels(line_labels, rotation=45, wrap=True)
ax1.set_title('Sports and Entertainment Participation and Spectator Trends', fontsize=20)
ax1.grid(linestyle='--')

# Automatically resize the image by tight_layout() before savefig().
fig.tight_layout()

# The image must be saved as /cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/12.png.
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/12.png')

# Clear the current image state at the end of the code.
plt.clf()