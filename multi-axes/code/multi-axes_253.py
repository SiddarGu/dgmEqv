import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoLocator

data_labels = ['Total Freight (Thousand Tonnes)','Total Revenue (Million Dollars)','Average Fuel Consumption (Thousand Litres)']
line_labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
data = np.array([[4500, 7580, 250], [4600, 7650, 270], [4700, 7740, 300], [4800, 7820, 330], 
                 [4900, 7910, 360], [5000, 8000, 390], [5100, 8100, 420], [5200, 8200, 450], 
                 [5300, 8300, 480], [5400, 8400, 510], [5500, 8500, 540], [5600, 8600, 570]])

fig = plt.figure(figsize=(15, 10))
ax1 = fig.add_subplot(111)
ax1.plot(line_labels, data[:, 0], color='blue', label=data_labels[0])
ax1.set_ylabel(data_labels[0], color='blue')

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:, 1], color='green', label=data_labels[1])
ax2.set_ylabel(data_labels[1], color='green')

ax3 = ax1.twinx()
ax3.fill_between(line_labels, data[:, 2], color='red', alpha=0.3, label=data_labels[2])
ax3.spines['right'].set_position(('outward', 60))
ax3.set_ylabel(data_labels[2], color='red') 
ax3.yaxis.set_major_locator(AutoLocator())
ax3.grid(False)

plt.title('Yearly Overview of Freight Transport: Total Freight, Revenue, and Fuel Consumption')
fig.legend(loc=1)
plt.gcf().autofmt_xdate()
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/133_202312310108.png')
plt.clf()
