import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# handle the data
rows = ['Under 20', '20-40', '40-60', '60-80', 'Over 80']
data = np.array([
    [200, 350, 75],
    [300, 500, 80],
    [400, 620, 85],
    [850, 1000, 90],
    [950, 1200, 92]
], dtype=np.float32).T
col_names = ['Number of Hospital Visits', 'Annual Healthcare Spending ($000)', 'Life Expectancy (years)']

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

x_values = np.arange(len(rows))
width = 0.2
colors = ['r', 'g', 'b']

for i in range(len(col_names)):
    ax.bar3d(x_values, [i]*len(rows), np.zeros(len(rows)), width, .1, data[i], color=colors[i], alpha=0.7)

ax.view_init(30, -20)
ax.set_xticks(x_values)
ax.set_yticks(np.arange(len(col_names)))
ax.set_xticklabels(rows, rotation=45, ha='right')
ax.set_yticklabels(col_names, va='bottom', ha='left')
ax.set_zlim([0, np.max(data)])
ax.set_title('Analysis of Healthcare Factors by Age Group')
plt.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/165_202312302235.png')
plt.clf()
