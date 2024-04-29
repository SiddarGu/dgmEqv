
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

# Transform the given data into three variables: data_labels, data, line_labels.
data = np.array([[480, 1590, 5.7], [1080, 2090, 2.4], [390, 1040, 2.3], [720, 4330, 2.1], [530, 1460, 8.6], [360, 1070, 12.1], [2250, 2590, 3.4], [850, 780, 2.2]])
data_labels = ["Cost of Treatment (Millions of Dollars)", "Average Hospital Stay (Days)", "Patients Treated (Thousands)"]
line_labels = ["Inpatient", "Outpatient", "Emergencies", "Primary Care", "Mental Health", "Rehabilitation", "Specialized Care", "Home Care"]

# Create figure before plotting, i.e., add_subplot(111) follows plt.figure(). 
# The value of figsize should be set larger than 20 to prevent content from being displayed. 
fig = plt.figure(figsize=(15,10))
ax1 = fig.add_subplot(111)

# The first column of data array, i.e., data[:,0] is plotted first, whose y-axis is unique to data[:,0] and defined as the primary y-axis in the multi-axes chart, while the x-axis is shared.
ax1.bar(line_labels, data[:, 0], width=0.25, color="darkgreen", alpha=0.8)
ax1.set_ylabel(data_labels[0], fontsize=15, color="darkgreen")
ax1.tick_params(axis='y', labelcolor="darkgreen")

# Then, the second column of data array, i.e. data[:,1], is plotted after using twinx to overlay a new ax, named as ax2 on the first plot, where the x-axis is reused from the first plot and the y-axis is unique for data[:, 1].
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:, 1], linewidth=2, marker="o", color="royalblue")
ax2.set_ylabel(data_labels[1], fontsize=15, color="royalblue")
ax2.tick_params(axis='y', labelcolor="royalblue")

# After that, the third column of data array (if possible), i.e. data[:,2], is plotted after using another twinx, named as ax3 to overlay another new ax on the first plot, where the x-axis is reused from the first plot and the y-axis is unique for data[:, 2].
ax3 = ax1.twinx()
ax3.plot(line_labels, data[:, 2], linewidth=2, marker="x", color="orange")
ax3.set_ylabel(data_labels[2], fontsize=15, color="orange")
ax3.tick_params(axis='y', labelcolor="orange")

# The primary y-axis is naturally positioned on the left side of the chart, with other y-axes placed on the right side.
ax3.spines['right'].set_position(('axes', 1.1))

# Label all axes, and match their colors with the data plotted against them.
plt.xticks(fontsize=14)
plt.title("Healthcare Services Analysis: Treatment Costs, Patient Volume, and Average Hospital Stay", fontsize=20)

# Show the legends of all plots at different positions, ensuring it does not overlap with other legends and not interfere with data, title and axes.
ax1.legend(data_labels[0], loc="best")
ax2.legend(data_labels[1], loc="lower left")
ax3.legend(data_labels[2], loc="lower right")

# Drawing techniques such as background grids can be used. 
ax1.grid(True)

# Use Autolocator for all ax, i.e., ax1, ax2, ax3, ..., to adjust the range of all y-axes.
ax1.yaxis.set_major_locator(ticker.AutoLocator())
ax2.yaxis.set_major_locator(ticker.AutoLocator())
ax3.yaxis.set_major_locator(ticker.AutoLocator())

# Automatically resize the image by tight_layout() before savefig().
plt.tight_layout()

# The image must be saved as /cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/8_2023122261325.png.
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/8_2023122261325.png")

# Clear the current image state at the end of the code.
plt.clf()