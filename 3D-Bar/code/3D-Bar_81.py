import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Transforming data into the required format
raw_data = 'Platform,Monthly active users (Billion),Daily active users (Billion),Revenue last quarter ($ Billion)\n Facebook,2.8,1.84,29.08\n Instagram,1,0.5,20.68\n Twitter,0.33,0.187,1.29\n YouTube,2,0.3,6.01\n TikTok,0.69,0.365,7.4'
lines = raw_data.split("\n")
header = lines[0].split(",")
lines = lines[1:]
x_values = [line.split(",")[0].strip() for line in lines]
y_values = header[1:]
data = np.array([[np.float32(val) for val in line.split(",")[1:]] for line in lines])

# defining bar width and depth
width = 0.2
depth = 0.2

# creating 3D subplot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# iterating and plotting each column
colors = ['r', 'g', 'b']
for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), width, depth, data[:,i], color=colors[i], alpha=0.7)

# adding labels
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=30, horizontalalignment='right')
ax.set_yticklabels(y_values, ha='left')

# adding title
plt.title('Social Media Platforms - User engagement and Revenue analysis')

#saving figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/254_202312310050.png')

plt.show()

#clearing the current figure
plt.clf()
