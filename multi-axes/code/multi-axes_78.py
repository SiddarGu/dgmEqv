import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoLocator

data_labels = ['Number of Museums', 'Attendance (Millions)','Revenue (Millions of Dollars)', 'Average Ticket Price']
line_labels = ['Art Museums','History Museums','Science Museums','Natural History Museums','Music Venues','Theaters','Galleries']
data = np.array([[500,55,400,8],[400,40,350,9],[300,25,300,12],[200,20,250,13],[600,75,500,10],[800,80,600,12],[1000,50,450,9]])

fig = plt.figure(figsize=(25, 10))

ax1 = fig.add_subplot(111)
ax1.bar(line_labels, data[:,0], width=0.4, color='blue', alpha=0.6, label=data_labels[0])

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1],'r', label=data_labels[1])
loc = AutoLocator()
ax2.yaxis.set_major_locator(loc)

ax3 = ax1.twinx()
ax3.spines["right"].set_position(("axes", 1.1))
ax3.plot(line_labels,data[:,2],'g', label=data_labels[2])
loc = AutoLocator()
ax3.yaxis.set_major_locator(loc)

ax4 = ax1.twinx()
ax4.spines["right"].set_position(("axes", 1.2))
ax4.plot(line_labels,data[:,3],'b', label=data_labels[3])
loc = AutoLocator()
ax4.yaxis.set_major_locator(loc)

ax1.set_ylabel(data_labels[0], color='blue')
ax2.set_ylabel(data_labels[1], color='red')
ax3.set_ylabel(data_labels[2], color='green')
ax4.set_ylabel(data_labels[3], color='blue')

ax1.set_xlabel('Category')
ax1.set_title('Arts and Culture Institutions: Museums, Venues, and Revenue Analysis')

fig.legend(loc="upper left", bbox_to_anchor=(0,1), bbox_transform=ax1.transAxes)

plt.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/333_202312311430.png')

plt.close()
