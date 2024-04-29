

import matplotlib.pyplot as plt
import numpy as np

# Transform data into multiple variables
data_labels = ["Number of Participants", "Number of Events", "Average Event Duration (Hours)"]
line_labels = ["Music","Dance","Film","Theatre","Visual Arts","Literary Arts","Street Arts","Arts Festivals","Traditional Arts","Pop Culture","Multimedia Arts"]
data = np.array([[34500,1200,10],[23000,800,8],[20000,900,9],[15000,600,7],[8000,400,6],[6000,400,5],[12000,900,7],[25000,1000,9],[18000,700,8],[30000,1200,10],[10000,500,6]])

# Plot the data
plt.figure(figsize=(15,10))
ax1 = plt.subplot(111)
ax1.bar(line_labels, data[:,0], width=0.2, color="orange", alpha=0.6, label=data_labels[0])
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], color="b", marker="o", linestyle="--", label=data_labels[1])
ax3 = ax1.twinx()
ax3.spines["right"].set_position(("axes", 1.2))
ax3.plot(line_labels, data[:,2], color="g", marker="o", linestyle="-.", label=data_labels[2])

# Set axes labels
ax1.set_xlabel("Category", fontsize=14)
ax1.set_ylabel(data_labels[0], fontsize=14, color="orange")
ax2.set_ylabel(data_labels[1], fontsize=14, color="b")
ax3.set_ylabel(data_labels[2], fontsize=14, color="g")

# Set legend
ax1.legend(bbox_to_anchor=(0.1, 0.9))
ax2.legend(bbox_to_anchor=(0.5, 0.9))
ax3.legend(bbox_to_anchor=(0.8, 0.9))

# Adjust Y-axes
plt.autoscale()

# Title the figure
plt.title("Arts and Culture Participation and Event Trends", fontsize=16)

# Resize the image
plt.tight_layout()

# Save the figure
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/2_2023122270030.png")

# Clear the current image state
plt.clf()