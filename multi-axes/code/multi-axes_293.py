import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Data Transformation
raw_data = "Month,Website Visitors (Thousands),Active Users (Thousands),Average Session Time (Minutes)\n January,1020,984,8.4\n February,1055,1018,8.8\n March,1080,1064,9.2\n April,1140,1120,9.6\n May,1200,1190,10.1\n June,1265,1250,10.5\n July,1300,1280,11.0\n August,1340,1320,11.5\n September,1390,1370,12.0\n October,1450,1420,12.5\n November,1480,1450,13.0\n December,1550,1520,14.0"
rows = raw_data.split('\n')

data_labels = rows[0].split(',')[1:]
line_labels = [row.split(',')[0] for row in rows[1:]]
data = np.array([list(map(float,row.split(',')[1:])) for row in rows[1:]])

# Plotting
fig = plt.figure(figsize=(25, 10))
ax1 = fig.add_subplot(111)

# Plot Line chart for the first column
ax1.plot(line_labels, data[:, 0], color='b', label=data_labels[0])
ax1.set_xlabel('Month')
ax1.set_ylabel(data_labels[0], color='b')
ax1.tick_params('y', colors='b')

# Overlay second plot over the first plot with shared x-axis
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:, 1], color='g', label=data_labels[1])
ax2.set_ylabel(data_labels[1], color='g')
ax2.tick_params('y', colors='g')

# Overlay third plot over the first plot with shared x-axis
ax3 = ax1.twinx()
ax3.fill_between(line_labels, data[:, 2], color='r', alpha=0.5, label=data_labels[2])
ax3.set_ylabel(data_labels[2], color='r')
ax3.tick_params('y', colors='r')
ax3.spines['right'].set_position(('outward', 60))

ax1.xaxis.set_major_locator(ticker.AutoLocator())
ax2.yaxis.set_major_locator(ticker.AutoLocator())
ax3.yaxis.set_major_locator(ticker.AutoLocator())

fig.legend(loc=1)

plt.title('Website Performance Metrics: Visitor, User Engagement, and Session Analysis')
plt.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/83_2023122292141.png')
plt.close(fig)
