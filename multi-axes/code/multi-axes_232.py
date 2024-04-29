
#import libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

#transform data
data_labels = ["Annual Revenue (Millions of Dollars)", "Net Profit (Millions of Dollars)", "Market Capitalization (Millions of Dollars)", "Number of Employees"]
line_labels = ["Investment Banking", "Commercial Banking", "Asset Management", "Retail Banking", "Insurance Services", "Credit Card Services", "Mutual Fund Services", "Private Equity"]
data = np.array([[1750,600,44000,16000], [1180,780,99000,18000], [700,350,60000,9000], [1000,550,85000,14000], [1020,600,70000,12000], [790,400,58000,10000], [500,290,45000,8000], [790,500,75000,12000]])

#plot data
fig = plt.figure(figsize=(16, 10))
ax1 = fig.add_subplot(111)

#plot the first column data using bar chart
ax1.bar(line_labels, data[:, 0], width=0.8, color='#008080', alpha=0.8)
ax1.set_ylabel(data_labels[0], color='#008080')
ax1.tick_params('y', colors='#008080')
ax1.yaxis.set_major_locator(ticker.MultipleLocator(500))
ax1.set_xlabel('Category')
ax1.set_title('Business and Finance Performance Analysis: Revenues, Profits, and Market Capitalization',fontsize=14, fontweight='bold')

#plot the fourth column data using area chart
ax2 = ax1.twinx()
ax2.fill_between(line_labels, data[:, 3], color='#0000FF', alpha=0.6, label=data_labels[3])
ax2.spines['right'].set_position(('axes', 1.12))
ax2.set_ylabel(data_labels[3], color='#0000FF')
ax2.tick_params('y', colors='#0000FF')
ax2.yaxis.set_major_locator(ticker.MultipleLocator(2000))

#plot the second column data using line chart
ax3 = ax1.twinx()
ax3.plot(line_labels, data[:, 1], marker='o', linestyle='--', color='#FF0000', label=data_labels[1])
ax3.set_ylabel(data_labels[1], color='#FF0000')
ax3.tick_params('y', colors='#FF0000')
ax3.yaxis.set_major_locator(ticker.MultipleLocator(200))

#plot the third column data using scatter chart
ax4 = ax1.twinx()
ax4.scatter(line_labels, data[:, 2], marker='s', color='#800080', label=data_labels[2])
ax4.spines['right'].set_position(('axes', 1.05))
ax4.set_ylabel(data_labels[2], color='#800080')
ax4.tick_params('y', colors='#800080')
ax4.yaxis.set_major_locator(ticker.MultipleLocator(20000))


#show legend
handles, labels = ax1.get_legend_handles_labels()
handles1, labels1 = ax3.get_legend_handles_labels()
handles2, labels2 = ax4.get_legend_handles_labels()
handles3, labels3 = ax2.get_legend_handles_labels()
handles_combined = handles + handles1 + handles2 + handles3
labels_combined = labels + labels1 + labels2 + labels3
ax1.legend(handles_combined, labels_combined, loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=4, fontsize=12)

#draw background grids
ax1.grid(True, axis='y', linestyle='--', color='#A9A9A9', alpha=0.8)
ax3.grid(True, axis='y', linestyle='--', color='#A9A9A9', alpha=0.8)
ax4.grid(True, axis='y', linestyle='--', color='#A9A9A9', alpha=0.8)
ax2.grid(True, axis='y', linestyle='--', color='#A9A9A9', alpha=0.8)

#automatically resize the image
plt.tight_layout()

#save image
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/2_202312251608.png")

# Clear the current image state at the end of the code
plt.clf()