# import necessary library
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Provided data
data_str = 'Quarter,Revenue ($M),Net Profit ($M),Total Assets ($M),Total Liabilities ($M)/n Q1-2021,1250,180,3900,2675/n Q2-2021,1450,200,4100,2900/n Q3-2021,1690,240,4320,2980/n Q4-2021,1750,270,4450,3050/n Q1-2022,1890,290,4700,3200'

# Transforming data to suitable format
data_list = [i.split(',') for i in data_str.split('/n ')]
x_values = [i[0] for i in data_list[1:]]
y_values = data_list[0][1:]
data = np.float32([i[1:] for i in data_list[1:]])

fig = plt.figure(figsize=(10, 7)) #make sure figsize is suitable.
ax = fig.add_subplot(111, projection='3d')

colors = ['r', 'g', 'b', 'm'] # list of colors for different bars 
width = depth = 0.5 # width and depth of bars
d_color = 0.5/len(y_values) # to vary the color of bars

for c in range(len(y_values)):
    x_t = np.arange(len(x_values))
    y_t = np.full(len(x_values), c)
    ax.bar3d(x_t, y_t, np.zeros(len(x_values)), width, depth, data[:, c], color=(colors[c % len(colors)]), shade=True, alpha=0.5)

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45, horizontalalignment='right')
ax.set_yticklabels(y_values, ha='left')

ax.set_zlabel('Values ($M)') # z-label
ax.set_title('Financial Performance Quarterly Analysis 2021-2022') # Set title

# Adjusting viewing angles for better visualization
ax.view_init(elev=20, azim=-35)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/142_202312302235.png', dpi=300)
plt.clf() # Clear the current image state
