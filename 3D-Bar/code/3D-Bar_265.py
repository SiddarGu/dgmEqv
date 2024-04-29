import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

y_values = ["Auto Manufacturing (Units)", "Electronics Manufacturing (Units)", 
            "Machinery Manufacturing (Units)", "Chemical Production (Units)"]
x_values = ["Q1", "Q2", "Q3", "Q4"]
data = np.array([[1500, 1800, 2200, 2600],
                 [1700, 2000, 2300, 2700],
                 [1600, 2100, 2400, 2800],
                 [1800, 2300, 2600, 3100]], dtype=np.float32)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

_bar_width = 0.15
_colors = ['r', 'g', 'b', 'c']

for i, yt in enumerate(y_values):
    ax.bar3d(
        np.arange(len(x_values)) + (_bar_width * i),
        [i]*len(x_values),
        [0]*len(x_values),
        _bar_width,
        1,
        data[:, i],
        color=_colors[i],
        alpha=0.8
    )

ax.view_init(elev=30, azim=-60)  
ax.set_xticks(np.arange(len(x_values)) + (_bar_width * (len(y_values) - 1) / 2))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=30, ha='right')
ax.set_yticklabels(y_values, ha='left')

ax.set_title("Quarterly Trend in Manufacturing Sector Production - Auto, Electronics, Machinery, Chemicals")
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/195_202312302235.png')
plt.clf()
