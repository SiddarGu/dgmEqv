import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 

# Data preparation
data_str = 'Quarter,Total Sales ($ Billion),Online Sales ($ Billion),Store-Based Sales ($ Billion)\n Q1,20,12,22\n Q2,25,14,28\n Q3,26,15,29\n Q4,30,16,33'
lines = data_str.split("\n")
headers = lines[0].split(",")
rows = [line.split(",") for line in lines[1:]]
y_values = headers[1:]
x_values = [row[0] for row in rows]
data = np.array([[np.float32(val) for val in row[1:]] for row in rows])

# Create figure
fig = plt.figure(figsize=(10, 8))

# 3D subplot
ax = fig.add_subplot(111, projection='3d') 

# Plotting
width = depth = 0.3
for i in range(data.shape[1]):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)),
             width, depth, data[:, i])

ax.set_title('Quarter-Wise Sales Analysis in Retail and E-commerce Sector')
ax.set_xlabel('Quarter')
ax.set_zlabel('Sales ($ Billion)')
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45, ha='right')
ax.set_yticklabels(y_values, ha='left')

plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/108_202312302126.png', dpi=300)

# Clear the current image state
plt.close()
