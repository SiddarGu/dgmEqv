import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator

# Data
data_labels = ["Number of Students", "Number of Teachers", "Expenditure per Student", "Average Class Size"]
line_labels = ["Preschool", "Elementary School", "Middle School", "High School", "College", "University", "Academic Program", "Research Institute", "Educational Administration"]
data = np.array([
    [200,15,5000,10],
    [500,30,6000,20],
    [400,25,7000,25],
    [600,40,8000,30],
    [1000,50,10000,40],
    [2000,100,15000,50],
    [3000,200,20000,60],
    [500,50,25000,70],
    [200,20,30000,80],
])

# Plotting
fig = plt.figure(figsize=(25, 10))
ax1 = fig.add_subplot(111)
ax1.bar(line_labels, data[:,0], color='blue', label=data_labels[0])
ax1.set_ylabel(data_labels[0], color='blue')
ax1.tick_params(axis='y', colors='blue')

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], color='green', label=data_labels[1])
ax2.set_ylabel(data_labels[1], color='green')
ax2.tick_params(axis='y', colors='green')

ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60))
ax3.plot(line_labels, data[:,2], color='red', label=data_labels[2])
ax3.set_ylabel(data_labels[2], color='red')
ax3.tick_params(axis='y', colors='red')

ax4 = ax1.twinx()
ax4.spines['right'].set_position(('outward', 120))
ax4.plot(line_labels, data[:,3], color='purple', label=data_labels[3])
ax4.set_ylabel(data_labels[3], color='purple')
ax4.tick_params(axis='y', colors='purple')

fig.legend(loc="upper left", bbox_to_anchor=[0, 1],
           bbox_transform=fig.transFigure, ncol=4)

plt.gca().xaxis.set_major_locator(AutoLocator())
plt.gca().yaxis.set_major_locator(AutoLocator())

plt.title("Education and Academics: Overview of Student Enrollment, Faculty Size, Expenditure, and Class Sizes")
plt.grid(True)
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/323_202312311430.png")
plt.clf()
