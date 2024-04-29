
import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into three variables: data_labels, data, line_labels 
data_labels = ["Q1", "Q2", "Q3", "Q4"]
line_labels = ["Customer Satisfaction (%)", "Product Quality (%)", "Delivery Speed (%)", "Product Availability (%)", "Return Policy (%)"]
data = np.array([[85, 90, 95, 100], [90, 95, 100, 105], [80, 85, 90, 95], [75, 80, 85, 90], [70, 75, 80, 85]])

# Plot the data with the type of radar chart, i.e., set 'polar=True' 
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

# Iterate over each row in the data array, append the first numerical element of that row to the end of that row for close-loop plotting of data lines
data = np.concatenate((data, data[:, 0:1]), axis=1)

# The plottig of different data lines should use different colors
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
ax.plot(angles, data[0], 'o-', c='b', label=line_labels[0])
ax.plot(angles, data[1], 'o-', c='r', label=line_labels[1])
ax.plot(angles, data[2], 'o-', c='g', label=line_labels[2])
ax.plot(angles, data[3], 'o-', c='c', label=line_labels[3])
ax.plot(angles, data[4], 'o-', c='m', label=line_labels[4])

# Plot the axis label by using set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, fontsize=18)

# Adjust the radial limits to accommodate the maximum of data
ax.set_rlim(50, 110)

# For the plot of legend, use ax.get_legend_handles_labels() and legend to plot the legend of data lines. The positioning of the legend should not interfere with the chart and title.
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc='upper right', bbox_to_anchor=(1.3, 1))

# Drawing techniques such as background grids can be used.
ax.grid(True)

# The image must be saved as /cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/20_202312262320.png
plt.title('Retail and E-commerce Performance Evaluation - 2021', fontsize=20)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/20_202312262320.png')

# Clear the current image state at the end of the code
plt.clf()