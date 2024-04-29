
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Transform the given data into three variables
data_labels = ['Fines (Millions of Dollars)','Cases Filed (Thousands)','Average Fines per Case (Dollars)']
line_labels = ['Regulatory Issues','Contract Disputes','Property Disputes','Labour Law','Tax Law','Criminal Law','Environmental Law','Immigration Law','Intellectual Property','Family Law']
data = np.array([[3.8,1.2,3200],[2.4,0.9,2700],[1.2,0.6,2000],[1.7,0.8,2100],[2.1,1.0,2100],[3.9,2.0,1850],[1.6,0.8,2000],[2.0,1.1,1800],[2.5,1.3,1800],[1.3,0.7,1900]])

# Create figure
fig = plt.figure(figsize=(15, 8))
ax1 = fig.add_subplot(111)

# Plot the first column of data array
ax1.bar(line_labels,data[:,0], label=data_labels[0], color='green')
ax1.set_xlabel('Category')
ax1.set_ylabel(data_labels[0], color='green')
ax1.tick_params(axis='y', labelcolor='green')

# Overlay a new ax on the first plot
ax2 = ax1.twinx()

# Plot the second column of data array
ax2.plot(line_labels,data[:,1], label=data_labels[1], color='blue', marker='o')
ax2.set_ylabel(data_labels[1], color='blue')
ax2.tick_params(axis='y', labelcolor='blue')

# Overlay a third ax on the first plot
ax3 = ax1.twinx()

# Plot the third column of data array
ax3.plot(line_labels,data[:,2], label=data_labels[2], color='red', marker='^', linestyle='--')
ax3.set_ylabel(data_labels[2], color='red')
ax3.tick_params(axis='y', labelcolor='red')

# Seperate different y-axes
ax3.spines['right'].set_position(('axes', 1.1))

# Create legend
ax1.legend(loc='upper left')
ax2.legend(loc='upper center')
ax3.legend(loc='upper right')

# Set title
ax1.set_title('Legal System Performance Analysis: Fines, Cases Filed, and Cost per Case')

# Auto adjust the range of all y-axes
ax1.autoscale()
ax2.autoscale()
ax3.autoscale()

# Automatically resize the image
plt.tight_layout()

# Save figure
fig.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/25_2023122270030.png')

# Clear the current image state
plt.clf()