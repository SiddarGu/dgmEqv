import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

data_labels = ['Number of Donors', 'Total Donations', 'Ratio of Admin Expenses to Total Expenses', 'Program Expenses Ratio']
line_labels = ['Health', 'Education', 'Environment', 'Animal Welfare', 'Social Services']
data = np.array([[1500, 30000, 0.2, 0.7], 
                 [1200, 25000, 0.3, 0.6], 
                 [800, 18000, 0.1, 0.8],
                 [1000, 20000, 0.15, 0.75], 
                 [2000, 40000, 0.25, 0.65]])

fig = plt.figure(figsize=(25,10))
ax1 = fig.add_subplot(111)

ax1.bar(line_labels, data[:,0], color='b', label=data_labels[0])
ax1.set_xlabel(line_labels)
ax1.set_ylabel(data_labels[0], color='b')
ax1.tick_params(axis='y', colors='b')
ax1.yaxis.set_major_locator(ticker.AutoLocator())

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], color='g', label=data_labels[1])
ax2.set_ylabel(data_labels[1], color='g')
ax2.tick_params(axis='y', colors='g')
ax2.yaxis.set_major_locator(ticker.AutoLocator())

ax3 = ax1.twinx()
ax3.plot(line_labels, data[:,2], color='r', label=data_labels[2],alpha=0.5)
ax3.spines['right'].set_position(('outward', 60))
ax3.set_ylabel(data_labels[2], color='r')
ax3.tick_params(axis='y', colors='r')
ax3.yaxis.set_major_locator(ticker.AutoLocator())

ax1.legend(loc='upper left')
ax2.legend(loc='upper center')
ax3.legend(loc='upper right')

plt.title('Analysis of Donor Engagement and Financial Efficiency in the Nonprofit Sector')
plt.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/281_202312311430.png')
plt.cla()
