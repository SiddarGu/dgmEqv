import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

# Transform data into three variables
data_labels = ['Number of Exhibitions', 'Total Revenue (Thousands)', 'Average Attendance (per Exhibition)']
line_labels = ['Picasso', 'Van Gogh', 'Dali', 'Rembrandt', 'Warhol', 'Monet', 'da Vinci', 'Michelangelo', 'Cezanne', 'Pollock']
data = np.array([[58, 2541, 425],[64, 4892, 564],[45, 3712, 313],[52, 4150, 392],[67, 5598, 638],[55, 4452, 512],[51, 3892, 412],[49, 3983, 420],[53, 4572, 466],[57, 5043, 532]])

fig = plt.figure(figsize=(24, 15))

# Plotting data[:,0] with bar chart
ax1 = fig.add_subplot(111)
ax1.bar(line_labels, data[:,0], width=0.2, color='b', alpha=0.7, label=data_labels[0])
ax1.set_ylabel(data_labels[0], color='b')
ax1.tick_params(axis='y', colors='b')

# Plotting data[:,1] with line chart
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], color='g', alpha=0.7, label=data_labels[1])
ax2.set_ylabel(data_labels[1], color='g')
ax2.tick_params(axis='y', colors='g')

# Plotting data[:,2] with scatter chart
ax3 = ax1.twinx()
ax3.scatter(line_labels, data[:,2], color='r', alpha=0.7, label=data_labels[2])
ax3.spines['right'].set_position(('outward', 60))
ax3.set_ylabel(data_labels[2], color='r')
ax3.tick_params(axis='y', colors='r')
ax3.yaxis.set_major_locator(ticker.AutoLocator())

plt.title('Overview of Performance in Art Exhibitions')

fig.legend(loc="upper left", bbox_to_anchor=(0,1), bbox_transform=ax1.transAxes)

plt.grid(True)

plt.tight_layout()

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/177_202312310150.png')

plt.clf()
