import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

# define data
data_labels = ["Undergraduate Enrollment (thousands)", "Graduate Enrollment (thousands)", "Percentage of Male Students", "Percentage of Female Students"]
line_labels = ["2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020"]
data = np.array([[16745,2737,43.2,56.8],[16849,2789,42.5,57.5],[16912,2899,44.8,55.2],[17009,2945,43.8,56.2],[17248,3027,45.1,54.9],[17681,3094,46.7,53.3],[17874,3141,48.9,51.1],[18012,3204,50.3,49.7],[18748,3283,51.2,48.8],[19065,3345,52.5,47.5]])

colors = ['b', 'r', 'g', 'y']
# create the figure
fig = plt.figure(figsize=[15,10])
ax = fig.add_subplot(111)
ax2, ax3, ax4 = [ax.twinx() for _ in range(3)]
ax_list = [ax, ax2, ax3, ax4]
fig.subplots_adjust(right=0.75)
ax3.spines['right'].set_position(('outward', 60))
ax4.spines['right'].set_position(('outward', 120))
# plot data
for i, ax in enumerate(ax_list):
    if i<2: 
        ax.plot(line_labels, data[:,i], color=colors[i], label=data_labels[i])
    else:
        ax.bar(line_labels, data[:,i], color=colors[i], label=data_labels[i], alpha=0.5, align='center')
    ax.set_ylabel(data_labels[i], color=colors[i])
    ax.tick_params(axis='y', colors=colors[i])
ax.set_xlabel('Year')
plt.title('Trends in Higher Education: Enrollment and Gender Distribution')
handles, labels = [], []
for ax in ax_list:
    for h, l in zip(*ax.get_legend_handles_labels()):
        handles.append(h)
        labels.append(l)
plt.legend(handles, labels, loc=2, bbox_to_anchor=(1.05,1))
ax.yaxis.set_minor_locator(AutoMinorLocator())
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/108_202312310108.png", dpi=300)
plt.close(fig)
