import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoLocator

# Use the given data
data_str = '''General Medicine,1500,8,5,4
Pediatrics,500,5,3,5
Oncology,300,10,7,3
Cardiology,1000,12,6,2
Neurology,800,15,8,4
Orthopedics,700,18,10,3
Obstetrics,400,6,2,5
Psychiatry,200,4,3,4
Dermatology,600,7,4,4
Ophthalmology,500,9,5,3'''

# Transform the given data into three variables: data_labels, data, line_labels
lines = data_str.split('\n')
data_labels = ['Number of Patients', 'Treatment Cost (Millions of Dollars)', 'Average Hospital Stay (Days)', 'Hospital Rating']
line_labels = [line.split(',')[0] for line in lines]
data = np.array([list(map(int, line.split(',')[1:])) for line in lines])

fig = plt.figure(figsize=(25, 10))
ax1 = fig.add_subplot(111)
ax1.bar(line_labels, data[:,0], color='b', alpha=0.6, label=data_labels[0])
ax1.set_ylabel(data_labels[0], color='b')
for t in ax1.get_yticklabels():
    t.set_color('b')

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], 'g-', label=data_labels[1])
ax2.set_ylabel(data_labels[1], color='g')
for t in ax2.get_yticklabels():
    t.set_color('g')

ax3 = ax1.twinx()
ax3.scatter(line_labels, data[:,2], color='r', label=data_labels[2])
ax3.set_ylabel(data_labels[2], color='r')
for t in ax3.get_yticklabels():
    t.set_color('r')
ax3.spines['right'].set_position(('outward', 60))
    
if data.shape[1] > 3:
    ax4 = ax1.twinx()
    ax4.fill_between(line_labels, data[:,3], color='c', alpha=0.4, label=data_labels[3])
    ax4.set_ylabel(data_labels[3], color='c')
    for t in ax4.get_yticklabels():
        t.set_color('c')
    ax4.spines['right'].set_position(('outward', 120))

# Set the title and turn on the grid
plt.title('Healthcare Performance Analysis: Patient Count, Cost, and Quality Indicators', fontsize=20)
plt.grid(True)

# set up autolocators for all ax
ax1.yaxis.set_major_locator(AutoLocator())
ax2.yaxis.set_major_locator(AutoLocator())
ax3.yaxis.set_major_locator(AutoLocator())
if data.shape[1] > 3:
    ax4.yaxis.set_major_locator(AutoLocator())

plt.tight_layout()

# Show the legends at different positions
ax1.legend(loc="upper left")
ax2.legend(loc="upper right")
ax3.legend(loc="lower left")
if data.shape[1] > 3:
    ax4.legend(loc="lower right")

# Save the figure and clear the image 
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/277_202312311430.png')
plt.cla()
plt.close(fig)
