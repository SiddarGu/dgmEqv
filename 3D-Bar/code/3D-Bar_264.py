import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Provide numpy array data
given_data_matrix = np.array([
[350, 650, 1000],
[600, 400, 1000],
[700, 300, 1000],
[750, 250, 1000],
[800, 200, 1000]
], dtype=np.float32)

x_values = ['2019', '2020', '2021', '2022', '2023']
y_values = ['Online Sales ($Bn)', 'In-Store Sales ($Bn)', 'Total Sales ($Bn)']

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

colors = ['red', 'green', 'blue']
xticks = np.arange(len(x_values))
yticks = np.arange(len(y_values))

# Create the 3D bar chart
for c, j in zip(colors, range(len(y_values))):
    for i, xi in enumerate(x_values):
        ax.bar3d(i, j, 0, 0.9, 0.9, given_data_matrix[i][j], color=c)
        
ax.set_xticks(xticks)
ax.set_xticklabels(x_values, rotation=45, ha='right')
ax.set_yticks(yticks)
ax.set_yticklabels(y_values, ha='left')
        
ax.set_title("Retail and E-commerce Sales Trend from 2019 to 2023")
ax.view_init(30, 15)

plt.tight_layout()
plt.grid(True)

# Save the generated plot
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/70_202312302126.png')

# Clear the current figure's content
plt.clf()
