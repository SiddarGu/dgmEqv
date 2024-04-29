import matplotlib.pyplot as plt
import numpy as np

raw_data = "Department,Number of Undergraduate Students,Number of Postgraduate Students,Number of Research Projects/n Computer Science,650,300,55/n Civil Engineering,400,200,35/n Mechanical Engineering,700,300,70/n Electrical Engineering,500,180,40/n Bioengineering,450,250,60"
raw_lines = raw_data.split('/n')

labels = raw_lines[0].split(',')
y_values = labels[1:]
raw_values = [line.split(',') for line in raw_lines[1:]]
x_values = [values[0] for values in raw_values]
data = np.array([list(map(int, values[1:])) for values in raw_values])

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

colors = ['r', 'g', 'b']
xticks = np.arange(len(x_values))

for c, k in zip(colors, range(len(y_values))):
    ax.bar3d(xticks, np.array([k]*len(x_values)), np.zeros(len(x_values)), np.ones(len(x_values)), np.ones(len(x_values)), data[:, k], color=c, alpha=0.5)

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45, va='baseline', wrap=True)
ax.set_yticklabels(y_values, ha='left')
ax.view_init(elev=25, azim=165)
ax.grid(True)
plt.title('Student and Research Project Distribution in Science and Engineering Departments')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/243_202312310050.png', format='png')
plt.clf()
