import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoLocator

# Transforming data into correct format
data = np.array([
    [4570,1725,5.4,12],
    [5012,1870,5.6,14],
    [5793,2040,5.8,15],
    [6205,2235,6.1,16],
    [6333,2370,6.3,17],
    [6890,2555,6.5,20]
])
data_labels = ['Number of Cases Litigated', 'Attorney Fees (Millions)', 
               'Average Trial Length (Days)', 'Decisions Reversed (Percent)']
line_labels = [2016, 2017, 2018, 2019, 2020, 2021]

# Create figure
fig = plt.figure(figsize=(20,15))
ax1 = fig.add_subplot(111)
colors = ['r', 'g', 'b', 'm']

# Creating plots
for i in range(data.shape[1]):
    if i==0:  # line plot 
        ax1.plot(line_labels, data[:, i], color = colors[i])
    elif i==1:  # bar plot 
        ax2 = ax1.twinx()
        ax2.bar(np.array(line_labels)-(0.1*(i-1)), data[:, i], alpha=0.5, color = colors[i], width=0.2)
    elif i==2:  # scatter plot 
        ax3 = ax1.twinx()
        ax3.scatter(line_labels, data[:, i], color = colors[i])
        ax3.spines['right'].set_position(('outward', 60))
    else:  # area plot 
        ax4 = ax1.twinx()
        ax4.fill_between(line_labels, data[:, i], color=colors[i], alpha=0.3)
        ax4.spines['right'].set_position(('outward', 120))

# Setting autolocator and aligning y-axes
for ax in [ax1, ax2, ax3, ax4]:
    ax.yaxis.set_major_locator(AutoLocator())
    ax.yaxis.label.set_color(colors[i])
    ax.tick_params(axis='y', colors=colors[i])

# Adding labels and title
ax1.set_xlabel('Year', fontsize=16)
ax1.set_ylabel(data_labels[0], color=colors[0])
ax2.set_ylabel(data_labels[1], color=colors[1])
ax3.set_ylabel(data_labels[2], color=colors[2])
ax4.set_ylabel(data_labels[3], color=colors[3])
plt.title('Legal Affairs Trend Analysis: Litigated Cases, Attorney Fees, and Case Lengths', fontsize=18)

# Adding legends at different locations
ax1.legend([data_labels[0]], loc='upper left')
ax2.legend([data_labels[1]], loc='lower right')
ax3.legend([data_labels[2]], loc='upper right')
ax4.legend([data_labels[3]], loc='lower left')

# Grid, tight layout, and savefig 
plt.grid()
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/65_2023122292141.png')

# Clear plot for next plot
plt.clf()
