

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# transform data into three variables: data_labels, data, line_labels
data_labels = ["Number of Students","Number of Graduates","Number of Academic Staff","Number of Institutions"]
line_labels = ["Languages","Psychology","Sociology","History","Philosophy","Anthropology","Literature","Art","Music"]
data = np.array([[16947, 6002, 543, 18], [26366, 8645, 600, 29], [29800, 8298, 546, 39], [26392, 6825, 455, 20], [18744, 5128, 364, 14], [18098, 5087, 480, 22], [22918, 5903, 489, 26], [18092, 5232, 349, 17], [15890, 4587, 312, 17]], dtype = np.float64)

# Plot the data with the type of multi-axes chart
fig = plt.figure(figsize=(25, 10))
ax1 = fig.add_subplot(111)

# plot the first column of data array, i.e., data[:,0]
ax1.bar(line_labels, data[:, 0], width=0.4, color="skyblue", alpha=0.6)
ax1.set_ylabel(data_labels[0], fontsize=15, color="skyblue")
ax1.tick_params(axis='y', colors="skyblue")

# overlay a new ax on the first plot: twinx for ax2
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:, 1], linestyle='dashed', linewidth=2.5, color="orange")
ax2.set_ylabel(data_labels[1], fontsize=15, color="orange")
ax2.tick_params(axis='y', colors="orange")

# overlay another new ax on the first plot: twinx for ax3
ax3 = ax1.twinx()
ax3.plot(line_labels, data[:, 2], linestyle='dotted', linewidth=2.5, color="green")
ax3.set_ylabel(data_labels[2], fontsize=15, color="green")
ax3.tick_params(axis='y', colors="green")

# overlay another new ax on the first plot: twinx for ax4
ax4 = ax1.twinx()
ax4.plot(line_labels, data[:, 3], marker='o', markersize=8, linestyle='None', color="red")
ax4.set_ylabel(data_labels[3], fontsize=15, color="red")
ax4.tick_params(axis='y', colors="red")

# seperate different y-axes
ax3.spines['right'].set_position(('outward', 60))
ax4.spines['right'].set_position(('outward', 120))

# label all axes
ax1.set_xlabel("Category", fontsize=15)
ax1.set_title("Higher Education in Social Sciences and Humanities: Student, Graduate, Academic Staff, and Institution Analysis", fontsize=20)

# show the legends of all plots at different positions
ax1.legend(["Number of Students"], loc='upper left', fontsize=15)
ax2.legend(["Number of Graduates"], loc='upper right', fontsize=15)
ax3.legend(["Number of Academic Staff"], loc='lower right', fontsize=15)
ax4.legend(["Number of Institutions"], loc='lower left', fontsize=15)

# drawing techniques such as background grids
ax1.grid(axis='y', linestyle='dashed', color='grey', linewidth=1, alpha=0.6)
ax2.grid(axis='y', linestyle='dashed', color='grey', linewidth=1, alpha=0.6)
ax3.grid(axis='y', linestyle='dashed', color='grey', linewidth=1, alpha=0.6)
ax4.grid(axis='y', linestyle='dashed', color='grey', linewidth=1, alpha=0.6)

# use Autolocator for all ax, i.e., ax1, ax2, ax3, ..., to adjust the range of all y-axes
ax1.yaxis.set_major_locator(ticker.AutoLocator())
ax2.yaxis.set_major_locator(ticker.AutoLocator())
ax3.yaxis.set_major_locator(ticker.AutoLocator())
ax4.yaxis.set_major_locator(ticker.AutoLocator())

# automatically resize the image by tight_layout() before savefig()
plt.tight_layout()

# save the image
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/17_2023122270030.png")

# clear the current image state
plt.clf()