import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from matplotlib.colors import Normalize
import csv
import matplotlib.ticker as mticker

data_labels = ['Energy Generation (GWh)', 'Number of Customers (Millions)', 'Profit ($ Billion)', 'Environmental Impact (Score)']
data_text = """EDF Energy,650,10,5,7.5
Enel,890,15,7,8
Duke Energy,400,9,4.3,6.7
Dominion Energy,320,7,3.5,7.3
Exelon,500,8,4.8,7
Southern Company,450,10,5.2,7.9
NextEra Energy,900,11,8,8.5"""
reader = csv.reader(data_text.split("\n"), delimiter=',')
data = None
line_labels = []
for row in reader:
    line_labels.append(row[0] + " " + str(row[3]))
    array = np.array([float(x) for x in row[1:]])
    if data is not None:
        data = np.vstack([data, array])
    else:
        data = array
color_norm = Normalize(data[:, 3].min(), data[:, 3].max())
cmap = cm.get_cmap('Spectral')
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(1, 1, 1)
for i, line_label in enumerate(line_labels):
    bubble_sizes = Normalize(data[:, 2].min(), data[:, 2].max())(data[:, 2])*4400 + 600
    colors = cmap(color_norm(data[:, 3]))
    ax.scatter(data[i, 0], data[i, 1], s=bubble_sizes[i], c=colors[i:i+1, :], label=None)
    ax.scatter([], [], c=colors[i:i+1, :], label=line_label)
plt.gca().xaxis.set_major_formatter(mticker.StrMethodFormatter('{x:,.0f}'))
plt.gca().yaxis.set_major_formatter(mticker.StrMethodFormatter('{x:,.0f}'))
ax.legend(title=data_labels[2])
sm = cm.ScalarMappable(cmap=cmap, norm=Normalize(min(data[:, 3]), max(data[:, 3])))
sm.set_array([])
plt.colorbar(sm, label=data_labels[3])
plt.grid(True)
plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])
plt.title('Profit and Environmental Impact of Major Energy Companies')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/275_202312310045.png')
plt.cla()
plt.clf()
plt.close()
