import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap
from matplotlib.colorbar import ColorbarBase

# Transforming data
data_str = 'Disease,Incidence (Per 100K people),Mortality Rate (%),Health Spending (Billions $),Research Funding (Billions $)\n Cancer,200,20,1000,125\n Heart Disease,255,18,1200,190\n Diabetes,414,10,800,175\n Asthma,140,2,300,50\n Mental Disorders,1200,5,2000,500\n HIV/AIDS,80,32,400,300'
data_lines = data_str.split('\n')
data_labels = data_lines[0].split(',')[1:]
line_labels = [line.split(',')[0] + line.split(',')[2] for line in data_lines[1:]]

data = np.array([[float(elm) for elm in line.split(',')[1:]] for line in data_lines[1:]])
dpi = 80
fig = plt.figure(dpi = dpi, figsize = (512 / dpi, 384 / dpi) )
ax = fig.add_subplot()
cmap = get_cmap("viridis")

# creating a plot
for i, line_label in enumerate(line_labels):
    size = 600 + (data[i, 2] / data[:, 2].max()) * 3400
    color = Normalize(-min(data[:, 3]), max(data[:, 3]), clip=True)(data[i, 3])
    ax.scatter(data[i, 0], data[i, 1], cmap=cmap, label=None, s=size, c=cmap(color))
    ax.scatter([], [], c=cmap(color), label=line_label)

# adding details to graph
ax.legend(title=data_labels[2])
ax.grid(True)

fig.colorbar(plt.cm.ScalarMappable(norm=Normalize(min(data[:,3]), max(data[:,3])), cmap=cmap), ax=ax).set_label(data_labels[3])
plt.axis('equal')

ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
plt.title('Healthcare Investment and Impact on Prevalent Diseases')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/123_202312301731.png')
plt.clf()
