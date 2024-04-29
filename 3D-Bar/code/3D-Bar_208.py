
import numpy as np
import matplotlib.pyplot as plt

y_values = ['Funds Raised (Million $)', 'Number of Donations', 'Number of Volunteers']
data = np.array([[20000, 40000, 50000], [100000, 20000, 50000], [80000, 50000, 45000], [50000, 30000, 40000]])
x_values = ['Red Cross', 'Habitat for Humanity', 'United Way', 'WWF']

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 1, 1, data[:, i], shade=True, alpha=0.5)

ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values)

ax.set_xlabel('Organization')
ax.set_title('Charitable Contributions and Volunteerism - An Overview')

ax.grid(True)

plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/15_202312251044.png")

plt.cla()