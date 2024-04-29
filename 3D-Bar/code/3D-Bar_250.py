import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data = np.array([[45, 65, 90], [35, 70, 75], [50, 55, 80], [60, 75, 90], [40, 55, 70]], dtype=np.float32)
x_values = ["US", "UK", "Italy", "France", "Japan"]
y_values = ["Gallery Visitors (Millions)", "Cultural Events (Thousands)", 
            "Ancient Landmarks (Number of Visits - Millions)"]

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

xpos = np.arange(len(x_values))
ypos = np.arange(len(y_values))

for i in range(len(y_values)):
    ax.bar3d(xpos, [i]*len(x_values), np.zeros_like(xpos), 
              0.4, 0.4, data[:, i], alpha=0.8)

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45, ha='right')
ax.set_yticklabels(y_values, ha='left')

ax.set_title("Analysis of Arts and Culture Popularity by Country")

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/212_202312302235.png')
plt.clf()
