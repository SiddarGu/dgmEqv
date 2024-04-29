import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

# data
data_labels = ['Attendance', 'Revenue (Millions)', 'Average Ticket Price']
line_labels = ['Olympics', 'FIFA World Cup', 'Super Bowl', 'Wimbledon', 'NBA Finals', 'World Series', 'Concert Tours', 'Boxing', 'Broadway Shows', 'Music Festivals']
data = np.array([
    [3490000, 5200, 1400],
    [3500000, 5000, 1500],
    [103000, 624, 4000],
    [470000, 220, 450],
    [190000,  300, 1000],
    [342000,   367, 800],
    [19000000, 1500, 200],
    [250000,   200, 800],
    [13000000, 1000, 150],
    [8000000,  2000, 200]])

fig = plt.figure(figsize=(15,10))
ax1 = fig.add_subplot(111)
ax1.bar(line_labels,data[:,0],color='b',alpha=0.7,label=data_labels[0])
ax1.yaxis.set_major_locator(ticker.AutoLocator())
ax1.set_ylabel(data_labels[0],color='b')
ax1.tick_params(axis='y', colors='b')

ax2 = ax1.twinx()
ax2.plot(line_labels,data[:,1],'g--',label=data_labels[1])
ax2.yaxis.set_major_locator(ticker.AutoLocator())
ax2.set_ylabel(data_labels[1],color='g')
ax2.spines['right'].set_color('g')
ax2.tick_params(axis='y', colors='g')

ax3 = ax1.twinx()
ax3.scatter(line_labels,data[:,2],color='r',label=data_labels[2])
ax3.yaxis.set_major_locator(ticker.AutoLocator())
ax3.set_ylabel(data_labels[2],color='r')
ax3.spines['right'].set_position(('outward',60))
ax3.spines['right'].set_color('r')
ax3.tick_params(axis='y', colors='r')

fig.legend(loc=(0.1, 0.1),fontsize='large')
plt.grid()
plt.title('Attendance, Revenue and Average Ticket Price in Sports and Entertainment') 
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/157_202312310108.png')
plt.close()
