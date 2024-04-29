
import numpy as np
import matplotlib.pyplot as plt

# transform data into three variables
y_values = ['Number of Cases (in Thousands)', 'Average Resolution Time (Days)', 'Number of Lawyers Involved']
x_values = ['Civil', 'Criminal', 'Tax', 'Human Rights', 'International']
data = np.array([[200, 60, 150], [120, 90, 220], [150, 45, 100], [180, 70, 120], [110, 80, 170]])

# create figure before plotting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(1, 1, 1, projection='3d')

# iterate over y_values
for i, y in enumerate(y_values):
    # plot data
    x = np.arange(len(x_values))
    y_ = [i]*len(x_values)
    ax.bar3d(x, y_, np.zeros(len(x_values)), 0.8, 0.4, data[:, i], alpha=0.5, color='b')

# customize axis
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=45, fontsize=10, ha='right')
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, fontsize=10, ha='left')

# set title
ax.set_title('Law and Legal Affairs - Cases Overview', fontsize=16)

# draw background grids
plt.grid(True)

# resize the image
plt.tight_layout()

# savefig
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/1_202312251036.png')

# clear the current image state
plt.cla()