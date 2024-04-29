import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parse data
data_str = "Department,Undergraduate Students,Graduate Students,PhD Students,n Faculty Members/n Sociology,1200,845,210,60/n Psychology,1500,895,240,75/n Philosophy,800,590,140,45/n History,1050,660,180,70/n Anthropology,920,710,160,50"
data_pairs = [item.split(',') for item in data_str.split('/n')]

#Assume that "n Faculty Members" is "Faculty Members"
data_pairs[0][-1] = "Faculty Members"

x_values = [pair[0] for pair in data_pairs[1:]]
y_values = data_pairs[0][1:]
data = np.array([list(map(int,pair[1:])) for pair in data_pairs[1:]], dtype=np.float32)

# Create a 3D figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Determine the width and depth of a single bar
dx = 0.3
dy = 0.8
dz = [0] * len(x_values)

# Iterate over data to create 3D bars for every data point.
for i in np.arange(len(y_values)):
    ax.bar3d(i, np.arange(len(x_values)), dz, dx, dy, data[:, i], color=np.random.rand(3,), alpha=0.7)

#Set y ticks
ax.set_yticks(np.arange(len(x_values)) + dy/2)
ax.set_yticklabels(x_values)

#Set x ticks
ax.set_xticks(np.arange(len(y_values)))
ax.set_xticklabels(y_values, rotation=30, ha='right')

#Set other properties for better readable
ax.set_title('Student and Faculty Numbers in Social Sciences and Humanities Departments')
ax.view_init(azim=-50, elev=20)   # use a good viewing angle
ax.grid(True)

# to make tight layout and save
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/233_202312310050.png', format='png', dpi=100)
plt.clf()  # clear figure
