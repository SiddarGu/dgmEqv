import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Data
data = '''Year,Number of Internet Users (Billions),Smartphone Penetration Rate (%),E-commerce Sales (Trillions USD),Global ICT Spending (Trillions USD)
2019,4.5,7.5,3.5,4 
2020,4.8,7.8,4,4.3 
2021,5.1,8.1,4.8,4.6 
2022,5.3,8.3,5.2,5.1 
2023,5.6,8.5,5.6,5.4'''

all_values = [i.split(',') for i in data.split('\n')]

y_values = all_values[0][1:]
x_values = [item[0] for item in all_values[1:]]
data_values = np.array([item[1:] for item in all_values[1:]], dtype=np.float32)

# Create a new figure
fig = plt.figure(figsize=(10, 10))

# Add a subplot with 3D projection
ax = fig.add_subplot(111, projection='3d')

# Plot each column of data
for j, y_value in enumerate(y_values):
    x, y = np.meshgrid(np.arange(data_values.shape[0]), [j])
    z = np.zeros(x.shape)
    dx = np.ones(x.shape) * 0.3
    dy = np.ones(x.shape) * 0.6
    dz = data_values[:,j]
    ax.bar3d(x.flatten(), y.flatten(), z.flatten(), dx.flatten(), dy.flatten(), dz, color=plt.cm.viridis(j / len(y_values)), alpha=0.7, zsort='average')

# Formatting
ax.xaxis.labelpad = 20
ax.yaxis.labelpad = 20
ax.set_zlabel('Value')
ax.set_title('Global Technology and Internet Trends - 2019 to 2023', pad=50)
ax.view_init(elev=30, azim=-35)

# Align label position with data position and label them
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
plt.xticks(rotation=90)
ax.w_xaxis.set_ticklabels(x_values)
ax.w_yaxis.set_ticklabels(y_values, ha='left')

# Auto resizing the figure and save it
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/93_202312302126.png', bbox_inches='tight')

# Clear the current figure
plt.clf()
