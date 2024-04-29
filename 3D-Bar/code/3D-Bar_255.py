
import numpy as np
import matplotlib.pyplot as plt

y_values = ['Average Daily Usage (Hours)', 'Number of Users (Millions)','Average Monthly Active Users (Millions)']
data = np.array([[4.4,2.7,2.2],
                   [1.3,0.2,0.18],
                   [1.7,1.0,0.9],
                   [1.6,1.5,1.4]])
x_values = ['Facebook','Twitter','Instagram','YouTube']

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    if i == 0:
        ax.bar3d(xs, ys, [0]*len(x_values), 0.4, 0.4, data[:,i], color='#00BFFF')
    elif i == 1:
        ax.bar3d(xs, ys, [0]*len(x_values), 0.4, 0.4, data[:,i], color='#FF4500')
    else:
        ax.bar3d(xs, ys, [0]*len(x_values), 0.4, 0.4, data[:,i], color='#20B2AA')

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=30)
ax.set_yticklabels(y_values)

ax.set_title('Social Media Usage Statistics - Average Daily Usage & User Numbers')

fig.tight_layout()
fig.set_figwidth(10)
fig.set_figheight(6)

fig.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/36_202312251044.png')

plt.clf()