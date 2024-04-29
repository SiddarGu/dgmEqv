import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Data preparation
data_str = "Category,Number of Products Sold,Total Sales Revenue (USD),Average Price per Product,Number of Customers\n\
            Clothing,3500,157500,45,800\nElectronics,2500,500000,200,600\n\
            Home Decor,2000,80000,40,400\nBeauty and Personal Care,3000,150000,50,700\n\
            Sports and Fitness,1000,100000,100,300\nBooks and Media,1500,50000,33.33,200"
data_lines = data_str.split('\n')
data_labels = data_lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in data_lines[1:]]
data = np.array([line.split(',')[1:] for line in data_lines[1:]], dtype=float)

# Figure creation
fig = plt.figure(figsize=(15, 10))
ax1 = fig.add_subplot(111)

# Plotting data
colors = ['r', 'g', 'b', 'y', 'm']

# Bar chart
ax1.bar(line_labels, data[:,0], color=colors[0], alpha=0.75)
ax1.set_ylabel(data_labels[0], color=colors[0])
ax1.yaxis.set_major_locator(ticker.AutoLocator())

# Line chart
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], color=colors[1])
ax2.set_ylabel(data_labels[1], color=colors[1])
ax2.yaxis.set_major_locator(ticker.AutoLocator())

# Scatter chart
ax3 = ax1.twinx()
ax3.scatter(line_labels, data[:,2], color=colors[2])
ax3.set_ylabel(data_labels[2], color=colors[2])
ax3.spines['right'].set_position(('outward', 60))
ax3.yaxis.set_major_locator(ticker.AutoLocator())

# Area chart
if data.shape[1]>3:
    ax4 = ax1.twinx()
    ax4.fill_between(line_labels, data[:,3], color=colors[3], alpha=0.5)
    ax4.set_ylabel(data_labels[3], color=colors[3])
    ax4.spines['right'].set_position(('outward', 120))
    ax4.yaxis.set_major_locator(ticker.AutoLocator())

plt.grid()

# Legends
ax1.legend([data_labels[0]], loc='upper left')
ax2.legend([data_labels[1]], loc='upper right')
ax3.legend([data_labels[2]], loc='center left')
if data.shape[1]>3: ax4.legend([data_labels[3]], loc='center right')

plt.title('Retail and E-commerce Sales Analysis: Product Sales, Revenue, and Pricing Trends')
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/291_202312311430.png")
plt.clf()
