import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Data
data = np.array([[1980, 35000, 110000, 67, 140],
                 [1990, 50000, 160000, 72, 200],
                 [2000, 65000, 210000, 75, 280],
                 [2010, 80000, 270000, 78, 350],
                 [2020, 95000, 350000, 81, 420]])

data_labels = ["Number of Lawyers", "Number of Cases", "Success Rate (%)", "Number of Legal Firms"]
line_labels = data[:, 0]

fig = plt.figure(figsize=(15, 12))
ax1 = fig.add_subplot(111)

# Plot types: bar chart,line chart,area chart,scatter chart.
colors = ["r", "g", "b", "y"]
for idx, label in enumerate(data_labels):
    ax = ax1.twinx() if idx > 0 else ax1
    if idx == 0: 
        ax.bar(line_labels, data[:, idx+1], color=colors[idx], alpha=0.6)
    elif idx == 1:
        ax.plot(line_labels, data[:, idx+1], color=colors[idx])
    elif idx == 2:
        ax.fill_between(line_labels, data[:, idx+1], color=colors[idx], alpha=0.4)
    elif idx == 3:
        ax.scatter(line_labels, data[:, idx+1], color=colors[idx])
    if idx > 1:
        ax.spines['right'].set_position(('outward', 60 * (idx - 1)))
    ax.set_ylabel(label, color=colors[idx])
    ax.tick_params(axis='y', colors=colors[idx])

plt.title('Growth and Success of Legal Affairs over Decades')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/262_202312311051.png')
plt.clf()
