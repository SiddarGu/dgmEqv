
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels.
data_labels = ['Q1', 'Q2', 'Q3', 'Q4']
line_labels = ['Social Media', 'Network Security', 'Cloud Storage', 'Online Shopping', 'Artificial Intelligence']
data = np.array([[60, 65, 70, 75],
                 [85, 90, 95, 100],
                 [75, 80, 85, 90],
                 [70, 75, 80, 85],
                 [95, 100, 105, 110]])

# Plot the data with the type of radar chart, i.e., set 'polar=True'. Create figure before plotting, i.e., add_subplot() follows plt.figure().
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

# Evenly space the axes for the number of data points. Set angles as np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True).
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Iterate over each row in the data array, append the first numerical element of that row to its end for close-loop plotting of data lines.
# The plottig of different data lines should use different colors.
for i, line in enumerate(data):
    line = np.append(line, line[0])
    ax.plot(angles, line, color=plt.cm.jet(i/len(data)), linewidth=3, label=line_labels[i]
             )
    ax.fill(angles, line, color=plt.cm.jet(i/len(data)), alpha=0.2)

# During each iteration, besides plotting data lines, also generate a angle-like radius vector with constant values,
# i.e. np.full_like(angles, (iteration index+1) * maximum of all data / total iteration number), and use each radius and angle vector to draw multiple straight lines as gridlines with a single color.
max_data = np.max(data)
for i in range(len(data)):
    ax.plot(angles, np.full_like(angles, (i+1) * max_data/len(data)), color='black', linewidth=0.5, alpha=0.5)

# Plot the axis label by using set_thetagrids(angles[:-1] * 180/np.pi, data_labels). Adjust the radial limits to accommodate the maximum of data.
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_ylim(0, max_data)

# For the plot of legend, use handles, labels = ax.get_legend_handles_labels(), ax.legend(handles, line_labels, loc="upper right") to plot the legend of data lines. The positioning of the legend should not interfere with the chart and title.
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

# Drawing techniques such as background grids can be used. Remove the circular gridlines and background, i.e., ax.yaxis.grid(False), ax.spines['polar'].set_visible(False).
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)

# The title of the figure should be  Technology and Internet Usage in 2023.
ax.set_title('Technology and Internet Usage in 2023')

# Automatically resize the image by tight_layout() before savefig().
plt.tight_layout()

# The image must be saved as /cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/4.png.
# Save path is absolute path which is completedly the same as /cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png.
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/4.png')

# Clear the current image state at the end of the code.
plt.clf()