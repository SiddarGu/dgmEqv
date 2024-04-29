import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import AutoLocator

data_str = '''Soccer,5000,25000,80%,10
Basketball,4000,20000,90%,8
Baseball,3000,15000,70%,6
Football,6000,30000,85%,12
Hockey,2000,10000,75%,4
Tennis,1000,5000,95%,2
Golf,1500,7500,60%,3
Volleyball,2500,12500,80%,5
Rugby,800,4000,70%,1
Swimming,1200,6000,75%,2
Cycling,600,3000,65%,1
Running,1000,5000,85%,2
Ice Skating,500,2500,60%,1
Martial Arts,700,3500,80%,1
Gymnastics,900,4500,75%,2
Track and Field,400,2000,70%,1
Table Tennis,300,1500,90%,1
Badminton,600,3000,80%,1'''

data = list(map(lambda x: x.split(','), data_str.split('\n')))
df = pd.DataFrame(data, columns = ["Category","Tickets","Revenue","Attendance","Events"])
df['Tickets'] = df['Tickets'].astype(int)
df['Revenue'] = df['Revenue'].astype(int)
df['Attendance'] = df['Attendance'].str.rstrip('%').astype('float')
df['Events'] = df['Events'].astype(int)

fig = plt.figure(figsize=(20,10))
ax1 = fig.add_subplot(111)
ax1.bar(df['Category'], df['Tickets'], color='b', alpha=0.3, width=0.4)
ax1.set_xlabel('Category', color='b')
ax1.set_ylabel('Tickets')
ax1.yaxis.label.set_color('b')
plt.title("Sports and Entertainment Event Analysis")

ax2 = ax1.twinx()
ax2.plot(df['Category'], df['Revenue'], 'r-')
ax2.set_ylabel('Revenue')
ax2.yaxis.label.set_color('r')

ax3 = ax1.twinx()
ax3.scatter(df['Category'], df['Attendance'], color='g')
ax3.set_ylabel('Attendance', color='g')
ax3.spines['right'].set_position(('outward', 60))

ax4 = ax1.twinx()
ax4.fill_between(df['Category'], df['Events'],color='y', alpha=0.4)
ax4.set_ylabel('Events', color='y')
ax4.spines['right'].set_position(('outward', 120))

fig.legend(labels=['Tickets','Revenue','Attendance','Events'],loc='upper left')

ax1.grid()

ax1.yaxis.set_major_locator(AutoLocator())
ax2.yaxis.set_major_locator(AutoLocator())
ax3.yaxis.set_major_locator(AutoLocator())
ax4.yaxis.set_major_locator(AutoLocator())

plt.tight_layout()

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/292_202312311430.png')
plt.clf()
