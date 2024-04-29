import matplotlib.pyplot as plt
import numpy as np

# Input data
data_str = '''Product,Volume Sold (Thousands),Revenue (Millions of Dollars),Cost (Dollars)
Beer,10000,12000,50
Wine,6000,11000,75
Spirits,5000,8500,90
Non-alcoholic Beverages,8000,9000,20
Bakery Products,11000,10000,35
Dairy Products,9000,7500,45
Meat,7000,8000,60
Seafood,4500,5000,80
Grains,6500,5500,30
Fruits and Vegetables,7500,6500,25'''

# Parsing data into numpy array
data = []
data_labels = None
line_labels = []
for i, line in enumerate(data_str.split('\n')):
    if i==0:
        data_labels = line.split(',')[1:]
    else:
        items = line.split(',')
        line_labels.append(items[0])
        data.append(list(map(int,items[1:])))
data = np.array(data)

fig = plt.figure(figsize=(25,20))
ax = fig.add_subplot(111)

# Plotting data
colors = ['b', 'g', 'r', 'c']
plots = ['bar', 'line', 'scatter', 'line']
for i in range(len(data_labels)):
    if i == 0:  
        ax.bar(line_labels, data[:,i], color=colors[i], alpha=0.6)
        ax.set_ylabel(data_labels[i])
        ax.yaxis.label.set_color(colors[i])

    else:
        ax_i = ax.twinx()
        if plots[i] == 'bar':
            ax_i.bar(line_labels, data[:,i], color=colors[i], alpha=0.6)
        elif plots[i] == 'line':
            ax_i.plot(line_labels, data[:,i], color=colors[i])
        elif plots[i] == 'scatter':
            ax_i.scatter(line_labels, data[:,i], color=colors[i])

        ax_i.spines['right'].set_position(('outward', 60*(i-1)))
        ax_i.set_ylabel(data_labels[i])
        ax_i.yaxis.label.set_color(colors[i])

ax.set_title('Analysis of Sales and Cost in the Food and Beverage Industry')
ax.set_xlabel('Product')
plt.grid()
plt.autoscale()
plt.tight_layout()
plt.legend(loc='best')

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/94_2023122292141.png')
plt.clf()
