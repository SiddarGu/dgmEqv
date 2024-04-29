
import numpy as np
import matplotlib.pyplot as plt

data_labels = ['Tourism Expenditure (US$)','Accommodation Capacity (K Rooms)','Hotels Rating (Stars)','Tourist Attractions (Number)','Quality of Service (Score)']
line_labels = ['Shanghai','Beijing','Chengdu','Guangzhou','Hangzhou']
data = np.array([[10,20,30,40,50],[50,60,70,80,90],[45,48,50,52,55],[100,125,150,175,200],[90,85,80,75,70]])
data = np.concatenate((data, data[:, 0:1]), axis=1)

fig = plt.figure(figsize=(18,18))
ax = fig.add_subplot(111, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, fontsize=12)
ax.set_rlim(-1, np.max(data)+5)
ax.set_title('Tourism and Hospitality - 2021', fontsize=14)

for i in range(len(data)):
    ax.plot(angles, data[i], label=line_labels[i])
    ax.fill(angles, data[i], alpha=0.1)

ax.grid(True)
ax.legend(line_labels, loc="best")
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/29_202312262320.png')
plt.clf()