
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ["Volume of Shipments (Millions of Units)", "Revenue (Millions of Dollars)", "Average Shipping Cost (Dollars)", "Average Delivery Time (Hours)"]
data = np.array([[650,7300,10.5,32],[800,7680,8.5,61],[900,7200,6.5,36],[950,7890,11.5,48],[700,6190,9.5,50],[1000,7950,7.5,65],[850,7850,4.5,50],[1000,7140,7.5,70]])
line_labels = ["Air Freight","Sea Freight","Rail Freight","Trucking","Logistics Services","Courier Services","Warehousing","Pipeline Transport"]

# Create figure
fig = plt.figure(figsize=(15, 10))
ax1 = fig.add_subplot(111)

# Plot the data
ax1.bar(line_labels, data[:,0], color="#1f77b4", alpha=0.8, label=data_labels[0])
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], color="#ff7f0e", label=data_labels[1], marker="o")
ax3 = ax1.twinx()
ax3.spines["right"].set_position(("axes", 1.1))
ax3.plot(line_labels, data[:,2], color="#2ca02c", label=data_labels[2], marker="^")
ax4 = ax1.twinx()
ax4.spines["right"].set_position(("axes", 1.16))
ax4.plot(line_labels, data[:,3], color="#d62728", label=data_labels[3], marker="v")

# Labels
ax1.set_xlabel("Category")
ax1.set_ylabel(data_labels[0], color="#1f77b4")
ax2.set_ylabel(data_labels[1], color="#ff7f0e")
ax3.set_ylabel(data_labels[2], color="#2ca02c")
ax4.set_ylabel(data_labels[3], color="#d62728")

# Legends
ax1.legend(loc="upper left")
ax2.legend(loc="upper center")
ax3.legend(loc="upper right")
ax4.legend(loc="lower right")

# Adjust the range of all y-axes
ax1.yaxis.set_minor_locator(AutoMinorLocator(4))
ax2.yaxis.set_minor_locator(AutoMinorLocator(4))
ax3.yaxis.set_minor_locator(AutoMinorLocator(4))
ax4.yaxis.set_minor_locator(AutoMinorLocator(4))

# Set the title
plt.title("Transport and Logistics Performance: Volume, Revenue, Cost, and Delivery Trends")

# Automatically resize the image
plt.tight_layout()

# Save the image
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/29_2023122270030.png")

# Clear the current image state
plt.clf()