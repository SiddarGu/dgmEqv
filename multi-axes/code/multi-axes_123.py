import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator

# Input data
input_data = [
    ["Performing Arts",250,3.5,75],
    ["Visual Arts",270,2.1,200],
    ["History and Heritage",135,1.2,150],
    ["Science and Technology",185,2.5,100],
    ["Natural History and Natural Science",150,1.5,250],
    ["Zoo, Aquaria and Aviaries",180,3.2,50],
    ["Children and Youth",200,4.0,70],
    ["Film and Media",220,2.6,180],
    ["Humanities",130,1.4,160],
    ["Library and Museum related",250,3.2,200],
    ["Culturally Specific",100,0.8,210]]

# Transform data
data_labels = ['Total Funding (Millions)', 'Total Attendance (Millions)', 'Average Donation (Dollars)']
line_labels = [row[0] for row in input_data]
data = np.array([row[1:] for row in input_data])

# Plot
fig = plt.figure(figsize=(20, 10))
ax1 = fig.add_subplot(111)
ax1.bar(line_labels, data[:,0], color='b',alpha=0.7, label=data_labels[0] )
ax1.legend(loc='upper left', fontsize=12)
ax1.set_ylabel(data_labels[0])
ax1.yaxis.label.set_color('b')
ax1.set_ylim([0, 300])

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], color='r', label=data_labels[1] )
ax2.legend(loc='upper center', fontsize=12)
ax2.set_ylabel(data_labels[1])
ax2.yaxis.label.set_color('r')
ax2.set_ylim([0, 5])

ax3 = ax1.twinx()
ax3.scatter(line_labels, data[:,2], color='g', label=data_labels[2])
ax3.spines['right'].set_position(('outward', 60))      
ax3.set_ylabel(data_labels[2])
ax3.yaxis.label.set_color('g')
ax3.legend(loc='upper right', fontsize=12)
ax3.set_ylim([0, 260])

# Auto adjust the y-axes
for ax in [ax1, ax2, ax3]:
    ax.yaxis.set_major_locator(AutoLocator())

plt.grid(True)
plt.title('A Comprehensive Overview of Arts and Culture Funding, Attendance and Donation')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/114_202312310108.png')
plt.clf()

