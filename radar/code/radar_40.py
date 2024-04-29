
import numpy as np
import matplotlib.pyplot as plt

data_labels = ['Q1','Q2','Q3','Q4']
line_labels = ['Price (%)','Supply (%)','Demand (%)','Home Sales (%)','Mortgage Rates (%)']
data = [[65,70,75,80],[50,55,60,65],[60,65,70,75],[80,85,90,95],[70,75,80,85]]

angles = np.linspace(0, 2*np.pi, len(data_labels)+1, endpoint=True)
fig = plt.figure(figsize=(16,8))
ax = fig.add_subplot(111, polar=True)
ax.set_title('Real Estate and Housing Market Overview - 2023', fontsize=16)
ax.tick_params(labelsize=14)

for i in range(len(data)):
    data[i].append(data[i][0]) 
    ax.plot(angles, data[i], label=line_labels[i], linewidth=2)
    ax.fill(angles, data[i], alpha=0.25)

ax.set_thetagrids(angles[:-1]*180/np.pi, data_labels, fontsize=14)
ax.set_ylim(0,100)
ax.grid(True)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels, fontsize=14, loc='upper right')
fig.tight_layout()
fig.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/13_202312262150.png')
plt.cla()