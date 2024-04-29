import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.ticker import AutoMinorLocator, MultipleLocator, FuncFormatter

data = '''Civil Law,500,480,12
Criminal Law,800,780,10
Corporate Law,300,290,14
Family Law,600,590,11
Intellectual Property Law,400,390,13
Employment Law,700,680,10
Environmental Law,200,190,15
Immigration Law,100,90,16
Constitutional Law,200,190,14
Cyber Law,400,390,12'''

data = [row.split(',') for row in data.split('\n')]
data_labels = ['Number of Legal Cases Filed', 'Number of Cases Closed', 'Average Case Duration (Months)']
line_labels = [item[0] for item in data]
data = np.array([[int(item[j]) for j in range(1, len(item))] for item in data])

fig = plt.figure(figsize=(24, 12))
ax1 = fig.add_subplot(111)

ax1.bar(line_labels, data[:,0], color='b', alpha=0.6, label=data_labels[0])

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], color='r', label=data_labels[1])

ax3 = ax1.twinx()
ax3.plot(line_labels, data[:,2], color='g', label=data_labels[2])
ax3.spines['right'].set_position(('outward', 60))

ax1.xaxis.set_major_locator(MultipleLocator(1))
ax1.yaxis.set_major_locator(MultipleLocator(100))

ax2.yaxis.set_major_locator(MultipleLocator(100))

ax1.set_ylabel(data_labels[0], color='b')
ax2.set_ylabel(data_labels[1], color='r')
ax3.set_ylabel(data_labels[2], color='g')

plt.title('Analysis of Legal Cases: Filings, Closures, and Duration')
plt.grid(True)
plt.tight_layout()

lgd = fig.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05),
           ncol=3, fancybox=True, shadow=True)

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/309_202312311430.png', bbox_extra_artists=(lgd,), bbox_inches='tight')

plt.cla()
plt.clf()
plt.close()
