import matplotlib.pyplot as plt
import numpy as np

# transform the given data into three variables
data_labels = ["Units Sold", "Revenue (Thousands of Dollars)", "Average of Online Reviews / 5"]
line_labels = ["Shirts", "Jeans", "Jackets", "Shoes", "Bags", "Suits", "Belts", "Caps", "Sunglasses", "Gloves", "Watches", "Scarves"]
data = np.array([
    [3720, 740, 4.2],
    [2580, 1902, 4.5],
    [1366, 2049, 3.9],
    [4112, 3074, 4.3],
    [2298, 2197, 4.6],
    [2096, 2531, 4.1],
    [2981, 1192, 3.8],
    [3282, 985, 4.0],
    [3849, 1154, 4.4],
    [2289, 572, 4.1],
    [2796, 8952, 4.7],
    [1859, 405, 4.3]
])

# Set colors for the chart
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

fig = plt.figure(figsize=(30,15))
ax1 = fig.add_subplot(111)
ax1.bar(line_labels, data[:,0], color=colors[0], alpha=0.7)
ax1.set_ylabel(data_labels[0])
ax1.yaxis.label.set_color(colors[0])

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], color=colors[1])
ax2.set_ylabel(data_labels[1])
ax2.yaxis.label.set_color(colors[1])

if data.shape[1] > 2:  # if there is third y-axis
    ax3 = ax1.twinx()
    ax3.scatter(line_labels, data[:,2], color=colors[2])
    ax3.set_ylabel(data_labels[2])
    ax3.yaxis.label.set_color(colors[2])
    ax3.spines['right'].set_position(('outward', 60))

plt.title('E-Commerce Sales Overview, Unit and Revenue Metrics with Average Review Scores')
fig.legend([ax1, ax2, ax3],     
           labels=data_labels,   
           loc="center right",   
           borderaxespad=0.1,    
           title="Legend"  
           )

fig.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/259_202312311051.png')
plt.cla()
plt.clf()
plt.close()
