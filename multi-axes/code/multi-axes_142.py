import matplotlib.pyplot as plt
import numpy as np

# Given data
data_labels = ["Number of Students", "School Dropouts (%)", "Average Score"]
line_labels = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
data = np.array([[6900, 3.65, 85.25], [7100, 3.37, 86.10], [7600, 3.24, 87.40], 
                 [7800, 3.15, 88.20], [8100, 2.96, 88.93], [8300, 2.85, 89.70], 
                 [8750, 2.73, 90.10], [9000, 2.65, 91.00], [9300, 2.56, 91.70], 
                 [9600, 2.47, 92.20], [9900, 2.38, 92.83]])

# Define color for each y-axis
color_iter = iter(plt.get_cmap('tab10').colors)

fig, ax1 = plt.subplots(figsize=(20,10))

ax1.plot(line_labels, data[:,0], color=next(color_iter), label=data_labels[0])
ax1.set_ylabel(data_labels[0], color=next(color_iter))
ax1.tick_params(axis='y', labelcolor=next(color_iter))

ax2 = ax1.twinx()
ax2.fill_between(line_labels, 0, data[:,1], alpha=0.5, color=next(color_iter), label=data_labels[1])
ax2.set_ylabel(data_labels[1], color=next(color_iter))
ax2.tick_params(axis='y', labelcolor=next(color_iter))

ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60)) # to move the 2nd y-axis further right
ax3.plot(line_labels, data[:,2], color=next(color_iter), label=data_labels[2])
ax3.set_ylabel(data_labels[2], color=next(color_iter))
ax3.tick_params(axis='y', labelcolor=next(color_iter))

plt.grid()
ax1.set_title('Education Statistics: Student Numbers, Dropout Rates, and Average Scores Over a Decade')
fig.legend(loc='upper left')
ax1.xaxis.set_major_locator(plt.MultipleLocator(1))
fig.tight_layout()

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/255_202312311051.png')

plt.close(fig)
