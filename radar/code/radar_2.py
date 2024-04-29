
import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Employment Law', 'Family Law', 'Criminal Law', 'Tax Law', 'Civil Law']
data = np.array([[35,21,47,59,82],
                 [12,25,32,45,56],
                 [50,60,70,80,90],
                 [210,220,240,260,280],
                 [20,30,40,50,60]])
line_labels = ['Number of Cases (k)', 'Number of Practitioners (k)', 
               'Percentage of Successful Cases (%)', 'Average Legal Fees (USD/h)',
               'Percentage of Disputes Solved (%)']

# Plot the data with the type of radar chart, i.e., set 'polar=True'
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

# Create figure before plotting, i.e., add_subplot() follows plt.figure()
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
data = np.concatenate((data, data[:, 0:1]), axis=1)

# Iterate over each row in the data array, append the first numerical element of that row
# to the end of that row for close-loop plotting of data lines
for i in range(len(data)):
    ax.plot(angles, data[i], label=line_labels[i], linewidth=1.5, color='C' + str(i))

# Evenly space the axes for the number of data points
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

# Adjust the radial limits to accommodate the maximum of data
ax.set_rlim(-0.5, np.max(data) + 0.5)

# Plot the axis label by using set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.get_legend_handles_labels()
plt.legend(loc='upper right')

# Drawing techniques such as background grids can be used
ax.grid(True)

# The title of the figure should be Law and Legal Affairs Performance Analysis - 2023
plt.title('Law and Legal Affairs Performance Analysis - 2023')

# Automatically resize the image by tight_layout() before savefig()
plt.tight_layout()

# The image must be saved as /cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/17_202312262320.png
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/17_202312262320.png')

# Clear the current image state at the end of the code
plt.clf()