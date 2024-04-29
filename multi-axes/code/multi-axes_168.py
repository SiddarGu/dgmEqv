import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoLocator

#Transforming given data to data_labels, line_labels and data
data_labels = ["Total Revenue (Millions of Dollars)", "Profit Margin (%)", "Market Share (%)"]
line_labels = ["Packaged Foods", 
               "Beverages", 
               "Restaurants", 
               "Dairy Products", 
               "Snacks", 
               "Alcoholic Beverages", 
               "Confectionery", 
               "Frozen Foods", 
               "Baked Goods"]
data = np.array([[2000, 15, 30], 
                 [1500, 10, 25], 
                 [1000, 20, 20], 
                 [800, 12, 15], 
                 [600, 8, 10], 
                 [400, 18, 5], 
                 [300, 7, 3], 
                 [200, 5, 2], 
                 [100, 6, 1]])

#Setting figure size
fig = plt.figure(figsize=(25,15))
ax1 = fig.add_subplot(111)

#Then plotting the first column of data i.e. Revenue 
ax1.bar(line_labels,data[:,0],color='b',width=0.4,label=data_labels[0])
ax1.set_ylabel(data_labels[0], color='b')
ax1.yaxis.set_major_locator(AutoLocator())
# Overlay ax2 on the first plot
ax2 = ax1.twinx()
ax2.plot(line_labels,data[:,1],color='g',label=data_labels[1])
ax2.set_ylabel(data_labels[1], color='g')
ax2.yaxis.set_major_locator(AutoLocator())

#Overlay ax3 on the first plot
ax3 = ax1.twinx()
ax3.plot(line_labels,data[:,2],color='r',label=data_labels[2])
ax3.set_ylabel(data_labels[2], color='r')
ax3.spines['right'].set_position(('outward', 60)) 
ax3.yaxis.set_major_locator(AutoLocator())

s1, label1 = ax1.get_legend_handles_labels()
s2, label2 = ax2.get_legend_handles_labels()
s3, label3 = ax3.get_legend_handles_labels()

ax1.legend(s1+s2+s3,label1+label2+label3,loc='upper left')

ax1.title.set_text('Analysis of Food and Beverage Industry Performance')

plt.grid()
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/276_202312311430.png')
plt.clf()
