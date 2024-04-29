
#import libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

#Transform the given data into three variables: data_labels, data, line_labels
data_labels = ["Category", "Volume Produced (Metric Tons)", "Revenue (Millions of Dollars)", "Average Price per Ton", "Jobs Created"]
line_labels = ["Rice", "Corn", "Wheat", "Soybean", "Fruits", "Vegetables", "Dairy Products", "Poultry", "Beef", "Pork", "Fish"]
data = np.array([[4500, 290, 5.4, 7500], [6600, 400, 6.5, 9000], [7200, 480, 6.9, 10000], [3800, 250, 3.5, 6000], [5400, 420, 8.9, 8000], [7100, 520, 7.4, 9000], [7800, 600, 7.7, 11000], [5200, 400, 7.7, 8000], [6500, 500, 7.7, 10000], [3800, 320, 8.4, 6000], [4500, 280, 6.2, 7500]])

#Split the data array from the second dimension to get the data correpsonding to each category
vol_prod = data[:,0]
rev = data[:,1]
avg_price = data[:,2]
jobs = data[:,3]

#Plot the data with the type of multi-axes chart. Create figure before plotting, i.e., add_subplot() follows plt.figure().
fig = plt.figure(figsize=(12, 8))
ax1 = fig.add_subplot(1,1,1, label="1")
ax2 = ax1.twinx()
ax3 = ax1.twinx()
ax4 = ax1.twinx()

#The plot type of each category is sequentially decided by the following plot types, i.e., [ bar chart,bar chart,scatter chart,line chart].
ax1.bar(line_labels, vol_prod, label=data_labels[1], color="green", alpha=0.3, width=0.6, align="edge", edgecolor="black")
ax2.bar(line_labels, rev, label=data_labels[2], color="blue", alpha=0.3, width=0.6, align="edge", edgecolor="black")
ax3.scatter(line_labels, avg_price, label=data_labels[3], color="red", marker="^")
ax4.plot(line_labels, jobs, label=data_labels[4], color="purple", marker="o", linestyle="--")

#For the plot of each category, overlay the plot on one chart with a shared x-axis and an individual y-axis, a distinct color and marker style, ensuring the y-axes are visually distinct from the primary y-axis. All other y-axes should be positioned opposite the primary y-axis.
ax1.set_xticks(line_labels)
ax1.set_xlabel(data_labels[0])
ax1.set_ylabel(data_labels[1], color="green")
ax1.tick_params(axis="y", colors="green")
ax2.set_ylabel(data_labels[2], color="blue")
ax2.yaxis.set_label_position("right")
ax2.tick_params(axis="y", colors="blue")
ax3.set_ylabel(data_labels[3], color="red")
ax3.spines["right"].set_position(("axes", 1.1))
ax3.tick_params(axis="y", colors="red")
ax4.set_ylabel(data_labels[4], color="purple")
ax4.spines["right"].set_position(("axes", 1.15))
ax4.tick_params(axis="y", colors="purple")

#Label each axis with the name of the category it represents, matching the color of the data plotted against it.
ax1.set_title("Agricultural Production and Economic Impact", fontsize=20)
# Show the legends of all plots at different positions
ax1.legend(data_labels[0], loc="upper right", bbox_to_anchor=(1.0, 1.0))
ax2.legend(data_labels[1], loc="upper right", bbox_to_anchor=(1.0, 0.9))
ax3.legend(data_labels[2], loc="upper right", bbox_to_anchor=(1.0, 0.8))
ax4.legend(data_labels[3], loc="upper right", bbox_to_anchor=(1.0, 0.7))

# Drawing techniques such as background grids can be used
ax1.grid(linestyle="--", color="gray")

# Use Autolocator for all ax, i.e., ax1, ax2, ax3, ...
ax1.autoscale()
ax2.autoscale()
ax3.autoscale()
ax4.autoscale()

# Automatically resize the image by tight_layout() before savefig()
plt.tight_layout()

# Save the image
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/3.png")

# Clear the current image state at the end of the code
plt.clf()