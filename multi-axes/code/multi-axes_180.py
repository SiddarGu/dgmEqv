
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# transform data to variables
data_labels = ["Category", "Concentration of Carbon Dioxide (ppm)", "Greenhouse Gas Emissions (Gigatons of CO2)", "Water Quality Index"]
line_labels = ["Air Quality", "Water Quality", "Soil Quality", "Waste Management", "Renewable Energy", "Biodiversity"]
data = np.array([[410, 34.2, 50], [7.2, 2.8, 79], [140, 1.5, 65], [8.3, 3.2, 92], [2.4, 0.5, 80], [10.1, 1.7, 71]])

# split data
data_1 = data[:,0]
data_2 = data[:,1]
data_3 = data[:,2]

# plot data
fig, ax = plt.subplots(figsize=(10,6))
ax.set_title('Environmental Sustainability: Air, Water, Soil, Waste, and Renewable Energy Trends')

ax.bar(line_labels, data_1, color='red', alpha=0.7, label=data_labels[1], align='edge')
ax.set_xlabel(data_labels[0])
ax.set_xticklabels(line_labels, rotation=45)
ax.set_ylabel(data_labels[1], color='red', fontsize=12)
ax.tick_params(axis='y', labelcolor='red')

# add a second y-axis on the right side of the plot
ax_2 = ax.twinx()
ax_2.set_ylabel(data_labels[2], color='blue', fontsize=12)
ax_2.plot(line_labels, data_2, color='blue', marker='s', alpha=0.7)
ax_2.tick_params(axis='y', labelcolor='blue')

# add a third y-axis on the right side of the plot
ax_3 = ax.twinx()
ax_3.spines["right"].set_position(("axes", 1.1))
ax_3.set_ylabel(data_labels[3], color='green', fontsize=12)
ax_3.plot(line_labels, data_3, color='green', marker='o', alpha=0.7)
ax_3.tick_params(axis='y', labelcolor='green')

plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/10.png")
plt.clf()