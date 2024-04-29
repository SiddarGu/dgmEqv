
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
y_values = ['Sales Volume (Units)', 'Average Price ($)', 'Number of Listings']
x_values = ['Fast Food', 'Bakery', 'Beverages', 'Groceries'] 
data = np.array([[200, 50, 300], [150, 70, 400], [500, 25, 500], [400, 40, 400]])

for i in range(len(y_values)):
    ys = [i] * len(x_values)
    ax.bar3d(np.arange(len(x_values)), ys, [0] * len(x_values), 0.5, 0.5, data[:, i], alpha=0.3 * (i+1))

ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, ha='left')
ax.set_title('Comprehensive Overview of the Food and Beverage Industry Market')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/2_202312251044.png')
plt.clf()