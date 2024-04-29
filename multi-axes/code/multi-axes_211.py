import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import colors
import numpy as np
from matplotlib.ticker import AutoLocator

# Data
raw_data = '''Category,Number of Artists,Attendees (Millions),Revenue (Millions of Dollars),Average Art Piece Price (Dollars)
Paintings,590,1.3,860,4500
Sculpture,410,0.9,720,5600
Photography,230,0.6,460,3300
Calligraphy,180,0.4,280,2400
Ceramics,310,0.8,500,3200
Textile Art,290,0.7,410,2600
Digital Art,370,0.9,620,3900
Performance Art,210,0.5,350,0
Literary Art,160,0.5,280,0'''
data_string = raw_data.split('\n')

line_labels = [item.split(',')[0] for item in data_string[1:]]
data_labels = data_string[0].split(',')[1:]
data = np.array([item.split(',')[1:] for item in data_string[1:]], dtype=float)

# Figure
fig = plt.figure(figsize=(20,10))

plot_types = ['bar', 'line', 'scatter', 'area']

# Axes
ax1 = fig.add_subplot(111)
ax1.bar(line_labels, data[:,0], color='b', alpha=0.6)
ax1.set_ylabel(data_labels[0], color='b')
for tl in ax1.get_yticklabels():
    tl.set_color('b')

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], color='r')
ax2.set_ylabel(data_labels[1], color='r')
for tl in ax2.get_yticklabels():
    tl.set_color('r')

if data.shape[1] > 2:
    ax3 = ax1.twinx()
    ax3.plot(line_labels, data[:,2], 'go')
    ax3.set_ylabel(data_labels[2], color='g')
    ax3.spines['right'].set_position(('outward', 60))
    for tl in ax3.get_yticklabels():
        tl.set_color('g')

if data.shape[1] > 3:
    ax4 = ax1.twinx()
    ax4.fill_between(line_labels, 0, data[:,3], color='c', alpha=0.5)
    ax4.set_ylabel(data_labels[3], color='c')
    ax4.spines['right'].set_position(('outward', 120))
    for tl in ax4.get_yticklabels():
        tl.set_color('c')

set_labels = [ax1, ax2, ax3, ax4]
for axes in set_labels:
    axes.yaxis.set_major_locator(AutoLocator())

# Legends and Title
ax1.legend([plot_types[i] for i in range(data.shape[1])], loc='upper left')
plt.title('The Arts and Culture Sector: Artist Count, Audience Attendance, and Financial Profits')

fig.autofmt_xdate()
plt.tight_layout()
# Save Figure
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/210_202312311051.png")
plt.clf()
