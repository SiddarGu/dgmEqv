
# Import libraries
import matplotlib.pyplot as plt
import numpy as np

# Set figure size
plt.figure(figsize=(15,10))

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ["Volume Sold (Liters)", "Sale (Dollars)", "Average of State Bottle Retail", "Bottles Sold"]
line_labels = ["Beer", "Wine", "Spirits", "Hard Seltzer", "Non-Alcoholic Beer", "Ready-to-Drink Cocktails", "Kombucha", "Cocktail Mixers", "Water", "Tea", "Juice"]
data = np.array([[84000, 348000, 4500, 800],
                        [62900, 274500, 9300, 700],
                        [80000, 372100, 27000, 1000],
                        [29900, 140000, 7000, 500],
                        [38000, 160000, 4000, 400],
                        [9000, 38000, 1000, 200],
                        [12000, 50000, 3000, 300],
                        [15000, 50200, 3000, 500],
                        [70000, 280000, 4000, 1000],
                        [50000, 20000, 1000, 400],
                        [80000, 320000, 4000, 700]])

# Plot the data with the type of multi-axes chart
ax1 = plt.subplot(111)
# Plot the first column data
ax1.bar(line_labels, data[:, 0], alpha=0.5, label=data_labels[0])
ax1.set_xlabel("Category")
ax1.set_ylabel(data_labels[0], color="r")
ax1.tick_params(axis="y", labelcolor="r")

# Plot the second column data
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:, 1], label=data_labels[1], linestyle="dashed", color="b")
ax2.set_ylabel(data_labels[1], color="b")
ax2.tick_params(axis="y", labelcolor="b")

# Plot the third column data
ax3 = ax1.twinx()
ax3.spines["right"].set_position(("axes", 1.08))
ax3.plot(line_labels, data[:, 2], label=data_labels[2], linestyle="dotted", color="g", linewidth=3)
ax3.set_ylabel(data_labels[2], color="g")
ax3.tick_params(axis="y", labelcolor="g")

# Plot the fourth column data
ax4 = ax1.twinx()
ax4.spines["right"].set_position(("axes", 1.15))
ax4.scatter(line_labels, data[:, 3], label=data_labels[3], c="m")
ax4.set_ylabel(data_labels[3], color="m")
ax4.tick_params(axis="y", labelcolor="m")

# Set legend
handles, labels = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
handles3, labels3 = ax3.get_legend_handles_labels()
handles4, labels4 = ax4.get_legend_handles_labels()
ax1.legend(handles+handles2+handles3+handles4, labels+labels2+labels3+labels4, loc="upper left", bbox_to_anchor=(0.0, 1.15))

# Set title
plt.title("Food and Beverage Industry Performance Analysis")

# Automatically resize the image by tight_layout() before savefig()
plt.tight_layout()

# Save image
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/4_202312251608.png")

# Clear the current image state
plt.clf()