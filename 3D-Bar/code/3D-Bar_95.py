import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Transform data to variables
y_values = ['Grants Received (Million $)', 'Graduates (Thousands)', 'Academic Positions (Hundreds)']
x_values = ['Sociology', 'Philosophy', 'Anthropology', 'Psychology', 'Literature']
data = np.array([[12., 30., 5.],
                 [7., 20., 4.],
                 [9., 25., 3.8],
                 [14., 45., 6.],
                 [8., 18., 3.1]])

# Create 3D bar chart
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 0.4, 0.6, data[:, i], color='b', alpha=0.1*i+0.1)

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
plt.xticks(rotation=45)
ax.set_xticklabels(x_values)
ax.set_yticklabels(y_values, ha='left')
ax.set_title('Funding, Graduation and Academic Position Analysis across Humanities Fields')

plt.grid(True)
ax.view_init(30, -60)
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/216_202312302235.png", dpi=300)
plt.close()
