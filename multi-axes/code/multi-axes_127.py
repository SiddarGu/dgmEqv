import matplotlib.pyplot as plt
import numpy as np

# Transform the data into three variables
data_labels = ['Year', 'Wheat Production (Million Tons)', 'Rice Production (Million Tons)', 
               'Maize Production (Million Tons)', 'Soybean Production (Million Tons)', 'Oats Production (Million Tons)']
line_labels = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
data = np.array([[704, 745, 913, 251, 23],
                 [694, 758, 877, 268, 21],
                 [711, 769, 1021, 276, 23],
                 [729, 772, 1044, 314, 22],
                 [734, 767, 971, 321, 24],
                 [749, 795, 1068, 333, 23],
                 [763, 809, 1105, 341, 25],
                 [782, 823, 1133, 358, 27],
                 [796, 833, 1141, 369, 27],
                 [811, 848, 1173, 382, 28]])

fig = plt.figure(figsize=(15, 10))
ax1 = fig.add_subplot(111)

colors = ['r', 'g', 'b', 'y', 'black']
for i in range(data.shape[1]):
    if i == 0:
        ax = ax1
    else:
        ax = ax1.twinx()
        ax.spines['right'].set_position(('outward', 60*(i-1)))

    ax.plot(line_labels, data[:, i], label=data_labels[i+1], color=colors[i])
    ax.set_ylabel(data_labels[i+1])
    ax.yaxis.label.set_color(colors[i])
    ax.tick_params(axis='y', colors=colors[i])
    ax.xaxis.grid(True, which='both')
    ax.yaxis.grid(True, which='both')

plt.autoscale()
plt.legend(loc='upper left')
plt.title('A decade of Global Production Trends in Major Crops')
plt.tight_layout()

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/143_202312310108.png')
plt.clf()
