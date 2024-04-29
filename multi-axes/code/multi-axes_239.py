import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Median Home Price (Thousands of Dollars)', 'Inventory (Number of Homes)', 'Average Mortgage Interest Rate', 'Median Rent Price']
line_labels = ['Single Family Homes', 'Condominiums', 'Multi-family Homes', 'Townhomes', 'Vacation Homes', 'Luxury Homes']
data = np.array([[250,1000,3,1500],[200,500,3.5,1200],[300,800,4,1800],[220,600,3.8,1300],[400,300,4.5,2000],[800,200,5,3000]])

fig = plt.figure(figsize=(15,10))
ax1 = fig.add_subplot(111)

N = len(data)
ind = np.arange(N) 
width = 0.4       

ax1.bar(ind, data[:, 0], width, color='b', alpha=0.7)
ax2 = ax1.twinx()
ax2.scatter(ind, data[:, 1], color='r', alpha=0.7)
ax3 = ax1.twinx()
ax3.plot(ind, data[:, 2], color='g', alpha=0.7)
ax4 = ax1.twinx()
ax4.fill_between(ind, data[:, 3], color='y', alpha=0.4)

ax1.set_xlabel('Category')
ax1.set_ylabel(data_labels[0], color='b')
ax2.set_ylabel(data_labels[1], color='r')
ax3.set_ylabel(data_labels[2], color='g')
ax4.set_ylabel(data_labels[3], color='y')

ax1.set_xticks(ind)
ax1.set_xticklabels(line_labels, rotation='vertical')

ax4.spines['right'].set_position(('outward', 120)) 
ax3.spines['right'].set_position(('outward', 60))

ax1.yaxis.label.set_color('b')
ax2.yaxis.label.set_color('r')
ax3.yaxis.label.set_color('g')
ax4.yaxis.label.set_color('y')

ax1.legend([data_labels[0]], loc='upper left')
ax2.legend([data_labels[1]],loc='upper right')
ax3.legend([data_labels[2]],loc='upper center')
ax4.legend([data_labels[3]],loc='center right')

plt.grid()
plt.title('Real Estate Market Analysis: Home Prices, Inventory, Mortgage Rates, and Rent Prices')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/290_202312311430.png')
plt.clf()
