
import matplotlib.pyplot as plt
import numpy as np

data_labels=['Air Quality (Score)','Water Quality (Score)','Waste Management (Score)','Use of Renewable Energy (Score)','Carbon Emission (Score)']
line_labels=['Region 1','Region 2','Region 3','Region 4']
data=np.array([[90,85,80,75],[95,90,85,80],[80,85,90,95],[70,75,80,85],[60,65,70,75]])

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_rlim(0,100)

for i in range(len(line_labels)):
    data_row=np.append(data[:,i],data[0,i])
    ax.plot(angles,data_row,label=line_labels[i])
    ax.fill(angles,data_row,alpha=0.1)
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels,loc=(0.94, 0.95))
plt.title("Global Sustainability Report - 2023")
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/9_202312262150.png")
plt.clf()