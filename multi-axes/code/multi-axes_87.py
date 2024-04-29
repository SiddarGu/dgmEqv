from matplotlib import pyplot as plt
import numpy as np

#Data
data_str = """Electrical Engineering,315,4900,12100,599
Chemical Engineering,180,4500,5500,450
Mechanical Engineering,400,6900,7800,640
Civil Engineering,210,5200,7100,570
Computer Science,520,7600,14200,1200
Physics,140,4200,6600,380
Chemistry,200,4800,10900,690
Biology,410,6300,15800,940
Biomedical Engineering,250,5600,12300,740
Environmental Science,290,5400,8000,330"""
data_lines = data_str.split("\n")
data_labels = ["Research Funding (Millions of Dollars)","Number of Researchers","Number of Publications","Patents Filed"]
line_labels = [line.split(",")[0] for line in data_lines]
data = np.array([list(map(int, line.split(",")[1:])) for line in data_lines])

#Plot
fig = plt.figure(figsize=(25,15))
ax1 = fig.add_subplot(111)
ax1.plot(line_labels, data[:,0], color="blue", marker="o")
ax1.set_ylabel(data_labels[0], color="blue")
ax1.tick_params(axis='y', colors="blue")

ax2 = ax1.twinx()
ax2.scatter(line_labels, data[:,1], color="green")
ax2.set_ylabel(data_labels[1], color="green")
ax2.spines['right'].set_position(('outward', 60))
ax2.yaxis.set_ticks_position('right')
ax2.yaxis.set_label_position('right')
ax2.tick_params(axis='y', colors="green")

ax3 = ax1.twinx()
ax3.bar(line_labels, data[:,2], color="red", alpha=0.5, width=0.3, align='edge')
ax3.set_ylabel(data_labels[2], color="red")
ax3.spines['right'].set_position(('outward', 120))
ax3.yaxis.set_ticks_position('right')
ax3.yaxis.set_label_position('right')
ax3.tick_params(axis='y', colors="red")

ax4 = ax1.twinx()
ax4.bar(line_labels, data[:,3], color="purple", alpha=0.5, width=-0.3, align='edge')
ax4.set_ylabel(data_labels[3], color="purple")
ax4.spines['right'].set_position(('outward', 180))
ax4.yaxis.set_ticks_position('right')
ax4.yaxis.set_label_position('right')
ax4.tick_params(axis='y', colors="purple")

plt.title('Research Trends in Science and Engineering')
plt.grid()
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/80_2023122292141.png')
plt.clf()
