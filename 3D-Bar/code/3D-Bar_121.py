import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Transform data into variables
data = """2019,10,15,20,25
2020,11,16,22,28
2021,12,19,23,33
2022,14,21,26,36
2023,16,24,28,39"""
lines = data.split("\n")
x_values = [line.split(",")[0] for line in lines]
y_values = ['Car Production', 'Electronics Production', 'Furniture Production', 'Machinery Production']
data = np.array([list(map(np.float32, line.split(",")[1:])) for line in lines])

# Create figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot each column of data
for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 0.4, 0.8, data[:, i], alpha=0.5)

# Set labels and ticks
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values))+0.4)
ax.set_xticklabels(x_values, rotation=45, horizontalalignment='right')
ax.set_yticklabels(y_values, ha='left')

# Set title and labels
ax.set_title('Manufacturing and Production Statistics - 2019 to 2023')
ax.set_xlabel('Year')
ax.set_zlabel('Production (Million Units)')

# Adjust view
ax.view_init(elev=20., azim=-35)

# Increase layout and save figure
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/268_202312310050.png", format='png')

# Clear current figure
plt.clf()
