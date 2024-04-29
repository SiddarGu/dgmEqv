
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Transform the given data into three variables: data_labels, data, line_labels 
data_labels = ["Current Carbon Emission (Million of Tonnes of CO2)", "Projected Carbon Emission (Million of Tonnes of CO2)", "Percentage Difference (%)", "Total Renewable Energy Consumption (Trillion kWh)"]
data = np.array([[6.90, 8.24, 19.5, 1.22], [8.25, 9.99, 21.0, 0.65], [3.45, 4.30, 24.3, 0.32], [2.41, 2.97, 22.9, 0.22], [5.13, 5.90, 15.1, 3.90], [0.30, 0.35, 16.7, 0.05]])
line_labels = ["Transportation", "Industrial", "Residential", "Commercial", "Agriculture", "Fishing"]

# Plot the data with the type of multi-axes chart
fig = plt.figure(figsize=(15, 10))
ax1 = fig.add_subplot(111)

# Plot the first column of data array, i.e., data[:,0]
ax1.bar(line_labels, data[:, 0], width=0.2, color="b", alpha=0.8)
ax1.set_ylabel(data_labels[0], color="b")
ax1.tick_params(axis="y", labelcolor="b")

# The second column of data array, i.e. data[:,1]
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:, 1], color="r", marker="o", linestyle="--")
ax2.set_ylabel(data_labels[1], color="r")
ax2.tick_params(axis="y", labelcolor="r")

# The third column of data array (if possible), i.e. data[:,2]
ax3 = ax1.twinx()
ax3.spines["right"].set_position(("axes", 1.1))
ax3.plot(line_labels, data[:, 2], color="g", marker="s", linestyle="-.")
ax3.set_ylabel(data_labels[2], color="g")
ax3.tick_params(axis="y", labelcolor="g")

# The fourth column of data array (if possible), i.e. data[:,3]
ax4 = ax1.twinx()
ax4.spines["right"].set_position(("axes", 1.2))
ax4.plot(line_labels, data[:, 3], color="k", marker="d", linestyle=":")
ax4.set_ylabel(data_labels[3], color="k")
ax4.tick_params(axis="y", labelcolor="k")

# Label all axes
ax1.set_xlabel("Category")
ax1.set_title("Environmental Sustainability: Current and Projected Carbon Emissions and Renewable Energy Consumption")

# Show the legends of all plots at different positions
ax1.legend(data_labels[0], loc="upper right", bbox_to_anchor=(1.25, 1.0))
ax2.legend(data_labels[1], loc="upper right", bbox_to_anchor=(1.25, 0.9))
ax3.legend(data_labels[2], loc="upper right", bbox_to_anchor=(1.25, 0.8))
ax4.legend(data_labels[3], loc="upper right", bbox_to_anchor=(1.25, 0.7))

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
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/3_202312251608.png")

# Clear the current image state at the end of the code
plt.clf()