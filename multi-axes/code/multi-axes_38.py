
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables
data_labels = ['Number of Books Published (Thousands)', 'Number of Articles Published (Thousands)', 'Average Number of Journal Subscribers']
line_labels = ['English Literature', 'Psychology', 'Economics', 'Sociology', 'Political Science', 'Philosophy', 'Anthropology', 'Education', 'History', 'Law']
data = np.array([[950, 1150, 250],
                 [950, 1200, 500],
                 [570, 1300, 400],
                 [680, 1050, 450],
                 [750, 1050, 350],
                 [830, 990, 200],
                 [620, 870, 300],
                 [800, 1090, 380],
                 [820, 1150, 350],
                 [770, 1100, 450]])

# Create the figure
fig = plt.figure(figsize=(15, 10))
ax1 = fig.add_subplot(111)

# Plot the first column of data array, i.e., data[:,0]
ax1.bar(np.arange(len(line_labels)), data[:,0], 0.2, color='b', label=data_labels[0])
ax1.set_xlabel('Category')
ax1.set_ylabel(data_labels[0], color='b')
ax1.tick_params('y', colors='b')

# Overlay the second column of data array, i.e. data[:,1]
ax2 = ax1.twinx()
ax2.bar(np.arange(len(line_labels))+0.2, data[:,1], 0.2, color='g', label=data_labels[1])
ax2.set_ylabel(data_labels[1], color='g')
ax2.tick_params('y', colors='g')

# Overlay the third column of data array, i.e. data[:,2]
ax3 = ax1.twinx()
ax3.plot(np.arange(len(line_labels)), data[:,2], color='r', label=data_labels[2])
ax3.set_ylabel(data_labels[2], color='r')
ax3.tick_params('y', colors='r')

# Seperate the bars of different charts by adjusting their positions
ax1.set_xticks(np.arange(len(line_labels))+0.2)

# Set the alpha parameter to avoid occlusion of other charts
ax3.set_alpha(0.6)

# Label all axes
ax1.set_xticklabels(line_labels)

# Seperate different y-axes
ax3.spines['right'].set_position(('axes', 1.1))

# Show the legends of all plots at different positions
ax1.legend(loc='upper left')
ax2.legend(loc='upper center')
ax3.legend(loc='upper right')

# Drawing techniques such as background grids can be used
ax1.grid(linestyle = ':')

# Set the title of the figure
plt.title('Analysis of Social Sciences and Humanities Publications: Output, Reach, and Subscriber Trends')

# Automatically resize the image
fig.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/45_2023122270030.png')

# Clear the current image state
plt.clf()