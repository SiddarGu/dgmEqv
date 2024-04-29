

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

# transform the given data into three variables
data_labels = ["Gross Revenue (Millions of Dollars)", "Net Profit (Millions of Dollars)", "Cost of Goods Sold (Millions of Dollars)", "Expenses (Millions of Dollars)"]
data = np.array([[9200,4500,3200,800],[9500,5500,4500,900],[6800,3000,2600,600],[8200,4000,3000,700],[9600,6000,3800,1000],[8000,4600,3700,700]])
line_labels = ["Insurance","Banking","Investment","Credit","Real Estate","Securities"]

# Create figure before plotting
fig = plt.figure(figsize=(15,10))
ax1 = fig.add_subplot(111)

# Plot the data with the type of multi-axes chart
# plot data[:,0]
ax1.bar(line_labels, data[:,0], color='goldenrod', alpha=0.6, width=0.3, label=data_labels[0])
ax1.set_ylabel(data_labels[0], fontdict={'color': 'goldenrod'})
ax1.tick_params(axis='y', labelcolor='goldenrod')

# plot data[:,1]
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], linestyle='dashed', color='orangered', label=data_labels[1])
ax2.set_ylabel(data_labels[1], fontdict={'color': 'orangered'})
ax2.tick_params(axis='y', labelcolor='orangered')

# plot data[:,2]
ax3 = ax1.twinx()
ax3.spines["right"].set_position(("axes", 1.1))
ax3.plot(line_labels, data[:,2], linestyle='solid', color='teal', label=data_labels[2])
ax3.tick_params(axis='y', labelcolor='teal')
ax3.set_ylabel(data_labels[2], fontdict={'color': 'teal'})

# plot data[:,3]
ax4 = ax1.twinx()
ax4.spines["right"].set_position(("axes", 1.2))
ax4.plot(line_labels, data[:,3], linestyle='dotted', color='dodgerblue', label=data_labels[3])
ax4.tick_params(axis='y', labelcolor='dodgerblue')
ax4.set_ylabel(data_labels[3], fontdict={'color': 'dodgerblue'})

# Label all axes
ax1.set_xlabel('Category')

# Drawing techniques such as background grids
ax1.grid(True, linestyle='-', color='lightgrey', alpha=0.5)

# Use Autolocator for all ax
ax1.xaxis.set_major_locator(ticker.AutoLocator())
ax1.yaxis.set_major_locator(ticker.AutoLocator())
ax2.yaxis.set_major_locator(ticker.AutoLocator())
ax3.yaxis.set_major_locator(ticker.AutoLocator())
ax4.yaxis.set_major_locator(ticker.AutoLocator())

# Set the title of the figure
plt.title("Business and Finance Performance Analysis: Revenues, Profits, and Expenditures")

# Automatically resize the image by tight_layout() before savefig()
fig.tight_layout()

# The image must be saved as /cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/18_2023122261325.png
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/18_2023122261325.png')

# Clear the current image state at the end of the code
plt.clf()