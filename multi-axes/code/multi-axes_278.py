import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

# transforming data into variables
data_labels = ['Number of degrees awarded by discipline', 'Number of enrolled students', 
               'Number of Full-Time Professors', 'Number of Research Papers Published']

line_labels = list(range(2010, 2021))

data = np.array([
    [2580, 32067, 562, 1581],
    [2632, 32500, 589, 1675],
    [2750, 33000, 600, 1720],
    [2900, 34000, 619, 1785],
    [3050, 35050, 641, 1920],
    [3150, 35900, 665, 2050],
    [3200, 36500, 683, 2125],
    [3250, 37200, 711, 2275],
    [3300, 38000, 745, 2400],
    [3400, 38700, 772, 2485],
    [3500, 39500, 785, 2550]
])

# creating figure and adding sub-plot
fig = plt.figure(figsize=(15,10))
ax1 = fig.add_subplot(111)
ax1.plot(line_labels, data[:,0], label=data_labels[0], color='b')
ax1.set_ylabel(data_labels[0], color='b')

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], label=data_labels[1], color='g')
ax2.set_ylabel(data_labels[1], color='g')

ax3 = ax1.twinx()
ax3.bar(line_labels, data[:,2], alpha=0.8, color='r')
ax3.set_ylabel(data_labels[2], color='r')

# spines and y-axes positioning
sp = ax3.spines['right']
sp.set_position(('outward',60))

ax4 = ax1.twinx()
ax4.plot(line_labels, data[:,3], label=data_labels[3], color='c')
ax4.set_ylabel(data_labels[3], color='c')

# spines y-axes positioning
sp = ax4.spines['right']
sp.set_position(('outward',120))

# set autolocator for y-axes
ax1.yaxis.set_major_locator(ticker.AutoLocator())
ax2.yaxis.set_major_locator(ticker.AutoLocator())
ax3.yaxis.set_major_locator(ticker.AutoLocator())
ax4.yaxis.set_major_locator(ticker.AutoLocator())

plt.title('Trends in Social Sciences and Humanities Education and Research from 2010-2020')

plt.grid()
plt.legend()
plt.tight_layout()

# save image and clear
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/171_202312310108.png')
plt.clf()
