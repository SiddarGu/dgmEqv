
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd

data_labels = ["Total Research and Development Spending (Millions of Dollars)","Number of Patents Issued","Average Number of Employees"]
line_labels = ["Robotics","Aerospace","Nanotechnology","Automotive","Environmental Engineering","Civil Engineering","Biomedical Engineering","Electrical Engineering","Mechanical Engineering"]
data = np.array([[6750,2400,12450],[7240,3100,12000],[4800,1400,15300],[9150,3200,10500],[3750,1700,17000],[6780,2100,13500],[6300,2500,12000],[8900,3000,11000],[8000,2400,14000]])

fig = plt.figure(figsize=(15,10))
ax1 = fig.add_subplot(111)
ax1.bar(line_labels, data[:,0], width=0.3, color="lightblue", alpha=0.8)
ax1.set_ylabel(data_labels[0], color="lightblue")
ax1.tick_params(axis="y", labelcolor="lightblue")
ax1.set_title("Comprehensive Overview of Science and Engineering Performance")

ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], linestyle="dashed", marker="o", color="orange")
ax2.set_ylabel(data_labels[1], color="orange")
ax2.tick_params(axis="y", labelcolor="orange")

ax3 = ax1.twinx()
ax3.spines["right"].set_position(("axes", 1.1))
ax3.plot(line_labels, data[:,2], linestyle="solid", marker="s", color="green")
ax3.set_ylabel(data_labels[2], color="green")
ax3.tick_params(axis="y", labelcolor="green")
ax3.yaxis.set_label_coords(1.15, 0.5)

ax1.legend(data_labels[0])
ax2.legend(data_labels[1])
ax3.legend(data_labels[2])

ax1.grid()
ax2.grid()
ax3.grid()

ax1.set_xticklabels(line_labels, rotation=90, fontsize=12)
ax1.autoscale()
ax2.autoscale()
ax3.autoscale()

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/16_2023122270030.png')
plt.clf()