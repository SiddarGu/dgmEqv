import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from matplotlib.ticker import MultipleLocator, FormatStrFormatter, AutoMinorLocator


data = np.array([
    [386,21.33,5.52],
    [274.52,57.41,20.91],
    [182.53,40.27,22.06],
    [143,44.28,30.96],
    [85.97,29.15,33.90],
    [31.54,0.72,2.28],
    [82.58,14.71,17.82],
    [71.3,13.03,18.27],
    [21.84,10.93,50.05],
    [257.14,16.94,6.59]
])
data_labels = ["Revenue (Millions)","Net Income (Millions)","Profit Margin (%)"]
line_labels = ['Amazon','Apple', 'Alphabet', 'Microsoft','Facebook','Tesla','Johnson & Johnson','Procter & Gamble','Visa','UnitedHealth Group']
plot_types = ['bar', 'scatter', 'line']

fig = plt.figure(figsize=(20,10))
ax1 = fig.add_subplot(111)
ax1.bar(line_labels, data[:,0], color='b', alpha=0.6, align='center')
ax1.set_ylabel(data_labels[0])
ax1.yaxis.label.set_color('b')

ax2 = ax1.twinx()
ax2.scatter(line_labels, data[:,1], color='r')
ax2.set_ylabel(data_labels[1])
ax2.yaxis.label.set_color('r')

if data.shape[1] > 2:
    ax3 = ax1.twinx()
    ax3.spines['right'].set_position(('outward', 60))
    ax3.plot(line_labels, data[:,2], color='g')
    ax3.set_ylabel(data_labels[2])
    ax3.yaxis.label.set_color('g')


ax1.xaxis.set_tick_params(rotation=45)
ax1.set_title('Corporate Financial Performance: Revenue, Net Income, and Profit Margin')
fig.legend([data_labels[i] for i in range(data.shape[1])],loc='upper left', bbox_to_anchor=(0.1, 0.95))
plt.grid()
plt.autoscale(tight=True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/92_2023122292141.png')
plt.close(fig)
