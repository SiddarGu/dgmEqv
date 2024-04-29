
import numpy as np
import matplotlib.pyplot as plt

data_labels=["Q1","Q2","Q3","Q4"]
line_labels=["Job Satisfaction (score)","Work-life Balance (score)","Training and Development (score)","Employee Engagement (score)","Retention Rate (%)"]
data=[[70,75,80,85],[50,55,60,65],[60,65,70,75],[80,85,90,95],[65,70,75,80]]

angles=np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True) # evenly space the axes for the number of data points
fig=plt.figure(figsize=(10,10))
ax=fig.add_subplot(111, polar=True) # Create figure before plotting
for i in range(len(data)):
    data[i].append(data[i][0])
    ax.plot(angles, data[i], 'o-', linewidth=2, label=line_labels[i])
    ax.fill(angles, data[i], alpha=0.25)
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_title('Employee Management - 2023', fontsize=20)
ax.set_rlim(min(min(data))-10,max(max(data))+10)
ax.xaxis.label.set_rotation(90)
handles, labels=ax.get_legend_handles_labels()
ax.legend(handles, labels, loc=(0.9,0.95))
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/2_202312262150.png")
plt.clf()