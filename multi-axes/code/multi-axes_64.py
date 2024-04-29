import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker

# Data preparation
raw_data = "Category,Number of Researchers,Research Expenditure (Millions of Dollars),Number of Patents Granted/n Mathematics,2000,535.5,800/n Computer Science,6850,980.1,5500/n Physics,5000,895.3,3850/n Chemistry,2800,620.8,4150/n Biology,3200,699.9,4700/n Environmental Science,1560,400.7,1800/n Mechanical Engineering,6580,1129.2,4950/n Electrical Engineering,7000,1219.8,5450/n Civil Engineering,3900,845.7,3550/n Chemical Engineering,3215,702.1,4400/n Biomedical Engineering,2870,635.9,3600"
raw_data = raw_data.replace('/n', '\n').split('\n')
data_labels = raw_data[0].split(',')

line_labels = []
data = []

for line in raw_data[1:]:
    record = line.split(',')
    line_labels.append(record[0])
    data.append(list(map(float, record[1:])))

data = np.array(data)

# Data plotting
colors = ['r', 'b', 'g']
fig = plt.figure(figsize=(20, 14))

ax1 = fig.add_subplot(111)
ax1.bar(line_labels, data[:,0], color=colors[0], alpha=0.7, label=data_labels[1])
ax1.set_ylabel(data_labels[1], color=colors[0], fontsize=15)
ax1.tick_params(axis='y', colors=colors[0])
ax1.yaxis.set_major_locator(ticker.AutoLocator())

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], color=colors[1], alpha=0.7, label=data_labels[2])
ax2.set_ylabel(data_labels[2], color=colors[1], fontsize=15)
ax2.tick_params(axis='y', colors=colors[1])
ax2.yaxis.set_major_locator(ticker.AutoLocator())

ax3 = ax1.twinx()
rspine = ax3.spines['right']
rspine.set_position(('axes', 1.15))
ax3.scatter(line_labels, data[:,2], color=colors[2], alpha=0.7, label=data_labels[3])
ax3.set_ylabel(data_labels[3], color=colors[2], fontsize=15)
ax3.tick_params(axis='y', colors=colors[2])
ax3.yaxis.set_major_locator(ticker.AutoLocator())
ax3.grid(None)

plt.xlabel(data_labels[0], fontsize=15)
plt.title('Research Activity in Science and Engineering: Researchers, Expenditure, and Patents', fontsize=20)
plt.legend(loc='upper left')

ax1.legend(loc='upper right')
ax2.legend(loc='upper center')

plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/103_202312310108.png")

plt.close()
