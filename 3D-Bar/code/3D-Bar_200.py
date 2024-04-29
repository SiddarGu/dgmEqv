
import numpy as np
import matplotlib.pyplot as plt

y_values = ['Charitable Donations (USD)', 'Number of Volunteers', 'Number of Non-profit Organizations']
data = np.array([[5000, 10000, 3000], [3000, 12000, 2000], [4000, 15000, 4000], [2500, 8000, 2500], [3500, 9000, 3500]])
x_values = ['California', 'Texas', 'New York', 'Florida', 'Illinois']

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    ax.bar3d(xs, ys, [0]*len(x_values), 0.2, 0.4, data[:,i], alpha=0.3, color=plt.cm.viridis(i/len(y_values)))

ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=30, wrap=True)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values)
plt.title('Charitable Giving Trends Across the US')

fig.tight_layout()
fig.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/33_202312270030.png')
plt.clf()