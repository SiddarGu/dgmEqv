import matplotlib.pyplot as plt
import numpy as np

# Transform data into three variables: data_labels, data, line_labels
data_labels = ['Number of Cases (Thousands)','Annual Expenditure (Millions of Dollars)','Average Time to Resolution (Days)']
data = np.array([[1205, 22840, 164],
                 [1740, 16760, 203],
                 [1540, 16500, 249],
                 [910, 20500, 137],
                 [560, 18900, 146],
                 [830, 14670, 169],
                 [920, 24270, 352],
                 [410, 6800, 98],
                 [787, 12950, 188],
                 [580, 11340, 273]])
line_labels = ['Criminal Law','Civil Law','Family Law','Corporate Law','Personal Injury Law','Real Estate Law','Intellectual Property Law','Immigration Law','Employment Law','Environmental Law']

# Create figure and add subplot
fig = plt.figure(figsize=(15,10))
ax1 = plt.subplot(111)

# Plot line chart
ax1.plot(line_labels, data[:,0], color='blue', label=data_labels[0])

# Plot bar chart
ax2 = ax1.twinx()
ax2.bar(line_labels, data[:,1], color='red', alpha=0.3, label=data_labels[1])

# Plot scatter chart
ax3 = ax2.twinx()
ax3.scatter(line_labels, data[:,2], color='green', label=data_labels[2])

# Position the y-axes
ax3.spines['right'].set_position(('outward', 60))  

# Setting colors for y-labels
ax1.yaxis.label.set_color('blue')
ax2.yaxis.label.set_color('red')
ax3.yaxis.label.set_color('green')

# Set labels
ax1.set_xlabel('Category')
ax1.set_ylabel(data_labels[0])
ax2.set_ylabel(data_labels[1])
ax3.set_ylabel(data_labels[2])

# Set title
ax1.set_title('A Comprehensive Overview on Law Categories, Expenditures, and Timeframes')

# Set legends
ax1.legend(loc='upper left')
ax2.legend(loc='upper center')
ax3.legend(loc='upper right')

# Background grid 
ax1.grid()

# Set locator
ax1.yaxis.set_major_locator(plt.AutoLocator())
ax2.yaxis.set_major_locator(plt.AutoLocator())
ax3.yaxis.set_major_locator(plt.AutoLocator())

# Add tight layout
plt.tight_layout()

# Save the figure
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/119_202312310108.png")

# Clear the current image state
plt.clf()
