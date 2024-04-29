
import matplotlib.pyplot as plt
import numpy as np

data_labels=['Q1','Q2','Q3','Q4']
line_labels=['Academic Results','Collaboration','Student-Teacher Relations','Quality of Teaching','Resources']
data=[[80,85,90,95],[75,80,85,90],[65,70,75,80],[85,90,95,100],[60,65,70,75]]

plt.figure(figsize=(10,10))
ax = plt.subplot(111, polar=True)
angles=np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
for i in range(len(data)):
    data[i].append(data[i][0])
    ax.plot(angles, data[i], linewidth=1, linestyle='solid', label=line_labels[i])
    ax.fill(angles, data[i], alpha=0.3)
    r=np.full_like(angles, (i+1)*max(max(data))/len(data))
    ax.plot(angles, r, 'k', linewidth=1, linestyle='dashed')
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, fontsize=14)
ax.set_ylim(0, max(max(data))+3)
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")
ax.set_title('Education Quality in 2023', fontsize=14)
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)
plt.tight_layout()
plt.savefig(r'/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/2.png')
plt.clf()