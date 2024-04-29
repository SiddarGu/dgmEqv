
import matplotlib.pyplot as plt
import numpy as np

y_values = ["Energy Consumption (KWh)", "Average Utility Bill ($)", "Number of Customers"]
data = np.array([[200, 100, 500],
                  [220, 105, 550],
                  [180, 90, 450],
                  [210, 95, 520]])
x_values = ["North", "South", "East", "West"]

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection='3d')

xpos = np.arange(len(x_values))
ypos = np.arange(len(y_values))
xposM, yposM = np.meshgrid(xpos, ypos, copy=False)

for i in range(len(y_values)):
    xpos = xposM[i]
    ypos = yposM[i]
    zpos = np.zeros(len(x_values))
    dx = 0.5
    dy = 0.5
    dz = data[:,i]
    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='#00ceaa', alpha=0.8)
    ax.w_xaxis.set_ticklabels(x_values, rotation=30)

ax.set_title("Energy Usage and Billing Trends Across Regions")
ax.set_ylabel("Metrics")
ax.set_xlabel("Regions")
ax.set_xticks(xpos + .5/2.)
ax.set_yticks(ypos + .5/2.)
ax.set_zlabel('Values')
ax.tick_params(axis='both', which='major', labelsize=12)
ax.grid(linestyle='-', linewidth='0.5', color='black')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/36.png')
plt.clf()