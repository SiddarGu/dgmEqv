
import matplotlib.pyplot as plt
import numpy as np

# transform the given data into three variables
y_values = ['Automobile Production (Units)', 'Aircraft Production (Units)', 'Shipbuilding Production (Units)', 'Computer Production (Units)']
data = np.array([[500, 180, 450, 150], [600, 200, 500, 160], [650, 220, 550, 170], [700, 240, 600, 180], [750, 260, 650, 190]])
x_values = ['2019', '2020', '2021', '2022', '2023']

# create figure and set title
fig = plt.figure(figsize= (14, 10))
ax = fig.add_subplot(1, 1, 1, projection='3d')
ax.set_title('Production Output of Automobiles, Aircrafts, Ships, and Computers - 2019 to 2023')

# plot data with 3d bar chart
for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    ax.bar3d(xs, ys, [0]*len(x_values), 0.5, 0.5, data[:, i], shade=True, color='b')

# label x and y axes and rotate x-axis labels
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=12)
ax.set_yticklabels(y_values)
ax.view_init(30, -15)

# set background grids
ax.grid(alpha=0.2)

# resize image and save
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/40_202312270030.png')

# clear current image state
plt.clf()