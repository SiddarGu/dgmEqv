import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator
import numpy as np

data_labels = ["Number of Students Enrolled", "Number of Graduates", "Grants Offered (Millions)"]
line_labels = ['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019']
data = np.array([[6832,6190,157], [6950,6403,167], [7235,6708,172], [7507,7010,188], [7718,7235,202], [8088,7420,213],
                 [8302,7658,225], [8491,7895,239], [8710,8130,252], [8912,8310,273]])

fig = plt.figure(figsize=(25,15))
ax1 = fig.add_subplot(111)
ax1.plot(line_labels, data[:,0], label=data_labels[0], color='tab:blue')
ax1.set_xlabel('Year')
ax1.set_ylabel(data_labels[0], color='tab:blue')

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], label=data_labels[1], color='tab:orange')
ax2.set_ylabel(data_labels[1], color='tab:orange')

if data.shape[1] > 2:
    ax3 = ax1.twinx()
    ax3.spines['right'].set_position(('outward', 60))  
    ax3.plot(line_labels, data[:,2], label=data_labels[2], color='tab:green')
    ax3.set_ylabel(data_labels[2], color='tab:green')

ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

plt.gca().xaxis.set_major_locator(AutoLocator())
plt.gca().yaxis.set_major_locator(AutoLocator())

plt.title('A Decade of Progress in Social Sciences and Humanities Education')
plt.grid(True)
plt.tight_layout()

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/209_202312311051.png')
plt.clf()
