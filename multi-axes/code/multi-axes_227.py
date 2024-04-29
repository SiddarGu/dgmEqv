import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Donations Received (Millions)', 'Volunteers (Thousands)', 'Programs Launched']
line_labels = ['2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
data = np.array([
    [200, 300, 50],
    [220, 320, 55],
    [230, 350, 60],
    [250, 400, 70],
    [270, 450, 80],
    [300, 500, 90],
    [320, 550, 100],
    [340, 600, 110],
    [360, 650, 120],
    [400, 700, 130]
])

fig = plt.figure(figsize=(20,10)) 
ax1 = fig.add_subplot(111) 

ax1.plot(line_labels, data[:, 0], color='b', label=data_labels[0]) 
ax1.set_ylabel(data_labels[0], color='b')
ax1.set_xlabel('Year')

ax2 = ax1.twinx()  
ax2.plot(line_labels, data[:, 1], color='g', label=data_labels[1]) 
ax2.set_ylabel(data_labels[1], color='g')

ax3 = ax1.twinx()  
ax3.spines['right'].set_position(('outward', 60)) 
ax3.bar(line_labels, data[:, 2], color='r', label=data_labels[2], alpha=0.5)
ax3.set_ylabel(data_labels[2], color='r')

fig.legend(loc="upper left")

plt.title('Trends in Charitable Contributions, Volunteer Participation, and Program Launches')

fig.tight_layout()  

plt.grid()

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/220_202312311051.png')

plt.cla()
plt.clf()
