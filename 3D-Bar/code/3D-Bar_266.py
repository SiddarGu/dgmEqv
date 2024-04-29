import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load data
table = """Region,Defense Spending ($B),Healthcare Spending ($B),Education Spending ($B)
    East,55,70,85
    West,60,80,100
    North,50,65,80
    South,58,75,90"""
lines = table.split("\n")
y_values = lines[0].split(",")[1:]
x_values = [line.split(",")[0].strip() for line in lines[1:]]
data = np.array([list(map(np.float32, line.split(",")[1:])) for line in lines[1:]])

# Create figure and add 3D subplot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot each category
for i in range(data.shape[1]):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 
             0.4, 0.5, data[:, i], color=plt.cm.viridis(i / data.shape[1]), alpha=0.6)

# Format plot
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45, ha='right')
ax.set_yticklabels(y_values, ha='left')
plt.title('Government Spending in Multiple Sectors by Region')
ax.view_init(elev=20., azim=-35)
ax.grid(True)

# Save and clear figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/121_202312302126.png')
plt.clf()
