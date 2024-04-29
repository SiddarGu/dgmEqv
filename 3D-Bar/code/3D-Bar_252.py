
import numpy as np
import matplotlib.pyplot as plt

y_values = ['Average Price ($000)', 'Sales Volume (Units)', 'Number of Listings']
data = np.array([[250, 500, 700], 
                 [300, 600, 800], 
                 [200, 450, 650], 
                 [275, 550, 750]])
x_values = ['North', 'South', 'East', 'West']

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    ax.bar3d(xs, ys, np.zeros(len(x_values)), 1, 1, data[:,i], alpha=0.8,
             color=['b']*len(x_values), edgecolor='k')

ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, ha='left', rotation=-15)
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_ylim(bottom=0, top=len(y_values))
ax.set_title('Real Estate Market Analysis by Region')

fig.tight_layout()
fig.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/2.png')
plt.clf()