import matplotlib.pyplot as plt
import numpy as np

# parse data

data_all = '''Year,Number of Graduates (Thousands),Employment Rate (%),Average Starting Salary (Dollars)/n
2010,350,76,50000/n
2011,365,78,51000/n
2012,380,80,52000/n
2013,390,81,53000/n
2014,410,80,54000/n
2015,420,82,55000/n
2016,430,83,56000/n
2017,440,84,57000/n
2018,450,85,58000/n
2019,460,86,59000/n
2020,470,81,60000'''.split('/n')

line_labels = [line.split(',')[0] for line in data_all[1:]]
data_labels = data_all[0].split(',')[1:]
data = np.array([list(map(int, line.split(',')[1:])) for line in data_all[1:]])

# create figure

plt.figure(figsize=(20, 10))

# create primary axis
ax1 = plt.subplot(111)
ax1.plot(line_labels, data[:,0], label=data_labels[0], color='tab:blue')
ax1.set_xlabel("Year")
ax1.set_ylabel(data_labels[0], color='tab:blue')

# create secondary axis
ax2 = ax1.twinx()
ax2.bar(line_labels, data[:,1], label=data_labels[1], color='tab:orange', alpha=0.6)
ax2.set_ylabel(data_labels[1], color='tab:orange')

# create tertiary axis
ax3 = ax1.twinx()
ax3.plot(line_labels, data[:,2], label=data_labels[2], color='tab:green')

# Spines and position manipulation for third axis 
ax3.spines['right'].set_position(('outward', 60))  
ax3.set_ylabel(data_labels[2], color='tab:green')

# Adding legends for all lines
ax1.legend(loc="upper left")
ax2.legend(loc="upper center")
ax3.legend(loc="upper right")

plt.title("Yearly Trends in Education: Graduate Numbers, Employment, and Salaries")

# add grid
plt.grid()

# Show the plot
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/130_202312310108.png")
plt.cla()
