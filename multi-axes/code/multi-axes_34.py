

import matplotlib.pyplot as plt
import numpy as np

data_labels = ["Number of Consumers (Millions)", "Consumption (TWh)", 
               "Average Price ($)"]
data = np.array([[560, 3700, 52], [570, 1400, 5.2], [740, 1200, 2.2], 
                 [290, 400, 20], [750, 3800, 45], [200, 1000, 15]])
line_labels = ["Electric Power", "Natural Gas", "Petroleum", "Renewables", 
               "Coal", "Nuclear"]

plt.figure(figsize=(15, 10))
ax1 = plt.subplot(111)
ax1.bar(line_labels, data[:, 0], color="r", alpha=0.6, label=data_labels[0]) 
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:, 1], color="b", marker="o", label=data_labels[1])
ax3 = ax1.twinx()
ax3.spines["right"].set_position(("axes", 1.2))
ax3.plot(line_labels, data[:, 2], color="g", linestyle="--", label=data_labels[2])
ax1.set_xlabel("Category")
ax1.set_ylabel(data_labels[0], color="r")
ax2.set_ylabel(data_labels[1], color="b")
ax3.set_ylabel(data_labels[2], color="g")
ax1.legend(loc="upper left")
ax2.legend(loc="upper right")
ax3.legend(loc="lower right")
ax1.grid()
ax1.autoscale_view()
ax2.autoscale_view()
ax3.autoscale_view()
plt.title("Energy and Utilities Consumption Trends Analysis")
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/3_2023122261325.png")
plt.clf()