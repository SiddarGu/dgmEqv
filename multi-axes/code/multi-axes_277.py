

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

data_labels = ['Tickets Sold (Millions)','Average Ticket Price (Dollars)']
line_labels = ['Theater','Music','Dance','Circus','Opera','Film','Visual Arts','Literary Arts','Comedy']
data = np.array([[1090,3110,39], [500,6590,50], [650,3040,33], [1490,2700,66], [710,7250,31], [1130,8180,34], [1220,3000,55], [600,7250,70], [600,7630,50]])

fig = plt.figure(figsize=(15, 8))
ax = fig.add_subplot(111)
ax.bar(line_labels, data[:,1], width=0.7, color='#008080', alpha=0.9, label='Tickets Sold (Millions)', zorder=3) 
ax.set_xlabel('Category')
ax.set_ylabel('Tickets Sold (Millions)')
ax2 = ax.twinx()
ax2.plot(line_labels, data[:,2], marker='o', color='#FF7F50', label='Average Ticket Price (Dollars)', linestyle='--', zorder=2)
ax2.set_ylabel('Average Ticket Price (Dollars)')

ax3 = ax.twinx()
ax3.spines['right'].set_position(('axes', 1.1))
ax3.plot(line_labels, data[:,0], marker='s', color='#FF0000', label='Number of Performances', linestyle='-.', zorder=1)
ax3.set_ylabel('Number of Performances')

plt.title('Arts and Culture Performance Analysis: Attendance, Revenue, and Pricing Trends',fontsize=20)
ax.legend(loc=2, bbox_to_anchor=(0., 1.0, 0.3, 0.1), mode="expand", borderaxespad=0.)
ax2.legend(loc=1, bbox_to_anchor=(0., 0.95, 0.3, .2), mode="expand", borderaxespad=0.)
ax3.legend(loc=3, bbox_to_anchor=(0., 0.9, 0.3, .2), mode="expand", borderaxespad=0.)

ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.2))
ax.yaxis.set_major_locator(ticker.MultipleLocator(1000))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(200))
ax.yaxis.set_major_locator(ticker.MultipleLocator(1000))
ax2.yaxis.set_minor_locator(ticker.MultipleLocator(200))
ax3.yaxis.set_major_locator(ticker.MultipleLocator(200))
ax3.yaxis.set_minor_locator(ticker.MultipleLocator(40))

ax.autoscale_view()
ax2.autoscale_view()
ax3.autoscale_view()

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/37_2023122261325.png')
plt.clf()