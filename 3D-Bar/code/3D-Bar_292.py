
import numpy as np
import matplotlib.pyplot as plt

# transform the data into three variables
y_values = ["Average Home Size (sqft)", "Average Price ($000)", "Number of Listings"]
data = np.array([[2000, 600, 700], [1800, 500, 800], [1900, 480, 650], [1750, 660, 750]])
x_values = ["North", "South", "East", "West"]

# plot the data with 3D bar chart
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection='3d')

for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    ax.bar3d(xs, ys, np.zeros(len(x_values)), 1, 1, data[:,i], shade=True, color='#0073e6')

# adjust the dimension of the bars
ax.set_xlabel('Region', fontsize=14)
ax.set_ylabel('Metrics', fontsize=14)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, ha='left', rotation=-15)
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=45)

# draw background grids
ax.zaxis.set_major_locator(plt.LinearLocator(5))
ax.view_init(30, -15)

# set the title
ax.set_title('Real Estate Market Trends - Average Home Size and Prices by Region')

# resize the image
plt.tight_layout()

# save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/26_202312251044.png')

# clear the current image state
plt.clf()