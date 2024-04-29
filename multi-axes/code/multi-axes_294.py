
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# transform data to variables
data_labels = np.array(["Number of Cases", "Lawyers Involved", "Average Length of Case (Months)", "Average Cost of Case (Dollars)"])
data = np.array([[2900, 7000, 11, 350000], [2100, 3000, 14, 220000], [1800, 5000, 10, 400000], [1400, 2500, 15, 210000], [1200, 4000, 9, 320000], [1100, 3500, 13, 250000], [950, 3000, 12, 300000], [800, 2500, 16, 180000], [700, 2000, 17, 250000]])
line_labels = np.array(["Criminal Law", "Contract Law", "Tax Law", "Labor Law", "Corporate Law", "Immigration Law", "Family Law", "Intellectual Property Law", "Environmental Law"])

# plot
fig = plt.figure(figsize=(15,10))
ax1 = fig.add_subplot(111)
ax1.bar(line_labels, data[:, 0], width=0.2, color="C2", alpha=0.8, label=data_labels[0])
ax1.set_xlabel("Category")
ax1.set_ylabel("Number of Cases", color="C2")
ax1.tick_params(axis="y", labelcolor="C2")

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:, 1], color="C1", marker="o", linestyle="--", label="Lawyers Involved")
ax2.set_ylabel("Lawyers Involved", color="C1")
ax2.tick_params(axis="y", labelcolor="C1")

ax3 = ax1.twinx()
ax3.spines["right"].set_position(("axes", 1.1))
ax3.plot(line_labels, data[:, 2], color="C3", marker="^", linestyle=":", label="Average Length of Case (Months)")
ax3.set_ylabel("Average Length of Case (Months)", color="C3")
ax3.tick_params(axis="y", labelcolor="C3")

ax4 = ax1.twinx()
ax4.spines["right"].set_position(("axes", 1.2))
ax4.plot(line_labels, data[:, 3], color="C4", marker="s", linestyle="-.", label="Average Cost of Case (Dollars)")
ax4.set_ylabel("Average Cost of Case (Dollars)", color="C4")
ax4.tick_params(axis="y", labelcolor="C4")

ax1.set_title("Legal Affairs Performance Overview")
ax1.grid(alpha=0.5)
ax1.legend(loc="center left", bbox_to_anchor=(0.8, 0.5))
ax2.legend(loc="center left", bbox_to_anchor=(0.8, 0.4))
ax3.legend(loc="center left", bbox_to_anchor=(0.8, 0.3))
ax4.legend(loc="center left", bbox_to_anchor=(0.8, 0.2))

for ax in fig.axes:
    ax.autoscale_view()

plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/34_2023122270030.png")
plt.clf()