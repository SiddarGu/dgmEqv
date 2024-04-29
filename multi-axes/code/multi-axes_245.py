
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator

data_labels = ['Category', 'Volume of Tourists (Thousands)', 'Total Tourism Spending (Millions of Dollars)', 'Average Length of Stay (Nights)']
data = np.array([[550,4500,14],[750,8900,11],[210,2600,4],[900,11300,7],[340,4500,10],[150,3400,20],[690,7200,12],[120,1800,9],[230,3000,14],[180,2200,8]])
line_labels = ['Domestic', 'International', 'Cruise', 'Business', 'Adventure', 'Luxury', 'Cultural', 'Eco-tourism', 'Educational', 'Medical']

# split the data array from the second dimension
column1 = data[:,0]
column2 = data[:,1]
column3 = data[:,2]

# decide plot types
plot_types = ['bar', 'line', 'scatter']

# create figure before plotting
fig, ax1 = plt.subplots(figsize=(12, 6))

# plot the bar chart
ax1.bar(line_labels, column1, width=0.2, color='#F4511E', label = data_labels[1], alpha=0.5)

# plot the line chart
ax2 = ax1.twinx() 
ax2.plot(line_labels, column2, linestyle='-', marker='o', color='#039BE5', label=data_labels[2])

# plot the scatter chart
ax3 = ax1.twinx()
ax3.scatter(line_labels, column3, linestyle='-', marker='*', color='#7CB342', label=data_labels[3])

# label each axis with the name of the category
ax1.set_ylabel(data_labels[1], color='#F4511E')
ax2.set_ylabel(data_labels[2], color='#039BE5')
ax3.set_ylabel(data_labels[3], color='#7CB342')

# ensure each y-axis does not overlap with each other
ax3.spines["right"].set_position(("axes", 1.1))
# add a legend to the chart
ax1.legend(loc="upper left")
ax2.legend(loc="upper right")
ax3.legend(loc="lower right")
# set title of the figure
ax1.set_title('Tourism and Hospitality Overview: Visitor Activity, Spending, and Length of Stay', fontsize=12)

# Automatically adjust the range of each y-axis
ax1.yaxis.set_minor_locator(AutoMinorLocator())
ax2.yaxis.set_minor_locator(AutoMinorLocator())
ax3.yaxis.set_minor_locator(AutoMinorLocator())

# Automatically resize the image
plt.tight_layout()

# savefig
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/2.png')

# clear the current image state
plt.clf()