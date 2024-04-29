import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.cm import ScalarMappable

# Transform the given data into three variables

raw_data = """Hotel,Occupancy Rate (%),Average Daily Rate ($),Revenue per Available Room ($),Guest Satisfaction (Score)
Marriott,70,150,105,8
Hilton,75,140,105,9
InterContinental,65,130,84.5,8
Holiday Inn,72,120,86.4,7
Sheraton,68,135,91.8,8
Wyndham,74,110,81.4,7
Best Western,73,100,73,7"""

lines = raw_data.split("\n")
data_labels = lines[0].split(",")[1:]
line_labels = [line.split(",")[0] + " " + line.split(",")[2] for line in lines[1:]]

data = np.array([line.split(",")[1:] for line in lines[1:]], dtype=float)

# Create a bubble chart

fig, ax = plt.subplots(figsize=(10, 8))

size_scale = 5000
color_scale = mcolors.Normalize(vmin=np.min(data[:, 3]), vmax=np.max(data[:, 3]))

for i in range(len(data)):
    ax.scatter(data[i, 0], data[i, 1], s=size_scale*data[i, 2]/np.max(data[:, 2]),
               c=plt.cm.viridis(color_scale(data[i, 3])), label=None)

    ax.scatter([], [], c=plt.cm.viridis(color_scale(data[i, 3])), s=20,
               label="{0}".format(line_labels[i]))

ax.legend(title=data_labels[2])
ax.grid(True)

plt.colorbar(ScalarMappable(norm=color_scale, cmap=plt.cm.viridis),
             ax=ax, label=data_labels[3])

ax.set_title('Performance and Guest Satisfaction of Hotel Chains in the Hospitality Industry')
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/259_202312310045.png')
plt.clf()
