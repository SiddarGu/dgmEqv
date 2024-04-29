import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator

# data
data_labels = ['Number of Students', 'Graduate Employment Rate (%)', 'Average Starting Salary ($)']
line_labels = ['2016', '2017', '2018', '2019', '2020', '2021']
data = np.array([[3000, 75, 50000],
                 [3200, 78, 52000],
                 [3400, 82, 55000],
                 [3500, 86, 57000],
                 [3600, 80, 60000],
                 [3700, 85, 61000]])

# initiate figure and subplot
fig = plt.figure(figsize=(25, 10))
ax1 = fig.add_subplot(111)

# plot bar chart
ax1.bar(np.arange(len(data[:, 0])), data[:, 0], alpha=0.6, color='b', align='center')
ax1.set_ylabel(data_labels[0], color='b')
ax1.tick_params(axis='y', colors='b')

# plot line chart
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:, 1], color='r')
ax2.set_ylabel(data_labels[1], color='r')
ax2.tick_params(axis='y', colors='r')

# plot scatter chart
ax3 = ax1.twinx()
ax3.scatter(line_labels, data[:, 2], color='g')
ax3.set_ylabel(data_labels[2], color='g')
ax3.spines['right'].set_position(('outward', 60))
ax3.tick_params(axis='y', colors='g')

# set up the y-axis grid
ax1.yaxis.set_major_locator(AutoLocator())
ax2.yaxis.set_major_locator(AutoLocator())
ax3.yaxis.set_major_locator(AutoLocator())

# set up the x-axis grid
ax1.xaxis.grid(True)
ax1.set_xlabel('Graduation Year')

# set up title, legends and save the figure
plt.title('Trends in Graduate Numbers, Employment Rates, and Starting Salaries Over Recent Years', fontsize=20)
ax1.legend([data_labels[0]], loc='upper left')
ax2.legend([data_labels[1]], loc='upper right')
ax3.legend([data_labels[2]], loc='center right')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/76_2023122292141.png')

plt.clf()
