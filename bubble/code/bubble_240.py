

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

data_labels = np.array(["Fundraising Revenue (Billion $)", "Volunteer Hours (Millions)", "Charitable Donations (Billion $)", "Social Impact Score"])
line_labels = np.array(["Red Cross", "World Vision", "Salvation Army", "Unicef", "Feeding America", "Doctors Without Borders"])
data = np.array([[1.2,2.5,6.4,75], [0.8,3.2,10.2,85], [1.5,2.1,5.3,80], [0.9,1.7,4.1,95], [0.6,1.5,3.7,90], [0.3,1.2,2.5,88]])

fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111)

for i in range(len(line_labels)):
    s=data[i,2]/data[:,2].max()*5000 + 600
    c=data[i,3]/data[:,3].max()
    ax.scatter(data[i,0], data[i,1], s=s, c=cm.coolwarm(c), label=None)
    ax.scatter([], [], c=cm.coolwarm(c), label=line_labels[i]+" "+str(data[i,2]))

ax.legend(title=data_labels[2])

norm = cm.colors.Normalize(vmin=data[:,3].min(), vmax=data[:,3].max())
sm = cm.ScalarMappable(cmap=cm.coolwarm, norm=norm)
sm.set_array([])
plt.colorbar(sm,ax=ax,label=data_labels[3])

ax.set_title('Impact of Charitable and Nonprofit Organizations in 2021')
ax.set_ylabel(data_labels[1])
ax.set_xlabel(data_labels[0])

ax.grid()
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/50_2023122261326.png')
plt.clf()