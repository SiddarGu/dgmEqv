import matplotlib.pyplot as plt
import numpy as np

# Prepare the data
data_raw = """Region,Number of Tourists (Millions),Revenue (Billions of USD),Average Length of Stay (Days),Average Spend per Day (USD)
Asia,343,1021,8,90
North America,215,941,6,115
Europe,515,682,10,78
Africa,67,180,14,50
Oceania,67,134,12,110
South America,47,112,10,60
Central America,30,75,9,70
Caribbean,25,61,7,80"""
lines = data_raw.split("\n")
data_labels = lines[0].split(",")[1:]
line_labels = [line.split(",")[0] for line in lines[1:]]
data = np.array([[float(num) for num in line.split(",")[1:]] for line in lines[1:]])

# Create figure
fig = plt.figure(figsize=(30, 10))

# First plot (Bar chart)
ax1 = fig.add_subplot(111)
ax1.bar(line_labels, data[:, 0], color='b', alpha=0.7, label=data_labels[0])
ax1.set_ylabel(data_labels[0], color='b')
ax1.tick_params('y', colors='b')

# Second plot (Line chart)
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:, 1], color='r', label=data_labels[1])
ax2.set_ylabel(data_labels[1], color='r')
ax2.tick_params('y', colors='r')

# Third plot (Line chart)
ax3 = ax2.twinx()
ax3.plot(line_labels, data[:, 2], color='g', label=data_labels[2])
ax3.set_ylabel(data_labels[2], color='g')
ax3.spines['right'].set_position(('outward', 60))

# Fourth plot (Scatter chart)
ax4 = ax3.twinx()
ax4.scatter(line_labels, data[:, 3], color='c', label=data_labels[3])
ax4.set_ylabel(data_labels[3], color='c')
ax3.tick_params('y', colors='c')
ax4.spines['right'].set_position(('outward', 120))

# Format and show
plt.grid(True)
plt.title('Overview of Global Tourism Statistics: Tourist Numbers, Revenue, and Spending Habits')

# Set legend
fig.legend(loc="upper left", bbox_to_anchor=(0,1), bbox_transform=ax1.transAxes)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/248_202312311051.png')
plt.close(fig)
