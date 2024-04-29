
import numpy as np
import matplotlib.pyplot as plt
data_labels = ['Crowd Size (%)','Ticket Revenue (%)','Customer Satisfaction (Score)','Safety & Security (Score)','Cost Management (Score)']
line_labels = ['Movie Theater', 'Sports Stadium', 'Amusement Park', 'Concert Hall']
data = np.array([[80,85,90,95],[60,65,70,75],[90,85,80,75],[85,80,75,70],[75,80,85,90]]).T
data = np.concatenate((data, data[:,0:1]),axis=1)
angles = np.linspace(0, 2*np.pi, len(data_labels)+1, endpoint=True)
fig = plt.figure(figsize=(20,20))
ax = fig.add_subplot(111, polar=True)
color = ['b','r','y','g']
for i in range(len(data)):
    ax.plot(angles, data[i], 'o-', linewidth=2, color=color[i], label=line_labels[i])
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, fontsize=14)
ax.set_rlim(0,100)
legend = ax.legend(loc='upper right', bbox_to_anchor=(1.25, 1))
ax.grid(True)
plt.title('Entertainment and Sports Industry Performance Review', fontsize=20)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/8_202312262300.png')
plt.clf()