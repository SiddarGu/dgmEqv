import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Given data
data = """Country,Number of Tourists (Millions),Average Expenditure Per Tourist ($),Total Revenue from Tourism ($Billion)
USA,79.6,2000,159.2
Spain,82.7,1300,107.51
France,89.4,1700,151.98
China,62.9,1600,100.64
Italy,61.6,1500,92.4"""

# Processing data
data = data.split("\n")
x_values = [row.split(",")[0] for row in data[1:]]
y_values = data[0].split(",")[1:]
data = [list(map(np.float32, row.split(",")[1:])) for row in data[1:]]

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

_x = np.arange(len(x_values))
_y = np.arange(len(y_values))

for i in _y:
    X, Y = np.meshgrid(_x, _y[i])
    Z = np.array([data[j][i] for j in range(len(data))])
    ax.bar3d(X.flatten(), Y.flatten(), np.zeros(len(Z.flatten())), dx=0.5, dy=0.5, dz=Z.flatten(), color='aqua', alpha=0.5)
    
ax.set_xticks(_x + 0.25)
ax.set_yticks(_y + 0.4)
ax.set_xticklabels(x_values, rotation='vertical')
ax.set_yticklabels(y_values, ha='left')
plt.title('Tourism Statistics and Revenue Analysis – International Perspective')
plt.tight_layout()

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/55_202312302126.png')

plt.close()
