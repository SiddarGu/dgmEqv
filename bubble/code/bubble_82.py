import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap

data = """Cars,60,200,20,90
Skateboards,70,150,25,85
Motorcycles,50,180,22,88
Bicycles,80,120,27,92
Trucks,40,220,19,89
Electronic Gadgets,100,200,30,95"""
data_labels = ['Product', 'Production Volume (Million Units)', 'Operating Cost (Million $)', 'Profit Margin (%)', 'Quality Assurance (Score)']

# transform data into numpy array
data = [i.split(',') for i in data.split('\n')]
product, volume, cost, margin, quality = zip(*data)
volume = list(map(int, volume))
cost = list(map(int, cost))
margin = list(map(int, margin))
quality = list(map(int, quality))

data = np.array(list(zip(volume, cost, margin, quality)))

# labels
line_labels = [f'{product[i]} {data[i,2]}' for i in range(len(product))]

fig, ax = plt.subplots(figsize=(10,7))
# colors
norm = Normalize(data[:,3].min(), data[:,3].max())
colors = get_cmap('viridis')(norm(data[:,3]))

# plot data with scatter
for i in range(data.shape[0]):
    ax.scatter(data[i, 0], data[i, 1], label=None,
               c=colors[i], alpha=0.6, edgecolors='w', 
               s=600+4000*(data[i,2]-data[:,2].min())/data[:,2].ptp())
    ax.scatter([], [], c=colors[i], alpha=0.6, edgecolors='w',
               label=line_labels[i])

# adding title and labels    
ax.set_xlabel(data_labels[1])
ax.set_ylabel(data_labels[2] )
ax.legend(title=data_labels[2])
plt.title('Profitability and Quality Assurance in Different Product Manufacturing')

# adding color bar
sm = plt.cm.ScalarMappable(cmap=get_cmap('viridis'), norm=Normalize(vmin=data[:,3].min(), vmax=data[:,3].max()))
sm.set_array([])
fig.colorbar(sm, ax=ax, label=data_labels[3])

plt.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/300_202312310045.png')
plt.clf()
