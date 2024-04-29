
import matplotlib.pyplot as plt
import numpy as np

y_values = ["Trucking (million Tonnes)", "Shipping (million Tonnes)", "Air (million Tonnes)", "Rail (million Tonnes)"]
x_values = ["Road", "Sea", "Air", "Rail"]
data = np.array([[50,35,25,10], [45,60,20,15], [20,25,50,5], [15,30,20,40]])

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    ax.bar3d(xs, ys, np.zeros(len(x_values)), 1, 1, data[:,i], shade=True, color='#0099FF')

ax.w_xaxis.set_ticklabels(x_values)
ax.w_yaxis.set_ticklabels(y_values)
ax.set_title('Transportation and Logistics: A Look at Volume by Mode of Transport')
ax.set_xlabel('Mode of Transport')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/40_202312251044.png')
plt.clf()