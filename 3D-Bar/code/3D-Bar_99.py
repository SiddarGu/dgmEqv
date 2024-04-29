import numpy as np
import matplotlib.pyplot as plt

# Data Preparation
raw_data = "Facebook,2450,85,250/n Instagram,1200,70,200/n Twitter,330,20,70/n LinkedIn,310,30,80/n Pinterest,450,15,75"
raw_data = raw_data.split("/n")

y_values = ["Active Users (Millions)", "New Users (Millions)", "Inactive Users (Millions)"]
x_values = []
data = []

for row in raw_data:
    items = row.split(",")
    x_values.append(items[0])
    data.append([np.float32(n) for n in items[1:]])

data = np.array(data)

# Plotting
fig = plt.figure(figsize=(12, 7))
ax = fig.add_subplot(111, projection='3d')

_color_list = ['r', 'g', 'b']
_x = np.arange(data.shape[0])
_y = np.arange(data.shape[1])

for c, z in zip(_color_list, _y):
    xs = _x
    ys = data[:, z]
    ax.bar(xs, ys, z, zdir='y', color=c, alpha=0.8)

# Setting labels
ax.set_xticks(_x)
ax.set_yticks(_y)
ax.set_xticklabels(x_values, rotation='vertical')
ax.set_yticklabels(y_values, ha='left')

# Setting title and labels
ax.set_title("Social Media Platform - Users' Status Analysis")
ax.set_xlabel("Social Media Platform")
ax.set_ylabel("Metrics")
ax.set_zlabel("Number in Millions")

# Adjust view angle for better visualization
ax.view_init(elev=25, azim=-60)    

# Save the figure
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/56_202312302126.png")

# Clean current figure
plt.clf()
