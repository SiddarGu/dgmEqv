

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# transform the given data into three variables
data_labels = ['Cases Resolved (Thousands)', 'Lawsuits Filed (Thousands)', 'Average Sentence (Years)']
line_labels = ['Civil Cases', 'Criminal Cases', 'Contractual Disputes', 'Intellectual Property', 'Family Law', 'Bankruptcy', 'Immigration', 'Regulatory Violations', 'Administrative Law']
data = np.array([[120,90,2.5], [150,100,4], [90,70,3], [30,50,1.5], [80,120,2], [20,30,1], [40,50,2.2], [50,60,1.8], [20,30,1.5]])

# create figure before plotting
fig = plt.figure(figsize=(15,10))
ax1 = fig.add_subplot(111)

# draw multi-axes chart
# plot the first column data with bar chart
ax1.bar(line_labels, data[:,0], color='#3F51B5', width=0.45, alpha=0.8, label=data_labels[0])
ax1.set_ylabel(data_labels[0], color='#3F51B5', fontsize=12)
ax1.tick_params(axis='y', labelcolor='#3F51B5', labelsize=12)
ax1.set_xticklabels(line_labels, rotation=45, fontsize=12)
ax1.grid(color='#EEEEEE', linestyle='-', linewidth=1)
ax1.set_title("Law and Legal Affairs Performance Overview", fontsize=14)

# plot the second column data with line chart
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], color='#FF5722', linestyle='--', marker='o', linewidth=2, label=data_labels[1])
ax2.set_ylabel(data_labels[1], color='#FF5722', fontsize=12)
ax2.tick_params(axis='y', labelcolor='#FF5722', labelsize=12)

# plot the third column data with area chart
ax3 = ax1.twinx()
ax3.fill_between(line_labels, 0, data[:,2], facecolor='#4CAF50', alpha=0.6, label=data_labels[2])
ax3.set_ylabel(data_labels[2], color='#4CAF50', fontsize=12)
ax3.tick_params(axis='y', labelcolor='#4CAF50', labelsize=12)
ax3.spines['right'].set_position(('axes', 1.1))

# show legend
ax1.legend(loc='upper left', bbox_to_anchor=(0.05, 0.95), ncol=3, fontsize=12)

# adjust range of all y-axes
ax1.autoscale(axis='y', tight=True)
ax2.autoscale(axis='y', tight=True)
ax3.autoscale(axis='y', tight=True)

# automatically resize the image
plt.tight_layout()

# save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/31_2023122270030.png')

# clear the current image state
plt.clf()