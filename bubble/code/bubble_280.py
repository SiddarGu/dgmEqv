
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as colors
import numpy as np

data_labels = ["Incidence Rate (Per 100,000 Population)", "Mortality Rate (Per 100,000 Population)", "Cost of Treatment (Billion $)", "Global Impact (Score)"]
line_labels = ["Cancer", "Diabetes", "Heart Disease", "Stroke", "Chronic Respiratory Disease", "HIV/AIDS"]
data = np.array([[400, 150, 200, 80], [100, 30, 90, 50], [140, 60, 100, 70],
       [50, 20, 80, 60], [30, 15, 30, 40], [30, 25, 50, 70]])

fig = plt.figure()
ax = fig.add_subplot()

scalar_map = cm.ScalarMappable(norm=colors.Normalize(vmin=data[:,3].min(), vmax=data[:,3].max()), cmap=cm.get_cmap('RdYlGn'))
scalar_map.set_array(data[:,3])

for i in range(len(data)):
    ax.scatter(data[i,0], data[i,1], s=600*data[i,2]/data[:,2].max(), c=scalar_map.to_rgba(data[i,3]), label=None)
    ax.scatter([], [], s=20, c=scalar_map.to_rgba(data[i,3]), label=line_labels[i]+": "+str(data[i,2]))

ax.legend(title=data_labels[2])
plt.colorbar(scalar_map, ax=ax, label=data_labels[3])

ax.set_title("Healthcare Impacts of Common Diseases Worldwide")
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.grid()

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/12_2023122270050.png')

plt.clf()