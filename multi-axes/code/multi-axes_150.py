import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import AutoLocator

# Transforming given data
data = [['Education', 800, 5, 5], ['Healthcare', 1200, 10, 4], ['Defense', 500, 15, 6], ['Infrastructure', 400, 3, 7], 
        ['Social Welfare', 700, 7, 4], ['Law Enforcement', 300, 2, 3], ['Environmental Protection', 200, 1, 2], 
        ['Transportation', 600, 6, 5]]
data_labels = ["Total Government Spending (Billions of Dollars)", "Public Debt (Trillions of Dollars)", 
               "Unemployment Rate (%)"]
line_labels = ['Education', 'Healthcare', 'Defense', 'Infrastructure', 'Social Welfare', 'Law Enforcement', 
               'Environmental Protection', 'Transportation']

df = pd.DataFrame(data, columns=["Category"] + data_labels)
line_labels = df['Category']
data = df.drop(columns = ['Category']).values

# Plotting the data
fig = plt.figure(figsize=(25, 15))
ax1 = fig.add_subplot(111)

# for bar chart
ax1.bar(line_labels, data[:, 0], color='g', alpha=0.7)
ax1.set_ylabel(data_labels[0], color='g')

# for line chart
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:, 1], color='b')
ax2.set_ylabel(data_labels[1], color='b')

# for scatter chart
ax3 = ax1.twinx()
ax3.scatter(line_labels, data[:, 2], color='r')
ax3.set_ylabel(data_labels[2], color='r')

# positioning y-axis for ax3
ax3.spines['right'].set_position(('outward', 60))

# Adding grid
ax1.grid()

# AutoLocator
ax1.yaxis.set_major_locator(AutoLocator())
ax2.yaxis.set_major_locator(AutoLocator())
ax3.yaxis.set_major_locator(AutoLocator())

# legend setting
ax1.legend([data_labels[0]], loc='upper right')
ax2.legend([data_labels[1]], loc='upper center')
ax3.legend([data_labels[2]], loc='upper left')

plt.title('Government Expenditure and Public Policy Assessment')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/282_202312311430.png')
plt.clf()
