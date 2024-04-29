
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

data_labels = ["Number of Stores", "Online Sales (Millions of Dollars)", "Average Revenue per Store (Thousands of USD)", "Average Selling Price"]
line_labels = ["Clothing Stores", "Grocery Stores", "Electronics Stores", "Home Improvement Stores", "Department Stores"]
data = np.array([[7000, 1200, 5.45, 60], [12000, 800, 2.10, 50], [3000, 900, 7.90, 100], [4000, 200, 5.50, 80], [2000, 500, 14.30, 70]])

fig = plt.figure(figsize=(15, 10))
ax1 = fig.add_subplot(111)
ax1.bar(line_labels, data[:, 0], width=0.2, color="b", alpha=0.5)
ax1.set_ylabel(data_labels[0], color="b")

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:, 1], marker="o", linestyle="-", color="r")
ax2.set_ylabel(data_labels[1], color="r")

ax3 = ax1.twinx()
ax3.spines["right"].set_position(("axes", 1.1))
ax3.plot(line_labels, data[:, 2], marker="o", linestyle="-", color="g")
ax3.set_ylabel(data_labels[2], color="g")

ax4 = ax1.twinx()
ax4.spines["right"].set_position(("axes", 1.2))
ax4.plot(line_labels, data[:, 3], marker="o", linestyle="-", color="y")
ax4.set_ylabel(data_labels[3], color="y")

ax1.set_xlabel("Category")
ax1.set_title("Retail and E-commerce Sales Analysis: Store Numbers, Online Revenue, and Average Prices")
ax1.xaxis.set_major_locator(ticker.FixedLocator(np.arange(5)))
ax1.xaxis.set_major_formatter(ticker.FixedFormatter((line_labels)))
ax1.grid(True)
ax2.grid(True)
ax3.grid(True)
ax4.grid(True)
ax1.legend(data_labels, loc="upper right", bbox_to_anchor=(1., 1))
ax2.legend([data_labels[1]], loc="upper right", bbox_to_anchor=(1., 0.95))
ax3.legend([data_labels[2]], loc="upper right", bbox_to_anchor=(1., 0.9))
ax4.legend([data_labels[3]], loc="upper right", bbox_to_anchor=(1., 0.85))
ax1.xaxis.set_tick_params(rotation=45)
ax1.yaxis.tick_left()
ax2.yaxis.tick_right()
ax3.yaxis.tick_right()
ax4.yaxis.tick_right()
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/15_2023122270030.png")
plt.clf()