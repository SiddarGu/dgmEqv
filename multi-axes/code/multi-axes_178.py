import matplotlib.pyplot as plt
import numpy as np
import textwrap

data = """
Football Match,64000,1570,50,7.85
Concert,50000,1230,55,6.80
Movie Premiere,3500,832,98,2.90
Comedy Show,8000,749,62,1.08
Baseball Game,45000,1025,40,5.13
Theater Performance,2500,617,90,1.30
Basketball Game,19000,940,70,6.70
Music Festival,70000,1532,68,10.20
Art Exhibition,1500,160,80,0.80
Racing Event,55000,1322,60,7.92 
"""

# Transforming the data
lines = data.strip().split('\n')
line_labels = [line.split(',')[0] for line in lines]
data = np.array([list(map(float, line.split(',')[1:])) for line in lines])
data_labels = ['Number of Participants', 'Ticket Sales (In Thousands)', 'Average Ticket Price (In Dollars)', 'Total Funding (In Millions)']

fig = plt.figure(figsize=(25, 10))

# Adding subplot
ax1 = fig.add_subplot(111)

# Bar chart
ax1.bar(np.arange(len(data[:, 0])), data[:, 0], color='blue', alpha=0.7, label=data_labels[0])
ax1.set_ylabel(data_labels[0], color='blue')
ax1.tick_params(axis='y', colors='blue')
ax1.set_xticks(np.arange(len(line_labels)))
ax1.set_xticklabels(line_labels, rotation=30)

# Area chart
ax2 = ax1.twinx()
ax2.fill_between(np.arange(len(data[:, 1])), 0, data[:, 1], color='green', alpha=0.5, label=data_labels[1])
ax2.set_ylabel(data_labels[1], color='green')
ax2.tick_params(axis='y', colors='green')

# Line chart
ax3 = ax1.twinx()
ax3.plot(np.arange(len(data[:, 2])), data[:, 2], color='red', alpha=0.7, label=data_labels[2])
ax3.spines['right'].set_position(('outward', 60))
ax3.set_ylabel(data_labels[2], color='red')
ax3.tick_params(axis='y', colors='red')

# Scatter chart
ax4 = ax1.twinx()
ax4.scatter(np.arange(len(data[:, 3])), data[:, 3], color='purple', alpha=0.7, label=data_labels[3])
ax4.spines['right'].set_position(('outward', 120))
ax4.set_ylabel(data_labels[3], color='purple')
ax4.tick_params(axis='y', colors='purple')

fig.legend(loc="upper left", bbox_to_anchor=(0,1), bbox_transform=ax1.transAxes)

plt.title('Analysis of Participation, Sales, and Funding for Various Sports and Entertainment Events')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/185_202312310150.png')
plt.show()
plt.close()
