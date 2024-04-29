
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as colors
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels. 
# Data_labels represents the labels of each column except the first column. 
# Line_labels represents the labels of each row except the first row. 
# Each line_label should be suffixed with data[i, 2].
# Data represent the numerical array in the data. 
data_labels=['Efficiency (%)','Cost (Billion $)','Research Time (Years)','Innovation (Score)']
data=np.array([[50, 50, 10, 6],
              [60, 40, 8, 7],
              [70, 30, 6, 8],
              [80, 20, 4, 10],
              [90, 10, 2, 9],
              [95, 5, 1, 10]])
line_labels=np.array(['Artificial Intelligence','Robotics','Nanotechnology','3D Printing','Quantum Computing','Automation'])

# Plot the data with the type of bubble chart.
# Create figure before plotting, i.e., add_subplot() follows plt.figure().
plt.figure(figsize=(12, 8))
ax = plt.subplot()

# For the plotting using plt.scatter, the color should be normalized to the range of cmap values, 
# the bubble size should range from 60 to 500 by normalization, 
# and parameters can be set to accurately reflect the differences in data values.
# The label here must set as None, i.e., ax.scatter(data[i, 0], data[i, 1], label=None).
norm=colors.Normalize(vmin=data[:,3].min(),vmax=data[:,3].max())
cmap=cm.ScalarMappable(norm=norm,cmap=cm.jet)
sizes=(500-60)*(data[:,2]-data[:,2].min())/(data[:,2].max()-data[:,2].min())+60
for i in range(6):
    ax.scatter(data[i, 0], data[i, 1], label=None, c=cmap.to_rgba(data[i, 3]), s=sizes[i])

# During each iteration of plotting, you must also scatter an empty point, i.e., ax.scatter([], [], label=line_label), by keeping the same color. The size must be set as the default size, i.e., 20.
for i in range(6):
    ax.scatter([], [], label=line_labels[i]+' '+str(data[i,2]), c=cmap.to_rgba(data[i, 3]), s=20)

# Plot the legend with the title, by using ax.legend(title=data_labels[2]). The legend should not be overlapped with the main plot area and the title.
ax.legend(title=data_labels[2],bbox_to_anchor=(1,1.02))

# Add a color bar for the bubble colors using the ScalarMappable object with Normalize based on the range of color value.
# Place the color bar in a location that doesn't interfere with the legend or the main plot. 
# Set the title of the color bar by data_labels[3].
cbar=plt.colorbar(cmap,ax=ax,fraction=0.046, pad=0.04)
cbar.ax.set_title(data_labels[3])

# Drawing techniques such as background grids and other parameter settings can be adjusted. 
# Show the labels of two axes.
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

# The title of the figure should be Comparing Efficiency and Cost of Innovative Technologies in Science and Engineering.
ax.set_title('Comparing Efficiency and Cost of Innovative Technologies in Science and Engineering', fontsize=18)

# Automatically resize the image by tight_layout() before savefig().
plt.tight_layout()

# The image must be saved as /cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/4_2023122261440.png.
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/4_2023122261440.png', bbox_inches='tight')

# Clear the current image state at the end of the code.
plt.clf()