import matplotlib.pyplot as plt
import numpy as np

# Data
y_values = ["Charity Donations (Million USD)", "Volunteer Hours (Million Hours)", "Fundraising Events (Number of Events)"]
data = np.array([[1.2,1.5,4], [2.4,2.3,3], [1.9,2.1,3], [2.1,2.7,4]])
x_values = ["North", "South", "East", "West"]

# Plot
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

xpos = np.arange(data.shape[0])
ypos = np.arange(data.shape[1])
xpos, ypos = np.meshgrid(xpos, ypos)
xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros(data.flatten().shape)

dx = dy = 0.5
dz = data.flatten()

colors = plt.cm.viridis(dz / np.max(dz))

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=colors)

ax.w_xaxis.set_ticklabels(x_values)
ax.w_yaxis.set_ticklabels(y_values)
ax.set_xlabel('Region')
ax.set_ylabel('Metrics')
ax.set_zlabel('Values')

plt.title('Charity and Nonprofit Organizations Analysis by Region')
plt.tight_layout()

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/29.png')
plt.clf()