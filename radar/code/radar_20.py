
import matplotlib.pyplot as plt
import numpy as np

#Transform the given data into three variables: data_labels, data, line_labels.
data_labels = ['Website A', 'Website B', 'Website C', 'Website D']
line_labels = ['Traffic', 'Engagement', 'Conversions', 'Brand Awareness', 'Retention']
data = np.array([[3, 5, 7, 9], [4, 6, 8, 10], [2, 4, 6, 8], [5, 7, 9, 11], [7, 9, 11, 13]])

#Plot the data with the type of radar chart, i.e., set 'polar=True'.
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, polar=True)

#Create figure before plotting, i.e., add_subplot() follows plt.figure().
#Evenly space the axes for the number of data points.
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

#Iterate over each row in the data array, append the first numerical element of that row to its end for close-loop plotting of data lines. 
#The plottig of different data lines should use different colors.
for i, d in enumerate(data):
    d = np.append(d, d[0])
    ax.plot(angles, d, 'o-', color=plt.cm.Set1((i+1)/len(data)), label=line_labels[i])

#During each iteration, besides plotting data lines, also generate a angle-like radius vector with constant values,
#i.e. np.full_like(angles, (iteration index+1) * maximum of all data / total iteration number), and use each radius and angle vector to draw multiple straight lines as gridlines with a single color.
    for j in range(len(data_labels)):
        ax.plot(angles[j], d[j], '-', color='#cccccc')

#Plot the axis label by using set_thetagrids(angles[:-1] * 180/np.pi, data_labels).
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, fontsize=14, rotation=45, wrap=True)

#Adjust the radial limits to accommodate the maximum of data.
ax.set_rlim(0, np.max(data))

#For the plot of legend, use get_legend_handles_labels() to plot the data lines.
#The positioning of the legend should not interfere with the chart and title.
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, loc=(0.9, 0.95), fontsize=12, bbox_to_anchor=(1.1, 1.05))

#Drawing techniques such as background grids can be used.
#Remove the circular gridlines and background, i.e., ax.yaxis.grid(False), ax.spines['polar'].set_visible(False).
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)

#The title of the figure should be Social Media and the Web - Performance Compariso.
plt.title("Social Media and the Web - Performance Compariso", fontsize=16)

#Clear the current image state at the end of the code.
plt.tight_layout()
#The image must be saved as /cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/20.png.
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/20.png')

plt.clf()