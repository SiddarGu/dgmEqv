
import matplotlib.pyplot as plt
import numpy as np

y_values = ["CO2 Emission (Million Tonnes)","Renewable Energy Production (Million kWh)","Water Usage (Million Cubic Meters)"]
data = np.array([[6200,6700,2000],[1020,4500,1500],[9400,3200,1800],[3100,1800,1000],[520,2300,1200]])
x_values = ["USA","Japan","China","India","UK"]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i in range(len(y_values)):
    x = np.arange(len(x_values))
    y = [i] * len(x_values)
    ax.bar3d(x, y, np.zeros(len(x_values)), 0.2, 0.4, data[:,i], color='b', alpha=0.5)

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values)
ax.set_yticklabels(y_values)
ax.set_title('Environmental Sustainability Status of Major Countries')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/30_202312251036.png')
plt.clf()