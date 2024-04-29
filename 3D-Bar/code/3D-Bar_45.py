
import numpy as np
import matplotlib.pyplot as plt

y_values = ['Sales Volume (Units)', 'Average Price ($)', 'Gross Revenue ($)']
data = np.array([[100,110,1000], [200,280,1600], [400,320,800], [500,515,750]])
x_values = ['Pizza', 'Burgers', 'Soft Drinks', 'Salads']

fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(1,1,1, projection='3d')

for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    ax.bar3d(xs, ys, [0]*len(x_values), 0.5, 0.5, data[:,i], color='#9966FF', alpha=1)

ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=20)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values)
ax.set_title("Food and Beverage Industry Analysis - Sales Volume, Price and Revenue")
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/17_202312251044.png', bbox_inches = "tight")
plt.clf()