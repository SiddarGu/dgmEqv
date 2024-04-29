import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator, MultipleLocator

# Data Preparation
data_all = '''Category,Users (Millions),Active Users (Millions),Average Time Spent (Hours),Number of Posts
Social Networking,2400,1800,4.5,1200
Video Sharing,1700,900,3.2,800
Blogging,1400,600,2.8,600
Microblogging,1500,800,3.5,700
Social News,800,400,2.2,400
Online Forums,1100,500,2.5,500
Photo Sharing,1900,1000,3.8,900
Social Gaming,1200,700,2.9,700
Instant Messaging,2000,1500,5,1100
Dating Sites,1000,400,2,300
Mobile Apps,2400,1600,4.2,1300'''

data_all = data_all.split('\n')
data_labels = data_all[0].split(',')[1:]
line_labels = [x.split(',')[0] for x in data_all[1:]]
data = np.array([list(map(float, x.split(',')[1:])) for x in data_all[1:]])

# Create Plot
fig, ax1 = plt.subplots(figsize=(12,8))
markers = ['s','o','^','x','*']

# First Column Data
ax1.bar(line_labels, data[:,0], color='c', alpha=0.6, label=data_labels[0])
plt.title('Social Media and the Web Usage Analysis: Users, Activity, and Engagement')
ax1.set_ylabel(data_labels[0])

# Second Column Data
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], color='b',marker=markers[1], label=data_labels[1])
ax2.set_ylabel(data_labels[1])

# Third Column Data
if len(data[0]) > 2:
    ax3 = ax1.twinx()
    ax3.scatter(line_labels, data[:,2], color='r', marker=markers[2], label=data_labels[2])
    ax3.spines["right"].set_position(("axes", 1.1))
    ax3.set_ylabel(data_labels[2])

# Fourth Column Data
if len(data[0]) > 3:
    ax4 = ax1.twinx()
    ax4.fill_between(line_labels, data[:,3], color='g', alpha=0.3, label=data_labels[3])
    ax4.spines["right"].set_position(("axes", 1.2))
    ax4.set_ylabel(data_labels[3])

# Configurations
fig.autofmt_xdate(rotation=45)
plt.tight_layout()

# Legends
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
if len(data[0]) > 2: ax3.legend(loc='center left')
if len(data[0]) > 3: ax4.legend(loc='center right')

# Save Plot
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/270_202312311430.png')
plt.clf()
