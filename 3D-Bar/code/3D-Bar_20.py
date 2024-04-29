
import matplotlib.pyplot as plt
import numpy as np

y_values = ['Viewership (Million)', 'Events', 'Revenue ($ Billion)']
data = np.array([[200, 400, 400], [400, 600, 700], [250, 300, 550], [500, 650, 900], [350, 450, 650]])
x_values = ['Outdoor Sports', 'Indoor Sports', 'Music Concerts', 'TV Shows', 'Movies']

fig = plt.figure(figsize=(9, 6))
ax = fig.add_subplot(111, projection='3d')

for i in range(len(y_values)):
    ys = [i] * len(x_values)
    xs = np.arange(len(x_values))
    ax.bar3d(xs, ys, np.zeros(len(x_values)), 0.7, 0.7, data[:, i], alpha=0.4, color='green', linewidth=0)

ax.set_xticks(xs)
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, ha='left')
ax.set_title('Sports and Entertainment Industry Growth - Viewership, Events and Revenue')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/23_202312251044.png')
plt.clf()