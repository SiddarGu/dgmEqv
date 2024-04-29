
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

# Transform the given data into three variables: data_labels, data, line_labels. 
data_labels = ["Energy Output (Megawatts)", "Fuel Cost (Billion $)", "Emissions (Kg/MWh)", "Safety (Score)"]
data = np.array([[1800, 1.5, 25, 9], [1600, 1.2, 0, 10], [1400, 2.0, 0, 8], [1200, 0.8, 0, 10], [1000, 1.0, 50, 7], [500, 1.2, 20, 8]])
line_labels = ["Nuclear", "Wind", "Solar", "Hydro", "Coal", "Natural Gas"]

# Plot the data with the type of bubble chart. 
fig = plt.figure()
ax = fig.add_subplot()

# For each row of data, the third value is mapped to the bubble size, and the fourth value is mapped to the color value.
# Plot the data using plt.scatter, the color should be normalized to the range of cmap values, the bubble size should range from 60 to 500 by normalization.
cmap = cm.get_cmap('Greens')
norm = cm.colors.Normalize(vmin=np.min(data[:,3]), vmax=np.max(data[:,3]))
scalar_map = cm.ScalarMappable(norm=norm, cmap=cmap)

for i in range(len(data)):
    size_val = (data[i,2] - np.min(data[:,2])) / (np.max(data[:,2]) - np.min(data[:,2])) * (500 - 60) + 60
    ax.scatter(data[i,0], data[i,1], s=size_val, c=scalar_map.to_rgba(data[i,3]), label=None)
    ax.scatter([], [], s=20, c=scalar_map.to_rgba(data[i,3]), label=line_labels[i] + ": " + str(data[i,2]))

# Plot the legend with the title, by using ax.legend(title=data_labels[2]). 
ax.legend(title=data_labels[2])

# Add a color bar for the bubble colors using the ScalarMappable object with Normalize based on the range of color value. Place the color bar in a location that doesn't interfere with the legend or the main plot. Set the title of the color bar by data_labels[3].
plt.colorbar(scalar_map, ax=ax, extend='both').set_label(data_labels[3])

# Drawing techniques such as background grids and other parameter settings can be adjusted. Show the labels of two axes.
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.grid(linestyle='--', linewidth=0.5)
ax.set_title('Comparing Energy Output and Costs of Different Power Plants')

# Automatically resize the image by tight_layout() before savefig().
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/14_2023122270050.png')

# Clear the current image state at the end of the code.
plt.clf()