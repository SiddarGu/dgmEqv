import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator
import numpy as np

# Transform data to Python objects
data_str = "Department,Number of Employees,Turnover Rate (%),Average Salary ($),Gender Diversity Ratio (Fe:Ma)\
\n HR,50,15,60000,1.2\n Sales,200,25,75000,0.8\n Marketing,100,20,65000,1.0\
\n IT,150,10,85000,0.6\n Finance,75,12,70000,0.9\n Operations,300,30,55000,0.7\
\n Product,120,18,80000,1.1"
data_str = data_str.split("\n")
data = np.array([row.split(",")[1:] for row in data_str[1:]]).astype(float)
data_labels = data_str[0].split(",")[1:]
line_labels = [row.split(",")[0] for row in data_str[1:]]

# Create figure and add subplot
plt.figure(figsize=(22,16))
ax1 = plt.subplot(111)
ax1.bar(line_labels, data[:,0], alpha=0.6, color='r', label=data_labels[0])
ax1.set_ylabel(data_labels[0], color = 'r')

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], color='b')
ax2.set_ylabel(data_labels[1], color='b')

ax3 = ax1.twinx()
ax3.scatter(line_labels, data[:,2], color='g')
ax3.set_ylabel(data_labels[2], color='g')
ax3.spines["right"].set_position(("axes", 1.1))

ax4 = ax1.twinx()
ax4.bar(line_labels, data[:,3], alpha=0.6, color='y', label=data_labels[3])
ax4.set_ylabel(data_labels[3], color='y')
ax4.spines["right"].set_position(("axes", 1.2))

ax1.legend(loc='upper left')
ax4.legend(loc='upper right')

ax1.yaxis.set_major_locator(AutoLocator())
ax2.yaxis.set_major_locator(AutoLocator())
ax3.yaxis.set_major_locator(AutoLocator())
ax4.yaxis.set_major_locator(AutoLocator())

plt.grid(True)
plt.title('Employee Statistics and Diversity in Different Departments')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/105_202312310108.png')
plt.close()
