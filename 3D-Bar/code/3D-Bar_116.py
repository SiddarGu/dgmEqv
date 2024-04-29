import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Data processing
data="""
Category,Psychology Publications,Anthropology Publications,Philosophy Publications,Sociology Publications
 2018,250,200,150,300
 2019,260,210,160,310
 2020,275,225,170,350
 2021,300,240,180,400
 2022,350,280,220,450 
"""
lines = data.strip().split('\n')
y_values = np.array(lines[0].split(',')[1:])
x_values = np.array([l.split(',')[0].strip() for l in lines[1:]])

temp_data = [l.split(',')[1:] for l in lines[1:]]
data = np.float32(temp_data)

# Set up the figure and axis
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

color_list = ['b', 'r', 'g', 'y']
for i, y_val in enumerate(y_values):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 
             0.4, 0.4, data[:, i], color=color_list[i], alpha=0.7)

ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation='vertical')
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, ha='left')
ax.set_title('Trends in Humanities and Social Sciences Publications 2018-2022')

for tick in ax.get_yticklabels():
    tick.set_rotation('vertical')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/276_202312310050.png')
plt.cla()   
plt.close(fig)  
