import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator
import numpy as np

data_string = "Year,Number of Cases,Laws Passed,Average Trial Duration (Days),Courts Clearance Rate(%)/n 2010,5500,219,56,70.5/n 2011,5800,225,60,71.0/n 2012,6000,230,58,72.0/n 2013,5700,205,62,73.0/n 2014,5900,210,59,75.0/n 2015,6100,220,61,74.5/n 2016,6200,224,60,76.0/n 2017,6300,232,57,77.5/n 2018,6400,240,55,78.0/n 2019,6500,248,56,79.5"
lines = data_string.split('/n')
data_labels = lines[0].split(',')
line_labels = [line.split(',')[0] for line in lines[1:]]

data = np.array([list(map(float, line.split(',')[1:])) for line in lines[1:]])

fig = plt.figure(figsize=(25, 10))
ax1 = fig.add_subplot(111)
line1, = ax1.plot(line_labels, data[:, 0], color='blue', label=data_labels[1])
ax1.set_ylabel(data_labels[1], color='blue')
ax1.yaxis.set_major_locator(AutoLocator())
ax2 = ax1.twinx()
bars = ax2.bar(line_labels, data[:, 1], color='orange', label=data_labels[2], alpha=0.6)
ax2.set_ylabel(data_labels[2], color='orange')
ax2.yaxis.set_major_locator(AutoLocator())
ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60))
line3 = ax3.fill_between(line_labels, data[:, 2], color='green', label=data_labels[3], alpha=0.5)
ax3.set_ylabel(data_labels[3], color='green')
ax3.yaxis.set_major_locator(AutoLocator())
ax4 = ax1.twinx()
ax4.spines['right'].set_position(('outward', 120))
line4, = ax4.plot(line_labels, data[:, 3], color='red', label=data_labels[4])
ax4.set_ylabel(data_labels[4], color='red')
ax4.yaxis.set_major_locator(AutoLocator())

fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.85))
fig.legend(loc='upper right', bbox_to_anchor=(0.9, 0.85))

ax1.set_xlabel(data_labels[0])
fig.autofmt_xdate()
fig.suptitle('Judicial Performance Over the Past Decade')

fig.tight_layout()
plt.grid(True)
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/104_202312310108.png')
plt.clf()
