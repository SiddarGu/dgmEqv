import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable

raw_data = [('Healthcare Reform', 2000, 67, 8.5, 9),
            ('Education Policy', 1500, 75, 8, 9.5),
            ('Climate Change Mitigation', 1000, 65, 9.2, 10),
            ('Defense Spending', 2500, 45, 7, 8.5),
            ('Tax Reform', 500, 56, 7.5, 8),
            ('International Trade Policy', 3000, 60, 8.5, 9)]
    
data = np.array([list(x[1:]) for x in raw_data])
line_labels = ["{}\n({}%)".format(x[0], x[2]) for x in raw_data]
data_labels = ['Implementation Cost (Billion $)', 'Public Support (%)', 'Efficiency (Score)', 'Reliability (Score)']
color_range = Normalize(vmin=min(data[:, 3]), vmax=max(data[:, 3]))

fig, ax = plt.subplots(figsize=(10, 6))

for i, line_label in enumerate(line_labels):
    c = cm.viridis(color_range(data[i, 3]))
    ax.scatter(data[i, 0], data[i, 1], alpha=0.6, s=600+4000*(data[i, 2]/100), label=None, color=c)
    ax.scatter([], [], label=line_label, color=c, alpha=0.6)

ax.legend(title=data_labels[2], bbox_to_anchor=(1.1, 1), loc='upper left')
sm = ScalarMappable(cmap='viridis', norm=color_range)
sm.set_array([])
plt.colorbar(sm, label=data_labels[3], pad=0)

ax.set_title('Assessment of Different Government Policies')
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.grid(True)
fig.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/62_202312301731.png', format='png')
plt.clf()
