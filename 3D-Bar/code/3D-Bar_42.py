
import numpy as np
import matplotlib.pyplot as plt

y_values = ['Sales Volume (Units)', 'Average Price ($000)', 'Number of Listings']
data = np.array([[500, 250, 700],
                 [600, 300, 800],
                 [450, 200, 650],
                 [550, 275, 750]])
x_values = ['North', 'South', 'East', 'West']

fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot(111, projection='3d')

for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    ax.bar3d(xs, ys, np.zeros(len(x_values)), 0.5, 0.5, data[:, i], shade=True)

ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values)
ax.set_title('Real Estate Market Analysis by Region')
ax.tick_params(labelsize=8)
ax.view_init(elev=25, azim=-25)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/12.png')
plt.clf()