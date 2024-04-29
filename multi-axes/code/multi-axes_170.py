import matplotlib.pyplot as plt
import numpy as np

# prepare data
data="""
Platform,Users in millions,Active Users in millions,Average Time Spent (Hours)
Facebook,2050,1890,2.34
Instagram,1720,1060,1.53
YouTube,2000,1870,2.13
WhatsApp,1500,1370,1.98
LinkedIn,420,295,0.97
Twitter,340,252,1.26
Snapchat,450,381,1.50
Pinterest,320,275,1.09
Reddit,250,222,1.37
Quora,220,185,0.87 
"""
lines = data.split("\n")[1:-1]
data_labels = lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in lines[1:]]
data = np.array([list(map(float, line.split(',')[1:])) for line in lines[1:]])

# create figure and ax
fig = plt.figure(figsize=(20, 10))
ax1 = fig.add_subplot(111)

# plot bar chart
ax1.bar(line_labels, data[:, 0], color='b', alpha=0.7, label=data_labels[0])

# create secondary y-axes and plot line, scatter, and area charts
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:, 1], color='g', label=data_labels[1])
  
ax3 = ax1.twinx()
ax3.scatter(line_labels, data[:, 2], color='r', label=data_labels[2])
ax3.spines['right'].set_position(('outward', 60))  

# label axes
ax1.set_xlabel("Platform")
ax1.set_ylabel(data_labels[0], color='b')
ax2.set_ylabel(data_labels[1], color='g')
ax3.set_ylabel(data_labels[2], color='r')

# set title
plt.title('User Engagement Across Different Social Media Platforms')

# show legend
ax1.legend(loc='upper left')
ax2.legend(loc='upper center')
ax3.legend(loc='upper right')

# final adjustments
plt.tight_layout()
plt.grid(True)
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/202_202312311051.png")
plt.clf()
