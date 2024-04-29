import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator

data = """Department,Number of Employees,Payroll (Thousands of Dollars),Average Hours Worked Per Week,Staff Turnover Rate (%)
Human Resources,120,6000,38,12
Sales,200,10400,42,15
IT,80,4400,40,10
Marketing,150,7800,39,14
Production,300,15500,43,18
Finance,70,3600,37,8
Customer Service,250,13000,41,16
R&D,50,2600,37,7
Logistics,90,4700,38,13
Administration,100,5200,39,11"""
lines = data.split("\n")
line_labels = [line.split(",")[0] for line in lines[1:]]
data_labels = lines[0].split(",")[1:]
data_array = np.array([list(map(int, line.split(",")[1:])) for line in lines[1:]])

fig = plt.figure(figsize=(25, 10))
colors = ['b', 'g', 'r', 'c']
ax = fig.add_subplot(111)
ax.yaxis.label.set_color(colors[0])
ax.set_ylabel(data_labels[0])
ax.bar(line_labels, data_array[:,0], color=colors[0])
plt.grid()
plt.title('Human Resources and Employee Management Overview')

ax2 = ax.twinx()
ax2.plot(line_labels, data_array[:,1], color=colors[1])
ax2.yaxis.label.set_color(colors[1])
ax2.set_ylabel(data_labels[1])

if data_array.shape[1] > 2:
    ax3 = ax.twinx()
    ax3.scatter(line_labels, data_array[:,2], color=colors[2])
    ax3.yaxis.label.set_color(colors[2])
    ax3.spines['right'].set_position(('outward', 60))
    ax3.set_ylabel(data_labels[2])
    
if data_array.shape[1] > 3:
    ax4 = ax.twinx()
    ax4.fill_between(line_labels, data_array[:,3], alpha=0.5, color=colors[3])
    ax4.yaxis.label.set_color(colors[3])
    ax4.spines['right'].set_position(('outward', 120))
    ax4.set_ylabel(data_labels[3])

for axs in [ax, ax2, ax3, ax4]:
    axs.yaxis.set_major_locator(AutoLocator())

fig.legend([ax, ax2, ax3, ax4],     # The line objects
           labels=data_labels,   # The labels for each line
           loc="center right",   # Position of legend
           borderaxespad=0.1,    # Small spacing around legend box
           )
    
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/107_202312310108.png')
plt.clf()
