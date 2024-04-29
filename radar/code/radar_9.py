
import matplotlib.pyplot as plt
import numpy as np

#Transform the given data into three variables: data_labels, data, line_labels. 
data_labels = ['Popularity','Viewership','Prize Money','Sponsorship','Fan Engagement']
line_labels = ['Football','Basketball','Tennis','Hockey']
data = [[90,95,80,85,95],[85,90,75,80,90],[80,85,70,75,85],[75,80,65,70,80]]

# Plot the data with the type of radar chart, i.e., set 'polar=True'. 
fig = plt.figure(figsize=(9, 9))
ax = fig.add_subplot(111, polar=True)

# Create figure before plotting, i.e., add_subplot() follows plt.figure(). 
# Evenly space the axes for the number of data points. 
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

# Iterate over each row in the data array, append the first numerical element of that row to its end for close-loop plotting of data lines. 
# The plottig of different data lines should use different colors.
for i in range(len(line_labels)):
    values = data[i]
    values = np.append(values, values[0])
    ax.plot(angles, values, linewidth=2, label=line_labels[i], color=plt.cm.Set1(i))

# During each iteration, besides plotting data lines, also generate a angle-like radius vector with constant values, 
# i.e. np.full_like(angles, (iteration index+1) * maximum of all data / total iteration number), 
# and use each radius and angle vector to draw multiple straight lines as gridlines with a single color.
ax.set_rgrids([20, 40, 60, 80, 100])

# Plot the axis label by using set_thetagrids(angles[:-1] * 180/np.pi, data_labels). 
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, fontsize=15)

# Adjust the radial limits to accommodate the maximum of data.
ax.set_ylim(0,100)

# For the plot of legend, use get_legend_handles_labels() to plot the data lines. 
# The positioning of the legend should not interfere with the chart and title.
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, bbox_to_anchor=(0.1, 0.1))

# Drawing techniques such as background grids can be used. 
# Remove the circular gridlines and background, i.e., ax.yaxis.grid(False), ax.spines['polar'].set_visible(False).
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)

# The title of the figure should be  Sports and Entertainment Industry Metrics.
ax.set_title('Sports and Entertainment Industry Metrics', fontsize=20)

# The image must be saved as /cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/9.png.
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/9.png')

# Clear the current image state at the end of the code.
plt.clf()