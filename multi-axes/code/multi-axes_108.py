import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator
import random

# Given data
str_data = "Year,Number of Cases,Legal Expenditure (Millions),Average Case Duration (Days)/n 2015,300,500,90/n 2016,320,530,95/n 2017,350,560,100/n 2018,400,600,105/n 2019,450,650,110/n 2020,500,700,115"
str_data = str_data.replace("/n", "\n")

# Convert the data to list format and split columns and rows
data_list = [line.split(",") for line in str_data.split("\n")]
data_list = np.array(data_list)

# Prepare the data_labels, data, and line_labels
data_labels = data_list[0, 1:]
line_labels = data_list[1:, 0]
data = data_list[1:, 1:].astype(np.float32)

# Plot parameters
colors = ['#008fd5', '#fc4f30', '#6d904f']
fig = plt.figure(figsize=(20, 10))

ax1 = fig.add_subplot(111)
ax1.plot(line_labels, data[:, 0], label=data_labels[0], color=colors[0])
ax1.set_xlabel(data_list[0, 0])
ax1.set_ylabel(data_labels[0], color=colors[0])
ax1.tick_params('y', colors=colors[0])
ax1.yaxis.set_major_locator(AutoLocator())

ax2 = ax1.twinx()
ax2.bar(line_labels, data[:, 1], label=data_labels[1], color=colors[1], alpha=0.7)
ax2.set_ylabel(data_labels[1], color=colors[1])
ax2.tick_params('y', colors=colors[1])
ax2.yaxis.set_major_locator(AutoLocator())

ax3 = ax1.twinx()
ax3.scatter(line_labels, data[:, 2], label=data_labels[2], color=colors[2])
ax3.spines['right'].set_position(('outward', 60))
ax3.set_ylabel(data_labels[2], color=colors[2])
ax3.tick_params('y', colors=colors[2])
ax3.yaxis.set_major_locator(AutoLocator())

plt.grid(True)
plt.title("Law and Legal Affairs: Trends in Cases, Expenditures and Duration")
fig.legend(loc="upper right", bbox_to_anchor=(1,1), bbox_transform=ax1.transAxes)

plt.tight_layout()

# save path
save_path = "/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/227_202312311051.png"
plt.savefig(save_path, format='png')

# clear figure
plt.clf()
plt.close()
