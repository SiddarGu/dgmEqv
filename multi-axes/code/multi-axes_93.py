import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker

data = np.array([
    [12100, 270000, 425, 6000],
    [25700, 350000, 800, 5000],
    [19900, 150000, 500, 4500],
    [14500, 230000, 315, 5500],
    [30000, 175000, 1100, 4800], 
    [26700, 290000, 780, 5200],
    [16000, 310000, 550, 5700],
    [9800, 500000, 350, 5900],
    [21000, 330000, 650, 6100],
    [11300, 400000, 485, 7000]
])
data_labels = ['Units Produced', 'Revenue (in 1000s)', 'Maximum Daily Output (in units)', 'Total Labor Hours']
line_labels = ['Automobiles', 'Electronics', 'Textiles', 'Furniture', 'Toys', 'Plastics', 'Chemicals', 'Pharmaceuticals', 'Metals', 'Machinery']

fig = plt.figure(figsize=(20,10))

ax1 = fig.add_subplot(111)
ax1.bar(line_labels, data[:,0], label=data_labels[0], color='b', alpha=0.5)
ax1.set_xlabel('Products')
ax1.set_ylabel(data_labels[0], color='b')

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], label=data_labels[1], color='g')
ax2.set_ylabel(data_labels[1], color='g')

ax3 = ax1.twinx()
ax3.scatter(line_labels, data[:,2], label=data_labels[2], color='r')
ax3.spines['right'].set_position(('outward', 70))
ax3.set_ylabel(data_labels[2], color='r')
      
if data.shape[1] > 3:
    ax4 = ax1.twinx()
    ax4.fill_between(line_labels, data[:,3], label=data_labels[3], color='c', alpha=0.3)
    ax4.spines['right'].set_position(('outward', 100))
    ax4.set_ylabel(data_labels[3], color='c')

ax1.xaxis.set_tick_params(rotation=45)
ax1.xaxis.label.set_visible(False)

handles1, labels1 = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
handles3, labels3 = ax3.get_legend_handles_labels()

if data.shape[1] > 3:
    handles4, labels4 = ax4.get_legend_handles_labels()
    plt.legend(handles1 + handles2 + handles3 + handles4, labels1 + labels2 + labels3 + labels4, loc='upper right')
else:
    plt.legend(handles1 + handles2 + handles3, labels1 + labels2 + labels3, loc='upper right')

    
plt.title('Manufacturing & Production: Output, Revenue and Labor Hours Analysis')
fig.tight_layout()
plt.grid(True)
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/186_202312310150.png')
plt.clf()
