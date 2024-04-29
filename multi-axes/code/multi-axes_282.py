import matplotlib.pyplot as plt
import numpy as np

data_str="Product,Supply Demand (Units),Revenue (Millions of Dollars),Average Sale Price (Dollars)/n Dairy,70000,2150,3/n Fruits,85000,2550,3/n Bread and Bakery,65000,2950,4/n Meat,78000,3210,4/n Beverages,82000,2690,3/n Frozen Foods,66000,2500,4/n Snacks,73000,2720,4/n Sweets and Confectionery,71000,3050,4/n Packaged Foods,78000,3000,4/n Prepared Meals,69000,2790,4/n Organic Foods,76000,3300,4/n Fine Foods,72000,2960,4"
data_list = [i.split(",") for i in data_str.split("/n ")]
data_labels = data_list[0][1:]
line_labels = [i[0] for i in data_list[1:]]
data = np.array([i[1:] for i in data_list[1:]], dtype=float)

fig = plt.figure(figsize=(22,16))

ax1 = fig.add_subplot(111)
ax1.bar(line_labels, data[:,0], color='b', alpha=0.6, align='center')
ax1.set_ylabel(data_labels[0])
ax1.yaxis.label.set_color('blue')

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], 'r-', marker='o')
ax2.set_ylabel(data_labels[1])
ax2.yaxis.label.set_color('red')

if data.shape[1]>2:
    ax3 = ax1.twinx()
    ax3.fill_between(line_labels, data[:,2], color='green', alpha=0.3)
    ax3.set_ylabel(data_labels[2])
    ax3.yaxis.label.set_color('green')
    ax3.spines['right'].set_position(('outward', 60))

if data.shape[1]>3:
    ax4 = ax1.twinx()
    ax4.scatter(line_labels, data[:,3], color='purple')
    ax4.set_ylabel(data_labels[3])
    ax4.yaxis.label.set_color('purple')
    ax4.spines['right'].set_position(('outward', 120))

plt.title('Product Supply and Revenue Analysis in the Food and Beverage Industry', fontsize=20)
plt.grid(True)
fig.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/193_202312310150.png')
plt.show()
plt.clf()
