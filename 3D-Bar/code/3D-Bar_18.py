
import matplotlib.pyplot as plt
import numpy as np

# transform the data into three variables
y_values = ['Number of Vaccines Administered (Millions)', 'Number of Check-Ups (Millions)', 'Number of Hospitalizations (Millions)']
x_values = ['2019', '2020', '2021', '2022', '2023']
data = np.array([[110, 120, 130], [120, 130, 125], [115, 125, 125], [125, 140, 140], [135, 155, 145]])

# create the figure
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111, projection='3d')

# plot the data
for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    ax.bar3d(xs, ys, [0] * len(x_values), 0.5, 0.5, data[:, i], shade=True, color='green', alpha=0.5)

# set the x-axis and y-axis labels
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, rotation=90, wrap=True)

# add grids
ax.grid(True)

# set the title
ax.set_title('Healthcare Trends - 2019 to 2023')

# automatically resize the image
plt.tight_layout()

# save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/18_202312251036.png')

# clear the current image state
plt.clf()