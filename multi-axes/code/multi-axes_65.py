import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator
import numpy as np

# Transform data into variables
data_strings = [
    '2011,320,14,42,43',
    '2012,298,13,39,45',
    '2013,343,19,35,46',
    '2014,278,22,43,42',
    '2015,310,18,47,48',
    '2016,352,21,40,55',
    '2017,290,15,35,50',
    '2018,276,18,46,53',
    '2019,308,20,42,52',
    '2020,334,19,40,47',
]
data_labels = ['New Legislation Enacted', 'Bills Vetoed', 'Policy Changes', '% Approval']
data = np.array([list(map(int, string.split(','))) for string in data_strings])
line_labels = data[:,0]
data = data[:,1:]

# Plot data
fig = plt.figure(figsize=(18, 16))
ax1 = fig.add_subplot(111)

# Bar chart
ax1.bar(line_labels, data[:,0], color='skyblue', label=data_labels[0])
ax1.set_ylabel(data_labels[0], color='skyblue')
ax1.yaxis.set_major_locator(AutoLocator())
ax1.grid(color='lightgray', linestyle='--', linewidth=0.5)

# Line chart
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], color='orange', label=data_labels[1])
ax2.set_ylabel(data_labels[1], color='orange')
ax2.yaxis.set_major_locator(AutoLocator())

# Scatter chart
ax3 = ax1.twinx()
ax3.scatter(line_labels, data[:,2], color='green', label=data_labels[2])
ax3.set_ylabel(data_labels[2], color='green')
ax3.spines['right'].set_position(('outward', 60))  # Separate axis
ax3.yaxis.set_major_locator(AutoLocator())

# Area chart
ax4 = ax1.twinx()
ax4.fill_between(line_labels, data[:,3], color='purple', label=data_labels[3], alpha=0.5)
ax4.set_ylabel(data_labels[3], color='purple')
ax4.spines['right'].set_position(('outward', 120))  # Separate axis
ax4.yaxis.set_major_locator(AutoLocator())

# Show legends
fig.legend(loc="upper left", bbox_to_anchor=(0,1), bbox_transform=ax1.transAxes)

plt.title('Government Performance and Public Perception 2011-2020')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/117_202312310108.png')
plt.clf()
