import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Input data
raw_data = 'Event,Attendance (Millions),Ticket Sales ($ Millions),Merchandise Sales ($ Millions)\n Super Bowl,0.1,5,2\n World Cup,3.43,1.6,5\n Olympics,5,3.5,1\n WrestleMania,0.08,1.7,0.9\n Formula 1,3,1.2,0.4'

# Transform raw data into list of strings
data_strings = raw_data.split('\n')
data_set = [item.split(',') for item in data_strings]

# Split labels and data
x_values = [item[0] for item in data_set[1:]]
y_values = data_set[0][1:]
data = np.array([list(map(float, item[1:])) for item in data_set[1:]])

fig = plt.figure(figsize=(10, 6)) 
ax = fig.add_subplot(111, projection='3d') 

colors = ['r', 'g', 'b']

for c, k in zip(colors, range(data.shape[1])):
    xs = np.arange(len(x_values)) 
    ys = [k]*len(x_values)
    zs = np.zeros(len(x_values))
    dx = np.ones(len(x_values)) * 0.3
    dy = np.ones(len(x_values)) * 0.4
    dz = data[:, k]
    ax.bar3d(xs, ys, zs, dx, dy, dz, color=c, alpha=0.7)

ax.set_xlabel('Events') 
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, ha='left')
ax.set_xticks(np.arange(len(x_values))) 
ax.set_xticklabels(x_values, rotation=45, horizontalalignment='right')

ax.set_title('Sports and Entertainment Events - Attendance and Revenue Analysis') 

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/107_202312302126.png', format='png', dpi=300)
plt.clf()
