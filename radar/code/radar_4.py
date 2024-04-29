
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['University A','University B','University C','University D']
line_labels = ['Student Satisfaction (Score)','Quality of Teaching (Score)','Employment Rate (%)','Research Quality (Score)','Availability of Resources (Score)']
data = [[85,80,75,70],[90,85,80,75],[75,80,85,90],[80,85,90,95],[70,65,60,55]]

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(1, 1, 1, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels, fontsize=14)
ax.set_rlim(0, np.max(data))

for i in range(len(line_labels)):
    line_data = data[i]
    line_data.append(line_data[0]) # close the loop
    ax.plot(angles, line_data, linewidth=2, label=line_labels[i])

ax.legend(fontsize=12, bbox_to_anchor=(1.05, 0.5), loc='center left', borderaxespad=0.)
ax.set_title("Academic Performance Comparison", fontsize=16)

# draw background grids
ax.grid(True)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/3_202312262300.png')
plt.clf()