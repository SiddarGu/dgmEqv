import matplotlib.pyplot as plt
import numpy as np

data = """Category,Total Revenue (Millions),Operating Cost (Millions),Net Profit (Millions)
Retail,1850,1600,250
Banking,2800,1700,1100
Media,2300,1800,500
Energy,3500,1900,1600
Healthcare,4500,2500,2000
Manufacturing,3000,2400,600
Technology,4350,3200,1150
Entertainment,3580,2300,1280
Real Estate,4000,3000,1000
Insurance,3270,2700,570"""
lines = data.splitlines()
line_labels = [line.split(",")[0] for line in lines[1:]]
data = np.array([[int(num) for num in line.split(",")[1:]] for line in lines[1:]])
data_labels = lines[0].split(",")[1:]

fig = plt.figure(figsize=(22,10))
ax1 = fig.add_subplot(111)
ax1.bar(line_labels, data[:,0], label=data_labels[0])
ax1.set_ylabel(data_labels[0])
ax1.grid(True)
ax1.autoscale(axis='both',tight=True)

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], color='g', label=data_labels[1])
ax2.set_ylabel(data_labels[1], color='g')

ax3 = ax1.twinx()
ax3.scatter(line_labels, data[:,2], color='b', label=data_labels[2])
ax3.spines['right'].set_position(('outward', 60))
ax3.set_ylabel(data_labels[2], color='b')
ax3.set_ylim(bottom=0)
ax3.grid(True)

ax1.set_xlabel("Business Categories")
fig.suptitle("A Comparative Analysis of Revenue, Operating Cost and Net Profit Across Different Business Categories")

fig.legend(loc="upper left", bbox_to_anchor=(0,1), bbox_transform=ax1.transAxes)

plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/208_202312311051.png")
plt.clf()

