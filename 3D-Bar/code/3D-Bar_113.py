import numpy as np
import matplotlib.pyplot as plt

x_values = ['New York', 'Los Angeles', 'Chicago', 'Boston', 'Miami']

y_values = ['Average Rental Price ($)', 
            'Median Home Price ($000)', 
            'Number of New Homes Built']

data = np.array([[2800, 700, 5000],
                 [2500, 800, 4000],
                 [2000, 600, 3000],
                 [2300, 650, 4500],
                 [2100, 550, 3500]], np.float32)

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

_x = np.arange(len(x_values))
_y = np.arange(len(y_values))

for i, y_value in enumerate(y_values):
    ax.bar3d(_x, [i]*len(x_values), np.zeros(len(x_values)), 
             0.5, 0.5, data[:, i], color=np.random.rand(3,), alpha=0.8)

plt.title('Comparative Analysis of Real Estate and Housing Market in Major U.S Cities')

ax.set_xticks(_x)
ax.set_xticklabels(x_values, rotation=45, ha='right')

ax.set_yticks(_y)
ax.set_yticklabels(y_values, ha='left')

ax.dist = 10

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/99_202312302126.png', bbox_inches='tight')

plt.clf()
