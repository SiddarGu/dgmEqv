
import matplotlib.pyplot as plt
import numpy as np

#Transform the given data into three variables: data_labels, data, line_labels
data_labels = ["Elementary School","Middle School","High School","University","Vocational College"]
line_labels = ["Students (Number)","Pass Rate (%)","Teacher-Student Ratio (1:N)","Academic Achievement (Score)","Research Output (Publications)"]
data = np.array([[10,30,50,10,30],[95,90,85,80,75],[10,15,20,25,20],[90,85,80,75,70],[20,40,50,60,50]])

# Plot the data with the type of radar chart, i.e., set 'polar=True'
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, polar=True)

#Evenly space the axes for the number of data points
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

#Iterate over each row in the data array, append the first numerical element of that row to the end of that row for close-loop plotting of data lines
data = np.concatenate((data, data[:, 0:1]), axis=1)

# The plottig of different data lines should use different colors
ax.plot(angles, data[0], 'o-', linewidth=2, label=line_labels[0], color='r')
ax.plot(angles, data[1], 'o-', linewidth=2, label=line_labels[1], color='g')
ax.plot(angles, data[2], 'o-', linewidth=2, label=line_labels[2], color='b')
ax.plot(angles, data[3], 'o-', linewidth=2, label=line_labels[3], color='y')
ax.plot(angles, data[4], 'o-', linewidth=2, label=line_labels[4], color='m')

#Plot the axis label
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

#Adjust the radial limits to accommodate the maximum of data
ax.set_rlim(0, np.max(data))

#Plot the legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc=(0.9, 0.95))

#Drawing techniques such as background grids can be used
ax.grid(True)

#The title of the figure should be  Education Quality Evaluation - 2021
plt.title('Education Quality Evaluation - 2021')

#Automatically resize the image by tight_layout() before savefig()
plt.tight_layout()

#The image must be saved as /cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/11_202312262320.png
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/11_202312262320.png")

#Clear the current image state at the end of the code
plt.clf()