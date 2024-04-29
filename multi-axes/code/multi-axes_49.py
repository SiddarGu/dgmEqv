
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data_labels = ["Gross Revenue (Billions of Dollars)", "Number of Employees", "Number of Outlets"]
line_labels = ["Fast Food", "Cafes", "Restaurants", "Pizzerias", "Grocery Stores", "Bars", "Coffee Shops", "Convenience Stores"]
data = np.array([[456,2100,25000],[250,3000,3400],[820,1300,10000],[320,500,5000],[900,2300,8000],[130,800,4500],[90,1000,1500],[500,1400,6000]])
plot_types = ["bar chart", "line chart", "scatter chart", "area chart"]

fig = plt.figure(figsize=(15, 10))
ax1 = fig.add_subplot(111)
ax1.set_title("Food and Beverage Industry Performance and Growth Overview")
ax1.set_xlabel("Category")
ax1.set_ylabel(data_labels[0], color='b')
ax1.tick_params(axis='y', labelcolor='b')
ax1.bar(line_labels, data[:,0], color='b')

ax2 = ax1.twinx()
ax2.set_ylabel(data_labels[1], color='r')
ax2.tick_params(axis='y', labelcolor='r')
ax2.plot(line_labels, data[:,1], color='r', marker='o', linestyle='dashed')

ax3 = ax1.twinx()
ax3.spines['right'].set_position(('axes', 1.1))
ax3.set_ylabel(data_labels[2], color='g')
ax3.tick_params(axis='y', labelcolor='g')
ax3.plot(line_labels, data[:,2], color='g', linewidth=5, marker='s', linestyle='dotted')

ax1.legend(data_labels[0], loc='upper left')
ax2.legend(data_labels[1], loc='upper right')
ax3.legend(data_labels[2], loc='lower right')

plt.xticks(rotation=-45, ha="left")

ax1.grid()
ax1.autoscale()
ax2.autoscale()
ax3.autoscale()

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/42_2023122270030.png')
plt.clf()