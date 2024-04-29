

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

data_labels = ["Number of Volunteers", "Donations Received (in Millions of Dollars)", "Fundraising Events"]
line_labels = ["Homeless Shelters", "Animal Shelters", "Food Banks", "Mental Health Charities", "Education",
               "Hospices", "Arts and Cultural Organizations", "Environmental Groups", "Humanitarian Aid",
               "Religous Charities", "International Organizations"]
data = np.array([[220,77,12],
                 [100,50,9],
                 [140,72,15],
                 [200,98,10],
                 [180,70,12],
                 [90,64,10],
                 [100,50,8],
                 [150,68,13],
                 [210,89,11],
                 [160,87,11],
                 [190,75,14]])

fig = plt.figure(figsize=(15, 10))
ax1 = fig.add_subplot(111)
ax1.bar(line_labels, data[:,0], width=0.4, color='r', alpha=0.7)
ax1.set_ylabel(data_labels[0], color='r')
ax1.tick_params('y', colors='r')
ax1.set_xlabel('Category', fontsize=12)
ax1.set_title('Charitable Giving and Volunteerism: An Analysis of Trends', fontsize=18)

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], color='b', marker='o', linestyle='dashed', linewidth=2, markersize=6)
ax2.set_ylabel(data_labels[1], color='b')
ax2.tick_params('y', colors='b')

ax3 = ax1.twinx()
ax3.spines["right"].set_position(("axes", 1.1))
ax3.plot(line_labels, data[:,2], color='g', marker='^', linestyle='-.', linewidth=2, markersize=6)
ax3.set_ylabel(data_labels[2], color='g')
ax3.tick_params('y', colors='g')

ax1.set_xticklabels(line_labels, rotation=45)
ax1.grid(True)
plt.tight_layout()

plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='upper center',
           ncol=3, mode="closest", borderaxespad=0.)

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/10_202312251608.png')
plt.show()
plt.clf()