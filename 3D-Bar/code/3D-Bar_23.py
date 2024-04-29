
import numpy as np
import matplotlib.pyplot as plt

# transform the given data into three variables: y_values, data, x_values
y_values = ['Quantity Sold (Units)', 'Gross Revenue ($)', 'Average Price ($)']
data = np.array([[10000, 20000, 20200], [7500, 15000, 20000], [6500, 13000, 20400], [9000, 18000, 25000]])
x_values = ['Beverages', 'Dairy', 'Fruits', 'Vegetables']

# create figure
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# plot data
for i in range(len(y_values)):
    xpos = np.arange(len(x_values))
    ypos = [i] * len(x_values)
    dx = 0.5
    dy = 0.5
    dz = data[:, i]

    if i == 0:
        ax.bar3d(xpos, ypos, np.zeros(len(x_values)), dx, dy, dz, color='#ff8100', alpha=1, edgecolor='black')
    elif i == 1:
        ax.bar3d(xpos, ypos, np.zeros(len(x_values)), dx, dy, dz, color='#3d9bff', alpha=1, edgecolor='black')
    elif i == 2:
        ax.bar3d(xpos, ypos, np.zeros(len(x_values)), dx, dy, dz, color='#4cd137', alpha=1, edgecolor='black')

# set labels
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=20)
ax.set_yticklabels(y_values)
ax.set_title('Food and Beverage Industry Sales Analysis')
plt.tight_layout()

# save figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/5_202312251036.png')

# clear current image state
plt.cla()