
import numpy as np
import matplotlib.pyplot as plt

# Transform the given data into three variables: y_values, data, x_values. 
y_values=['Manufactured Output (Units)','Average Cost ($)','Average Time (Days)']
data=np.array([[800,1000,2000],[1000,1500,2500],[1200,2000,3000],[1500,2500,3500],[2000,3000,4000]])
x_values=['Machinery','Electricals','Automobiles','Clothing','Furniture']

# Create figure before plotting
fig=plt.figure(figsize=(10,5))
ax=fig.add_subplot(111, projection='3d')

# Plot the data with the type of 3D bar chart. 
for i in range(len(y_values)):
    xs=np.arange(len(x_values))
    ys=[i]*len(x_values)
    ax.bar3d(xs, ys, [0]*len(x_values), 0.5, 0.5, data[:, i], shade=True, color='g')

# Set the dimensions of the bars (width, depth, colors, alpha, etc) differently 
ax.set_zlabel('Output and Costs')
ax.set_ylabel('Metrics')
ax.set_xlabel('Categories')
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticklabels(y_values)

# Drawing techniques such as background grids can be used.
ax.grid(b=True, which='major', color='#666666', linestyle='-')
ax.minorticks_on()
ax.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

# The title of the figure should be  Manufacturing and Production Output and Costs Analysis.
ax.set_title('Manufacturing and Production Output and Costs Analysis')

# Automatically resize the image by tight_layout() before savefig().
plt.tight_layout()

# The image must be saved as /cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/14.png
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/14.png')

# Clear the current image state at the end of the code
plt.clf()