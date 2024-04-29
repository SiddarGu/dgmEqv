import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

# Data preparation
data_labels = ['Number of Internet Users (Millions)', 'E-commerce Sales (Billion Dollars)', 
               'Average Screen Time (Hours)', 'Cybersecurity Incidents (Thousands)']

data = np.array([[3202, 1940, 3.1, 314], 
                 [3425, 2221, 3.4, 571], 
                 [3629, 2546, 3.9, 826], 
                 [3907, 2961, 4.3, 948], 
                 [4204, 3514, 4.6, 1365], 
                 [4598, 4165, 5.5, 1634]])

line_labels = ['2015', '2016', '2017', '2018', '2019', '2020']

# Create figure
fig = plt.figure(figsize=(20,10))
ax1 = fig.add_subplot(111)

# Bar chart
ax1.bar(line_labels, data[:,0], width=0.2, color='b', alpha=0.8, label=data_labels[0])

# Line chart
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], color='g', label=data_labels[1])

# Area chart
ax3 = ax1.twinx()
ax3.fill_between(line_labels, 0, data[:,2], color='r', alpha=0.3, label=data_labels[2])

# Scatter chart
ax4 = ax1.twinx()
ax4.scatter(line_labels, data[:,3], color='y', label=data_labels[3])

# Y-axes
ax1.set_ylabel(data_labels[0], color='b')
ax2.set_ylabel(data_labels[1], color='g')
ax3.spines['right'].set_position(('outward', 60))   
ax3.set_ylabel(data_labels[2], color='r')
ax4.spines['right'].set_position(('outward', 120))   
ax4.set_ylabel(data_labels[3], color='y')

# AutoLocator
ax2.yaxis.set_major_locator(ticker.AutoLocator())
ax3.yaxis.set_major_locator(ticker.AutoLocator())
ax4.yaxis.set_major_locator(ticker.AutoLocator())

# Legend, grid, title
fig.legend(bbox_to_anchor=(0.5, 1), loc='upper center', ncol=4)
ax1.grid(True, linestyle='--', which='both', color='gray', alpha=0.5)
plt.title("Technology and the Internet: User Base, E-commerce Growth, Screen Time and Security Risk Analysis", y=1.1)

# Save image
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/87_2023122292141.png', dpi=300)

# Clear image
plt.clf()
