
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Transform the given data into three variables: data_labels, data, line_labels.
data_labels = np.array(['Revenue Collected (Billion $)','Compliance (Score)','Taxpayers (Millions)','Ease of Compliance (Score)'])
data = np.array([[3000,70,85,500],[2500,75,80,700],[1500,65,70,600],[1000,60,65,1200],[500,55,60,40]])
line_labels = np.array(['Income Tax','Corporate Tax','Property Tax','GST','International Tax'])

# Plot the data with the type of bubble chart.
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot()

# For each row of data, the third value is mapped to the bubble size, and the fourth value is mapped to the color value.
# The color should be normalized to the range of cmap values, 
# the bubble size should range from 60 to 500 by normalization, 
# and parameters can be set to accurately reflect the differences in data values.
sc = ax.scatter(data[:,0], data[:,1], c=data[:,3], s=(data[:,2]-data[:, 2].min())*600 + 600, cmap=cm.get_cmap('Spectral'), label=None)

# During each iteration of plotting, you must also scatter an empty point, 
# i.e., ax.scatter([], [], label=line_label), by keeping the same color. The size must be set as the default size, i.e., 20.
for i in range(len(line_labels)):
    ax.scatter([], [], c=sc.cmap(sc.norm(data[i,3])), s=20, label=line_labels[i]+' '+str(data[i,2]))

# Plot the legend with the title, by using ax.legend(title=data_labels[2]).
ax.legend(title=data_labels[2], loc='upper left')

# Add a color bar for the bubble colors using the ScalarMappable object with Normalize based on the range of color value. 
# Place the color bar in a location that doesn't interfere with the legend or the main plot. 
# Set the title of the color bar by data_labels[3].
cb = fig.colorbar(sc, ax=ax)
cb.set_label(data_labels[3])

# Drawing techniques such as background grids and other parameter settings can be adjusted.
ax.grid(axis='both')
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

# Show the labels of two axes.
ax.set_title('Tax Compliance and Revenue Collection Around the Globe')

# Automatically resize the image by tight_layout() before savefig().
plt.tight_layout()

# The image must be saved as /cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/6_2023122261440.png.
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/6_2023122261440.png')

# Clear the current image state at the end of the code.
plt.clf()