
import numpy as np
import matplotlib.pyplot as plt

y_values = ["Average GPA", "Average SAT Score", "Number of Students"]
x_values = ["Elementary", "Middle", "High School", "College"]
data = np.array([[370, 1100, 500], [390, 1200, 1000], [380, 1300, 2000], [360, 1400, 3000]])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    ax.bar3d(xs, ys, np.zeros(len(x_values)), 0.5, 0.5, data[:, i], shade=True, color='r')

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticklabels(y_values)
fig.suptitle("Academic Performance of Students - Elementary to College Level")

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/4_202312251036.png')
plt.clf()