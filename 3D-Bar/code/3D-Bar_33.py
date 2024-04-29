
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection='3d')

y_values = ["Computer Science Students (Thousands)", "Engineering Students (Thousands)", "Physics Students (Thousands)", "Chemistry Students (Thousands)"]
data = np.array([[20, 50, 30, 40], [25, 52, 33, 45], [30, 55, 37, 50], [35, 58, 40, 55], [40, 60, 45, 60]])
x_values = ["2019", "2020", "2021", "2022", "2023"]

for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    ax.bar3d(xs, ys, np.zeros(len(x_values)), 1, 1, data[:, i], color='#0099FF', alpha=0.2 * (i + 1))
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, ha='left', rotation=-15)
ax.set_title("Science and Engineering Student Enrollment Trends - 2019 to 2023")
fig.tight_layout()
fig.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/2_202312251036.png')
plt.clf()