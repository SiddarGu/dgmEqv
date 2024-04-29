
import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Q1","Q2","Q3","Q4"]
line_labels = ["Crop Yield (Tonnes)","Livestock Population (Heads)","Farmland Utilization (%)","Food Processing (%)","Technology Adoption (%)"]
data = [[90,95,100,105],[75,80,85,90],[60,65,70,75],[70,75,80,85],[65,70,75,80]]

fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot(111, polar=True)
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

for i in range(len(data)):
    data[i].append(data[i][0])
    ax.plot(angles, data[i], linewidth=1.5, label=line_labels[i])

ax.fill(angles, data[i], alpha=0.25)
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)
ax.set_rlim(0, 105)

max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=0)

ax.set_title("Agriculture and Food Production in 2023", va='bottom', fontdict={'fontsize': 18})

handles, labels = ax.get_legend_handles_labels()
legend = ax.legend(handles, labels, loc=(0.9, .95), labelspacing=0.1)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar/png/9_202312262300.png')
plt.clf()