import numpy as np
import matplotlib.pyplot as plt

# Transforming the given data into variables
data_labels = ['Child Aid', 'Healthcare Aid', 'Educational Aid', 'Environmental Aid', 'Animal Welfare']
line_labels = ['Fund Utilization (%)', 'Donor Satisfaction (Score)', 'Project Impact (Score)', 'Transparency Score', 'Volunteer Satisfaction (Score)', 'Efficiency Score']
data = np.array([[85, 80, 75, 70, 65], 
                 [90, 85, 80, 75, 70], 
                 [75, 80, 85, 90, 90], 
                 [80, 85, 90, 95, 85], 
                 [70, 75, 80, 85, 90], 
                 [60, 65, 70, 75, 80]])

# Creating a figure
fig = plt.figure(figsize=(8, 8))

# Adding a polar subplot
ax = fig.add_subplot(111, polar=True)

# Setting the angles for the axes
angles = np.linspace(0, 2*np.pi, len(data_labels)+1, endpoint=True)

# Closing the loop for plotting
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Plotting the data lines with different colors
colors = ['blue', 'red', 'green', 'orange', 'purple', 'pink']
for i, row in enumerate(data):
    ax.plot(angles, row, color=colors[i], marker='o', label=line_labels[i])

# Setting the axis labels
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# Adjusting the radial limits
ax.set_ylim(0, np.max(data))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i:.1f}' for i in range(1, len(data) + 1)], angle=0)

# Plotting the legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc='upper right', bbox_to_anchor=(1.2, 1))

# Adding a title
plt.title('Performance Analysis of Charity and Nonprofit Organizations')

# Adding background grids
ax.grid(True)

# Resizing the image
plt.tight_layout()

# Saving the chart image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/170_202312310100.png')

# Clearing the current image state
plt.clf()