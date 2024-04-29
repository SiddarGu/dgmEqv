import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Number of Journals Indexed","Number of Published Articles","Number of Citations","Number of Research Grants"]
line_labels = ["Education","Psychology","Sociology","Anthropology","Political Science","Economics","History","Linguistics","Philosophy","Cultural Studies"]

data = np.array([[100,5000,20000,50],[150,8000,30000,80],[90,4000,18000,30],[70,3000,15000,20],
                 [120,6000,25000,60],[140,7000,28000,70],[80,3500,16000,40],[60,2500,13000,15],
                 [50,2000,10000,10],[110,5500,23000,55]])

fig = plt.figure(figsize=(30,22))
ax1 = fig.add_subplot(111)

ax1.bar(line_labels, data[:,0], label=data_labels[0], color='b', alpha=0.7, width=0.4)
ax1.set_ylabel(data_labels[0])
ax1.yaxis.label.set_color('blue')

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], label=data_labels[1], color='g')
ax2.set_ylabel(data_labels[1])
ax2.yaxis.label.set_color('green')

ax3 = ax1.twinx()
ax3.plot(line_labels, data[:,2], label=data_labels[2], color='r')
ax3.spines['right'].set_position(('outward', 60))      
ax3.set_ylabel(data_labels[2])
ax3.yaxis.label.set_color('red')

ax4 = ax1.twinx()
ax4.plot(line_labels, data[:,3], label=data_labels[3], color='c')
ax4.spines['right'].set_position(('outward', 120)) 
ax4.set_ylabel(data_labels[3])
ax4.yaxis.label.set_color('cyan')

ax1.set_title("Research Performance in Social Sciences and Humanities")
ax1.legend(loc='upper left')
ax2.legend(loc='upper center')
ax3.legend(loc='upper right')
ax4.legend(loc='lower right')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/328_202312311430.png')
plt.clf()
