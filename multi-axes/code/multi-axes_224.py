import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.ticker import AutoLocator

data = '''Platform,Monthly Users (millions),Average Session Duration (minutes),% of Internet Users
Facebook,2500,19,89
YouTube,2291,41,85
Instagram,1117,28,62
Twitter,330,3,22
Pinterest,459,8,32
LinkedIn,260,7,27
Snapchat,433,25,48
Reddit,430,11,22
TikTok,689,45,50
WeChat,1000,32,60'''

data = [i.split(',') for i in data.split('\n')]
line_labels = [i[0] for i in data[1:]]
data_labels = data[0][1:]
data = np.array([i[1:] for i in data[1:]], dtype=float)

colors = ['r', 'g', 'b', 'm']
fig = plt.figure(figsize=(25,15))

ax1 = fig.add_subplot(111)
ax1.bar(line_labels, data[:,0], color=colors[0], label=data_labels[0])
ax1.set_xlabel(data_labels[0])
ax1.legend(loc='upper left')
ax1.yaxis.label.set_color(colors[0])
ax1.yaxis.set_major_locator(AutoLocator())

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], color=colors[1], label=data_labels[1])
ax2.set_ylabel(data_labels[1])
ax2.yaxis.label.set_color(colors[1])
ax2.legend(loc='upper right')
ax2.yaxis.set_major_locator(AutoLocator())

if data.shape[1] > 2:
    ax3 = ax1.twinx()
    ax3.spines['right'].set_position(('outward', 60))  
    ax3.scatter(line_labels, data[:,2], color=colors[2], label=data_labels[2])
    ax3.set_ylabel(data_labels[2])
    ax3.yaxis.label.set_color(colors[2])
    ax3.legend(loc='lower left')
    ax3.yaxis.set_major_locator(AutoLocator())

if data.shape[1] > 3:
    ax4 = ax1.twinx()
    ax4.spines['right'].set_position(('outward', 120))  
    ax4.fill_between(line_labels, data[:,3], color=colors[3], label=data_labels[3], alpha=0.5)
    ax4.set_ylabel(data_labels[3])
    ax4.yaxis.label.set_color(colors[3])
    ax4.legend(loc='lower right')
    ax4.yaxis.set_major_locator(AutoLocator())

plt.title('Social Media Analysis: Users, Engagement, and Web Impact')
plt.grid()
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/225_202312311051.png')
plt.clf()
