
import numpy as np
import matplotlib.pyplot as plt

# Data preparation
data = np.array([[3.4, 1.2, 0.5], [1.6, 0.7, 0.4], [0.9, 0.3, 0.2], [1.2, 0.5, 0.2]])
y_values = ["Viewers (Millions)", "Revenue (Millions $)", "Sponsorship (Millions $)"]
x_values = ["Football", "Basketball", "Volleyball", "Hockey"]

# Plotting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

xpos = np.arange(len(x_values))
width = 0.2

for i in range(len(y_values)):
    zpos = [0]*len(x_values)
    ypos = i
    dy = width
    dx = 0.5
    dz = data[:, i]
    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=['#ff9999', '#aaff99', '#99ccff'][i])

ax.set_xticks(xpos + width/2)
ax.set_xticklabels(x_values)
ax.set_yticks([0, 1, 2])
ax.set_yticklabels(y_values)
ax.set_ylabel('Metrics')
ax.set_title('Sports and Entertainment Market Performance - Viewers, Revenue and Sponsorship')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/33.png')
plt.clf()