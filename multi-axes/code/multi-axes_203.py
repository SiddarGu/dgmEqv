import matplotlib.pyplot as plt
import numpy as np

# Transforming given data
raw_data = "Category,Volume Produced (Tons),Revenue (Millions of Dollars),Average Product Price ($),Items Sold/n Dairy Products,1200,5000,102,49000/n Meat Products,980,4500,130,34598/n Bakery Products,1150,3500,94,37220/n Alcoholic Beverages,1100,9000,222,40500/n Non-alcoholic Beverages,1250,3000,70,42808/n Fruits and Vegetables,1300,2500,80,31250/n Grain Products,1230,3000,68,44105/n Seafood,950,4200,140,30082/n Confectionery,1100,6000,120,50000/n Packaged Foods,1200,4000,78,51277"
data_lines = raw_data.split('/n')
data_labels = data_lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in data_lines[1:]]
data = np.array([[float(n) for n in line.split(',')[1:]] for line in data_lines[1:]])

# Plotting multi-axes chart
fig = plt.figure(figsize=(20,20))
ax1 = fig.add_subplot(111)
ax1.bar(line_labels, data[:,0], color='b', alpha=0.6, label=data_labels[0])
ax1.set_ylabel(data_labels[0], color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], 'r-', label=data_labels[1])
ax2.set_ylabel(data_labels[1], color='r')
ax2.tick_params('y', colors='r')

if data.shape[1] > 2:
    ax3 = ax1.twinx()
    ax3.spines['right'].set_position(('outward', 60))
    ax3.plot(line_labels, data[:,2], 'g-', label=data_labels[2])
    ax3.set_ylabel(data_labels[2], color='g')
    ax3.tick_params('y', colors='g')

if data.shape[1] > 3:
    ax4 = ax1.twinx()
    ax4.spines['right'].set_position(('outward', 120))
    ax4.scatter(line_labels, data[:,3], color='c', label=data_labels[3])
    ax4.set_ylabel(data_labels[3], color='c')
    ax4.tick_params('y', colors='c')

plt.title('Analysis of Production Volume, Revenue, and Pricing in the Food and Beverage Industry')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/170_202312310108.png')
