import matplotlib.pyplot as plt
import numpy as np

data_string = "Mode,Road,Sea,Air,Rail/n Volume of Goods (in k tons),1.5,1.2,1,1.3/n Frequency of Transit,70,60,80,50/n Average Transit Time (in days),3,7,1,4/n Cost per Mile ($),2,1,3,1.5/n Energy Efficiency (in MPG),20,25,15,30"
data_string = data_string.split("/n")

data_labels = data_string[0].split(",")[1:]
data = [line.split(",")[1:] for line in data_string[1:]]
line_labels = [line.split(",")[0] for line in data_string[1:]]
data = [[float(num) for num in line] for line in data]

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

for idx, line in enumerate(data):
    line += line[:1] 
    ax.plot(angles, line, linewidth=1, label=line_labels[idx])

for i in range(len(data)):
    radius = np.full_like(angles, (i+1) * max(sum(data, [])) / len(data))
    ax.plot(angles, radius, color="grey", linestyle='dashed', linewidth=0.5)

ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, wrap=True)
ax.set_ylim(bottom=0, top=max(sum(data, [])))
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

plt.title( 'Transportation and Logistics - Mode Analysis', size=20, color='black', pad=40)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/120_2023122292141.png')
plt.clf()

