import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib import cm

# raw data
raw_data = '''Category,Attendees (Thousands),Revenue (Millions of Dollars),Average Ticket Price (Dollars)
Theatre,9720,38450,45
Concerts,13480,57550,60
Museums,6500,14230,20
Art Exhibitions,6950,18040,35
Music Festivals,14950,57200,55
Ballet,6000,13200,30
Opera,4720,17200,50
Film Festivals,7200,20400,40
Art Galleries,11200,27800,30
Symphony Orchestras,5300,19200,40'''

# parse the raw data
lines = raw_data.split('\n')
header = lines[0]
rows = lines[1:]
data_labels = header.split(',')[1:]
line_labels = [row.split(',')[0] for row in rows]
data = np.array([list(map(int, row.split(',')[1:])) for row in rows])

# create figure and ax
fig, ax1 = plt.subplots(figsize=(30, 10))
axes = [ax1, ax1.twinx(), ax1.twinx()]

# get color list
colors = [cm.viridis(x) for x in np.linspace(0, 1, len(data_labels))]

# plot data and adjust axes
for i, (ax, color, label, plot_type) in enumerate(zip(axes, colors, data_labels, ['plot', 'plot', 'bar'])):
    if plot_type == 'bar':
        ax.bar(line_labels, data[:, i], color=color, label=label, alpha=0.5)
    else:
        ax.plot(line_labels, data[:, i], color=color, label=label)
        
    ax.set_ylabel(label, color=color)
    ax.tick_params(axis='y', colors=color)
    ax.yaxis.set_major_locator(ticker.AutoLocator())

# separate y axes of ax2 and ax3
axes[2].spines['right'].set_position(('outward', 60)) 

# title and legend
plt.title('Arts and Culture Performance Analysis: Attendance, Revenue and Ticket Pricing')
for ax in axes:
    ax.legend(loc="upper left", bbox_to_anchor=(0,1))

# grid, tight_layout, and savefig
plt.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/77_2023122292141.png')

# clear figure
plt.clf()
