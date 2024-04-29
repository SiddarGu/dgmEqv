

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

# Transform the given data into three variables: data_labels, data, line_labels.
data_labels = ['Market Value (Millions of Dollars)', 'Share Price', 'Profit Margin', 'Revenue']
data = np.array([[19081, 480, 14, 27894],
                 [15835, 310, 7, 65673],
                 [14641, 325, 20, 12170],
                 [14234, 360, 12, 19081],
                 [13362, 280, 14, 18391],
                 [11824, 395, 17, 16765],
                 [10549, 220, 11, 14234],
                 [8600, 365, 19, 13362],
                 [5504, 495, 13, 11824],
                 [4243, 230, 16, 10549]])
line_labels = ['Technology', 'Health Care', 'Financial Services',
               'Industrial Goods', 'Consumer Services', 'Consumer Goods', 'Telecommunications', 'Energy', 'Utilities', 'Materials']

# Plot the data with the type of multi-axes chart.
plot_types = ['bar chart', 'scatter chart', 'line chart', 'area chart']

# Create figure before plotting
fig = plt.figure(figsize=(15, 10))
ax1 = fig.add_subplot(111)

# Plot the first column of data array, i.e., data[:,0]
ax1.bar(line_labels, data[:, 0], label=data_labels[0], color='#3F51B5', width=0.2, alpha=0.8)
ax1.set_ylabel(data_labels[0], color='#3F51B5')
ax1.tick_params(axis='y', labelcolor='#3F51B5')

# Plot the second column of data array, i.e. data[:,1]
ax2 = ax1.twinx()
ax2.scatter(line_labels, data[:, 1], label=data_labels[1], s=100, color='#F50057', alpha=0.8)
ax2.set_ylabel(data_labels[1], color='#F50057')
ax2.tick_params(axis='y', labelcolor='#F50057')

# Plot the third column of data array, i.e. data[:,2]
ax3 = ax1.twinx()
ax3.plot(line_labels, data[:, 2], label=data_labels[2], linestyle='--', marker='*', color='#CDDC39', alpha=0.8)
ax3.set_ylabel(data_labels[2], color='#CDDC39')
ax3.spines["right"].set_position(("axes", 1.1))
ax3.tick_params(axis='y', labelcolor='#CDDC39')

# Plot the fourth column of data array, i.e. data[:,3]
ax4 = ax1.twinx()
ax4.fill_between(line_labels, data[:, 3], 0, label=data_labels[3], color='#FF9800', alpha=0.6)
ax4.set_ylabel(data_labels[3], color='#FF9800')
ax4.spines["right"].set_position(("axes", 1.2))
ax4.tick_params(axis='y', labelcolor='#FF9800')

# Labeling all axes and legends
ax1.set_title('Business and Finance Market Performance: Market Value, Share Price, Profit Margin, and Revenue',
               fontsize=16, fontweight='bold')
ax1.set_xlabel('Category')
x_range = np.arange(len(line_labels))
ax1.set_xticks(x_range)
ax1.set_xticklabels(line_labels, rotation=37)
ax1.legend(loc='upper left', bbox_to_anchor=(0.05, 1), fontsize=14)
ax2.legend(loc='upper left', bbox_to_anchor=(0.4, 1), fontsize=14)
ax3.legend(loc='upper left', bbox_to_anchor=(0.57, 1), fontsize=14)
ax4.legend(loc='upper left', bbox_to_anchor=(0.9, 1), fontsize=14)

# Set Autolocator for all ax\
# Drawing techniques such as background grids and automatically resize the image by tight_layout()
ax1.grid(True, linestyle='dashed', linewidth=2, alpha=0.2)
plt.tight_layout()

# save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/47_2023122270030.png')

# Clear the current image state at the end of the code.
plt.clf()