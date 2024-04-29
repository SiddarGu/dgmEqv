import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import host_subplot
import matplotlib.ticker as ticker

# Input data
data_labels = ["Enrollment", "Annual Tuition (Dollars)", "Acceptance Rate", "Student-Professor Ratio"]
line_labels = ["Harvard University", "Stanford University", "Columbia University", "Princeton University", "University of Chicago", "Yale University", "Johns Hopkins University", "University of Pennsylvania", "California Institute of Tech", "Duke University"]
data = np.array([[20432, 47790, 5, 7],
                 [16677, 51354, 4, 5],
                 [27882, 60928, 7, 6],
                 [8013, 47320, 6, 5],
                 [14246, 58176, 8, 5],
                 [13847, 53250, 7, 6],
                 [16618, 54020, 11, 7],
                 [21713, 57344, 9, 6],
                 [2245, 52704, 6, 3],
                 [15867, 57044, 9, 6]])

# Create figure
fig = plt.figure(figsize=(20,10))
ax1 = host_subplot(111)
ax2 = ax1.twinx()
ax3 = ax1.twinx()
ax4 = ax1.twinx()

# Plot data
line_chart, = ax1.plot(line_labels, data[:,0], label=data_labels[0])
bar_chart = ax2.bar(line_labels, data[:,1], alpha=0.6, label=data_labels[1])
scatter_chart = ax3.scatter(line_labels, data[:,2], label=data_labels[2])
line_chart2, = ax4.plot(line_labels, data[:,3], label=data_labels[3])

# set y-axis
ax2.spines['right'].set_position(('outward', 60))
ax3.spines['right'].set_position(('outward', 120))
ax4.spines['right'].set_position(('outward', 180))

ax1.yaxis.label.set_color(line_chart.get_color())
ax2.yaxis.label.set_color(bar_chart.patches[0].get_facecolor())
ax3.yaxis.label.set_color(scatter_chart.get_facecolor()[0])
ax4.yaxis.label.set_color(line_chart2.get_color())

# set labels
ax1.set_xlabel('University')
ax1.set_ylabel(data_labels[0])
ax2.set_ylabel(data_labels[1])
ax3.set_ylabel(data_labels[2])
ax4.set_ylabel(data_labels[3])

# set tick auto locator
ax1.yaxis.set_major_locator(ticker.AutoLocator())
ax2.yaxis.set_major_locator(ticker.AutoLocator())
ax3.yaxis.set_major_locator(ticker.AutoLocator())
ax4.yaxis.set_major_locator(ticker.AutoLocator())

# set legend
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
ax3.legend(loc='lower left')
ax4.legend(loc='lower right')

# set title
plt.title('Comparisons of Leading Universities in Terms of Enrollment, Tuition, Acceptance, and Student-Professor Ratio')

# set grid
ax1.grid()

# automatically adjust subplot params so that the subplot fits into the figure area
fig.tight_layout()

# save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/131_202312310108.png')

# clear the fig
plt.clf()
