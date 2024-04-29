
import matplotlib.pyplot as plt
import numpy as np

y_values = ['Math Scores', 'Reading Scores', 'Science Scores']
data = np.array([[90,85,87], [89,84,86], [87,83,85], [86,82,84], [85,81,83]])
x_values = ['Grade 3', 'Grade 4', 'Grade 5', 'Grade 6', 'Grade 7']

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    ax.bar3d(xs, ys, [70]*len(x_values), 1, 1, data[:,i] - 70, alpha=0.6, color=['darkblue', 'darkorange', 'darkgreen'][i])

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticklabels(y_values)
ax.set_zlim(70, 90)
ax.set_title('Academic Performance by Grade Level in Math, Reading, and Science')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/20_202312251044.png')
plt.clf()