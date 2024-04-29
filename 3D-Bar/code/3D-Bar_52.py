import numpy as np
import matplotlib.pyplot as plt

# Data
x_values = ['2020', '2021', '2022', '2023', '2024']
y_values = ['Tea Production (Kgs)', 'Coffee Production (Kgs)', 'Beer Output (Litres)', 'Wine Production (Litres)']
data = np.array([[700, 750, 500, 150],
                [730, 780, 520, 155],
                [760, 810, 540, 160],
                [800, 850, 570, 170],
                [830, 900, 600, 180]], dtype=np.float32)

# Create a new figure 
fig = plt.figure(figsize=(10, 8))

# Create a 3D subplot
ax = fig.add_subplot(111, projection='3d')

xpos, ypos = np.meshgrid(np.arange(data.shape[1]), np.arange(data.shape[0]))
xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros_like(xpos)
dx = dy = 0.8
dz = data.flatten()

# Create color array
color = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'] * len(x_values)

# Plot
for i in range(len(y_values)):
  ax.bar3d(xpos[i*len(x_values):(i+1)*len(x_values)], ypos[i*len(x_values):(i+1)*len(x_values)], zpos[i*len(x_values):(i+1)*len(x_values)],
           dx, dy, dz[i*len(x_values):(i+1)*len(x_values)], color=color[i*len(x_values):(i+1)*len(x_values)], alpha=0.7)

# Labels
ax.axes.set_xticks(np.arange(len(x_values)))
ax.axes.set_yticks(np.arange(len(y_values)))
ax.axes.set_xticklabels(x_values, rotation=45, ha="right")
ax.axes.set_yticklabels(y_values, ha='left')
ax.view_init(30, 30)
ax.set_title("Food and Beverage Industry: Production Trends 2020-2024")

plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/89_202312302126.png")
plt.show()
plt.close(fig)
