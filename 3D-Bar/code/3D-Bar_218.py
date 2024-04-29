
import numpy as np
import matplotlib.pyplot as plt

# Define the data
y_values = ['Dairy Production (Million Tonnes)', 'Fruit Production (Million Tonnes)',
            'Vegetable Production (Million Tonnes)', 'Fish Production (Million Tonnes)']
x_values = ['2019', '2020', '2021', '2022', '2023']
data = np.array([[10, 25, 30, 15],
                 [9.5, 26.5, 32.5, 17],
                 [11, 27.8, 34.2, 18.3],
                 [10.7, 29.2, 35.9, 19.5],
                 [11.5, 30.5, 37.6, 20.7]])

# Create the figure
fig = plt.figure(figsize=(12, 8))
ax = plt.axes(projection='3d')
ax.set_title('Food Production Trends - 2019 to 2023', fontsize=20)

# Plot each column of data
for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    ax.bar3d(xs, ys, np.zeros(len(x_values)), 0.5, 0.5, data[:, i],
             shade=True, color='b', alpha=0.2 * (i + 1))

# Label the axes
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, fontsize=12, rotation=90)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, fontsize=12, ha='left')

# Create grids
ax.grid(False)
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/3_202312251036.png')
plt.clf()