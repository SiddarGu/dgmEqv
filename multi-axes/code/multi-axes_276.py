import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import AutoLocator
import numpy as np

data ='''Product,Units Sold,Revenue (Millions),Average Price (Dollars)
Soda,78000,350,4.5
Beer,68000,850,12.5
Burger,50000,325,6.5
Pizza,60000,510,8.5
Sandwich,70000,490,7
Pasta,52000,379,7.3
Wine,42000,600,14.3
Cheese,45000,380,8.45
Chocolate,100000,300,3
Ice Cream,74000,296,4
Coffee,120000,720,6
Tea,98000,490,5
Chips,102000,200,1.95
Fish,37000,592,16
Steak,25000,687,27.5'''
  
df = pd.DataFrame([x.split(',') for x in data.split('\n')])
df.columns = df.iloc[0]
df = df.iloc[1:]
df[df.columns[1:]] = df[df.columns[1:]].apply(pd.to_numeric)
line_labels = df[df.columns[0]]
data = df[df.columns[1:]].to_numpy()
data_labels = df.columns[1:]

fig = plt.figure(figsize=(25,10))
ax1 = fig.add_subplot(111)

ax1.bar(line_labels , data[:,0], color='c', label=data_labels[0], alpha=0.8)
ax1.set_ylabel(data_labels[0])
ax1.yaxis.label.set_color('c')
ax1.yaxis.set_major_locator(AutoLocator())

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1],color='g', label=data_labels[1])
ax2.set_ylabel(data_labels[1])
ax2.yaxis.label.set_color('g')
ax2.yaxis.set_major_locator(AutoLocator())

ax3 = ax1.twinx()
ax3.scatter(line_labels, data[:,2],color='r', label=data_labels[2])
ax3.set_ylabel(data_labels[2])
ax3.yaxis.label.set_color('r')
ax3.yaxis.set_major_locator(AutoLocator())

ax3.spines['right'].set_position(('outward', 60))

ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
ax3.legend(loc='center right')

plt.title("Profit and Selling Price Analysis of Products from the Food and Beverage Industry", fontsize=20)
plt.tight_layout()
plt.grid(True)
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/109_202312310108.png')
plt.clf()
