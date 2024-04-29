import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# pre-process the data into desired format
data_string = "Department,Number of Employees,Average Salary (K$),Training Hours per Employee\n IT,50,70,30\n Marketing,40,65,25\n Sales,60,80,32\n Finance,30,75,28\n Human Resources,20,70,35"
data_lines = data_string.split('\n')
header = data_lines[0].split(',')
x_values = [x.split(',')[0] for x in data_lines[1:]]
y_values = header[1:]
data = np.array([list(map(np.float32, x.split(',')[1:])) for x in data_lines[1:]])

# create figure and 3D subplot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# iterate over y_values to plot each column of data
for i, y_label in enumerate(y_values):
    ax.bar3d(np.arange(len(x_values)), 
             [i]*len(x_values), 
             np.zeros(len(x_values)), 
             0.4, 0.8, data[:, i], 
             color=plt.cm.viridis(i/len(y_values)), 
             alpha=0.6)

# set x, y labels and ticks
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=45, ha='right')
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, ha='left')

# grid, title and viewing angle
ax.grid(True)
ax.view_init(30, -60)
ax.set_title('Employee Management Analysis by Department')

# resize the image and save
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/146_202312302235.png', format='png', dpi=150)

# clear figure
plt.close(fig)
