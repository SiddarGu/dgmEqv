import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator

# data preparation
data_labels = ['Harvested Area (thousand hectares)', 'Production (thousand tonnes)', 'Yield (tonnes per hectare)', 'Market Value (million dollars)']
line_labels = ['Wheat', 'Corn', 'Barley', 'Oats', 'Rice', 'Soybean', 'Peanuts', 'Cotton', 'Sunflower', 'Rapeseed']

data = np.array([[21500, 75560, 3.5, 12650],
                [86800, 360000, 4.1, 20200],
                [2250, 5950, 2.6, 650],
                [1300, 3460, 2.7, 320],
                [15600, 80000, 5.1, 28400],
                [34000, 110700, 3.3, 34100],
                [550, 3500, 6.4, 976],
                [8450, 43000, 5.1, 8350],
                [5070, 11760, 2.3, 1970],
                [16400, 68000, 4.1, 15200]])

# plot initializations
fig = plt.figure(figsize=(20, 10))
ax1 = fig.add_subplot(111)
ax1.bar(line_labels, data[:, 0], color='b', alpha=0.3, label=data_labels[0])

# loop to add additional axes and plot data
colors = ['r', 'g', 'y']
factors = [0.3, 0.6, 1.2]
for i in range(1, data.shape[1]):
    axn = ax1.twinx()
    if i == 1:
        axn.plot(line_labels, data[:, i], color=colors[i-1], label=data_labels[i])
    elif i == 2:
        axn.scatter(line_labels, data[:, i], color=colors[i-1], label=data_labels[i])
    else:
        axn.fill_between(line_labels, data[:, i], 0, color=colors[i-1], alpha=0.4, label=data_labels[i])

    # setting ax positions
    if i > 1:
        axn.spines['right'].set_position(('axes', factors[i-2]))
        axn.set_frame_on(True)
        axn.patch.set_visible(False)

    axn.yaxis.label.set_color(colors[i-1])
    axn.yaxis.set_tick_params(labelcolor=colors[i-1])
    axn.xaxis.grid(True)
    axn.yaxis.set_major_locator(AutoLocator())
    axn.set_ylabel(data_labels[i])

# adding the legends    
fig.legend(loc="upper left", bbox_to_anchor=(0,1), bbox_transform=ax1.transAxes)

plt.tight_layout()
plt.title('Analysis of Crop Production: Fields, Output, Efficiency, and Revenue')
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/64_2023122292141.png')
plt.clf()
