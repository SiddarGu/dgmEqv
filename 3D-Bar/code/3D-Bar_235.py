

import numpy as np
import matplotlib.pyplot as plt

y_values = ['Total Number of Homes', 'Average Price ($000)', 'Average Price Per Square Foot ($)'] 
x_values = ['North', 'South', 'East', 'West']
data = np.array([[100,400,200], [150,350,225], [125,450,300], [175,500,250]])

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i]*len(x_values)
    ax.bar3d(xs, ys, np.zeros(len(xs)), 0.5, 0.5, data[:,i], 
             color=plt.cm.jet(i/len(y_values)), alpha=0.5)

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=20)
ax.set_yticklabels(y_values)
ax.set_title('Real Estate Market Analysis by Region')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/14_202312251036.png')
plt.clf()