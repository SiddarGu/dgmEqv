

import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels. 
data_labels = ['Revenue (Dollars)','Labour Cost (Dollars)','Profit (Dollars)']
line_labels = ['Automobiles','Electronics','Textiles','Machinery','Chemicals','Pharmaceuticals','Home Appliances','Furniture','Plastics']
data = np.array([[890,87600,7750,19150],[790,56700,5900,9800],[640,45600,5700,11500],[1200,71400,8500,19500],[950,72100,8700,12000],[1010,79200,9000,12500],[1000,75500,8500,15400],[850,64000,7000,13400],[900,68400,7800,14000]])

# Create figure before plotting, i.e., add_subplot(111) follows plt.figure(). The value of figsize should be set larger than 20 to prevent content from being displayed.
fig = plt.figure(figsize=(15, 10))
ax1 = fig.add_subplot(111)
ax2 = ax1.twinx()
ax3 = ax1.twinx()

# Plot the first column of data array, i.e., data[:,0] with bar chart
ax1.bar(line_labels,data[:,0],width=0.3,alpha=0.7,color='#1f77b4',label=data_labels[0])

# Plot the second column of data array, i.e. data[:,1] with line chart
ax2.plot(line_labels,data[:,1],'--',marker='o',color='#ff7f0e',label=data_labels[1])

# Plot the third column of data array, i.e. data[:,2] with scatter chart
ax3.scatter(line_labels,data[:,2],marker='s',color='#2ca02c',label=data_labels[2])

# Label all axes, and match their colors with the data plotted against them.
ax1.set_ylabel(data_labels[0],color='#1f77b4')
ax2.set_ylabel(data_labels[1],color='#ff7f0e')
ax3.set_ylabel(data_labels[2],color='#2ca02c')
ax1.set_xlabel('Category')

# Show the legends of all plots at different positions
ax1.legend(loc='upper left')
ax2.legend(loc='upper center')
ax3.legend(loc='upper right')

# Adjust the positions of bars of different charts by adjusting their positions, i.e., the first parameter in bar()
ax1.set_xticks(np.arange(len(line_labels))+0.3/2)

# Set the alpha parameter smaller than 0.6 for area chart
ax3.fill_between(line_labels,data[:,2],alpha=0.5,color='#2ca02c')

# Using spine() and set_position() for ax3, ax4, ... to seperate different y-axes
ax3.spines['right'].set_position(('axes',1.1))

# Set the title of the figure
plt.title('Manufacturing and Production: Volume, Revenue and Profitability Analysis', fontsize=20)

# Automatically resize the image by tight_layout() before savefig()
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/15_2023122261325.png')

# Clear the current image state
plt.clf()