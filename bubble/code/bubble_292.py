import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

#Transform the given data into three variables: data_labels, data, line_labels.
data_raw='''
Law Firm,Number of Cases Handled (annual),Client's Satisfaction Rate (%),Revenue (Million $),Global Impact Score
Baker McKenzie,100,80,27,75
DLA Piper,90,85,25,70
Clifford Chance,95,90,30,80
Latham & Watkins,85,85,29,77
Skadden Arps Slate,85,88,32,82
White & Case,90,83,28,79 
Kirkland & Ellis,100,90,35,85
Jones Day,95,87,31,80
Gibson Dunn,90,88,30,78
Morrison & Foerster,85,82,26,73
'''
data_raw_rows = data_raw.strip().split('\n')
data_labels = data_raw_rows[0].split(',')[1:]
data = np.array([row.split(',')[1:] for row in data_raw_rows[1:]], dtype=float)
line_labels = [f'{row.split(",")[0]} {row.split(",")[2]}%' for row in data_raw_rows[1:]]

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)

#Normalize colors
color = data[:,3]
normalize = colors.Normalize(vmin=min(color), vmax=max(color))
colormap = plt.get_cmap("viridis")

for i in range(len(data)):
    ax.scatter(data[i, 0], data[i, 1], label=None, c=colormap(normalize(color[i])), s=(data[i,2]*100), alpha=0.6, edgecolors='black')
    ax.scatter([], [], c=colormap(normalize(color[i])), alpha=0.6, s=20, label=line_labels[i])

ax.legend(title=data_labels[2])
plt.colorbar(plt.cm.ScalarMappable(norm=normalize, cmap=colormap),label=data_labels[3])

plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])
plt.title('Law Firms Efficiency Comparison regarding Cases Handled, Client Satisfaction and Revenue')

# to display all content
plt.tight_layout()

# save the plot to the absolute path
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/228_202312310045.png')
plt.clf()
