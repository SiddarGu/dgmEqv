import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Seperate the values
raw = [("Computer Science",1100,1000,150),("Electrical Engineering",900,870,125),("Mechanical Engineering",950,930,130),("Civil Engineering",850,800,120),("Chemical Engineering",700,670,115)]
y_values = ["Number of New Students", "Number of Graduates", "Research Funding ($m)"]
x_values = [x[0] for x in raw]
data = np.array([x[1:] for x in raw], dtype=np.float32)

# Create a figure for the plot
fig = plt.figure(figsize=(12,10))
ax = fig.add_subplot(111, projection='3d')

# Set bar dimensions and colors
bar_width = 0.25
bar_depth = 0.5
colors = ['b', 'r', 'g']

# Iteratively add bars to the plot
for i in range(len(y_values)):
    xpos = np.arange(len(x_values))
    ypos = [i]*len(x_values)
    zpos = np.zeros(len(x_values))
    dx = [bar_width]*len(x_values)
    dy = [bar_depth]*len(x_values)
    dz = data[:, i]
    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=colors[i], alpha=0.5)

# Set x and y ticks and labels
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=45, horizontalalignment='right')
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, ha='left')

# Set figure title
ax.set_title('Science and Engineering Department Overview')

# Adjust the view angle for better visualization
ax.view_init(elev=25, azim=-35)

# Save the image before clearing the state
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/214_202312302235.png')
plt.clf()
