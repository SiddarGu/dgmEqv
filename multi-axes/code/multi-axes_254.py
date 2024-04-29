import matplotlib.pyplot as plt
import numpy as np

#setting given data as numpy array
data = np.array([
[1230,85,54,6], 
[1300,95,51,6.5], 
[2000,150,49,7], 
[2200,165,48,7.5], 
[2500,200,47,8], 
[2400,195,45,8.5], 
[2600,205,44,9], 
[2700,210,42,9.5], 
[2750,215,40,10], 
[2800,220,38,10.5], 
[3000,230,36,11], 
[3200,250,34,11.5]
])

data_labels = ["Website Visitors (thousands)", "Ad Revenue (thousands of dollars)", "Bounce Rate (%)", "Page views per visitor"]
line_labels = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

fig = plt.figure(figsize=(22,10))
ax1 = fig.add_subplot(111)

ln1 = ax1.plot(line_labels, data[:,0], 'g-', alpha=0.6,label=data_labels[0]) 
ax1.set_ylabel(data_labels[0], color='g')

ax2=ax1.twinx()
ln2 = ax2.plot(line_labels, data[:,1], 'b-', alpha=0.6,label=data_labels[1])
ax2.set_ylabel(data_labels[1], color='b')

ax3=ax1.twinx()
ln3=ax3.bar(line_labels, data[:,2], alpha=0.6, label=data_labels[2])
ax3.set_ylabel(data_labels[2])
ax3.spines["right"].set_position(("axes", 1.1))

ax4=ax1.twinx()
ln4=ax4.scatter(line_labels, data[:,3], c='r', alpha=0.6, label=data_labels[3])
ax4.set_ylabel(data_labels[3], color='r')
ax4.spines["right"].set_position(("axes", 1.2))

l1, l2, l3, l4 = ln1[0], ln2[0], ln3, ln4
plt.legend((l1, l2, l3, l4), (data_labels[0], data_labels[1], data_labels[2], data_labels[3]), loc=0)

plt.grid(True)

plt.autoscale(tight=True)
plt.title('Summary of Website Performance Metrics')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/211_202312311051.png')

plt.clf()
