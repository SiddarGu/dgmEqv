
import matplotlib.pyplot as plt
import numpy as np

# transform data into 3 variables
data_labels = ["Sale (Dollars)", "Average of State Bottle Retail", "Bottles Sold"]
line_labels = ["Beer", "Wine", "Spirits", "Soft Drinks", "Water", "Dairy", "Juices"]
data = np.array([[150,3000,40,200], [200,4000,30,400], [300,6000,20,600], [200,3000,50,400], [100,2000,60,200], [200,3000,30,400], [150,2500,40,300]])

# create figure and plot
fig = plt.figure(figsize=(15, 10))
ax1 = fig.add_subplot(111)
ax1.bar(line_labels, data[:, 0], alpha=0.5, label=data_labels[0])
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:, 1], 'r-', label=data_labels[1])
ax3 = ax1.twinx()
ax3.spines['right'].set_position(('axes', 1.1))
ax3.plot(line_labels, data[:, 2], 'g-', label=data_labels[2])

# label axes and show legend
ax1.set_xlabel("Category")
ax1.set_ylabel(data_labels[0], color="b")
ax2.set_ylabel(data_labels[1], color="r")
ax3.set_ylabel(data_labels[2], color="g")
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
ax3.legend(loc='lower right')

# drawing techniques
ax1.grid(True)

# adjust the range
ax1.xaxis.set_ticks(np.arange(len(line_labels)) + 0.4)
ax1.set_xticklabels(line_labels)
ax1.autoscale_view(tight=True, scalex=True, scaley=True)

# save image
plt.title("Food and Beverage Industry Consumption Trends")
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/46_2023122261325.png")

plt.clf()