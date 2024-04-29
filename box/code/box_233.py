
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

data = [[3, 5, 7, 9, 11], [10, 15, 20, 25, 30], [2, 4, 6, 8, 10], [4, 8, 12, 16, 20], [6, 12, 18, 24, 30]]
outlier = [[], [40], [1, 11], [21], [35]]

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111)
ax.boxplot(data, whis=1.5, showmeans=True, meanline=True, showbox=True, showcaps=True,
            showfliers=True, notch=False, labels=['Assembly Line', 'Robot Automation', '3D Printing', 'CNC Machining', 'Product Design'])

for i, o in enumerate(outlier):
    if len(o) > 0:
        x = np.repeat(i + 1, len(o))
        ax.plot(x, o, 'ro', alpha=0.6)

ax.set_title('Production Time Distribution in Manufacturing Processes (2020)')
ax.set_ylabel('Time (Hours)')
ax.grid(True)
plt.xticks(rotation=45, ha='right', wrap=True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/1_202312251608.png')
plt.clf()