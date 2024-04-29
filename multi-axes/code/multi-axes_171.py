import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

# Date preprocess
records = ['January,15400,10200,120,4000','February,16780,12800,150,5000','March,21400,16300,200,7000','April,24800,17800,250,12000',                      
           'May,29800,24500,300,20000','June,32500,27600,350,25000','July,36400,30500,400,30000','August,41200,35500,450,35000',                       
           'September,38900,31900,400,32000','October,33800,27500,350,28000','November,26800,21000,300,21000','December,19800,15500,250,18000']
data_labels = ['Number of Tourists','Hotel Bookings','Average Spend Per Day (Dollars)','Tourist Attractions Visited']
data = np.array([list(map(int, record.split(',')[1:])) for record in records])
line_labels = [record.split(',')[0] for record in records]

# Create subplots
fig, ax1 = plt.subplots(figsize=(20,10))

# Plot line chart
ax1.plot(line_labels, data[:,0], 'm-', label=data_labels[0])
ax1.set_ylabel(data_labels[0], color='m')

# Create another y-axis for the bar chart
ax2 = ax1.twinx()
ax2.bar(line_labels, data[:,1], width=0.4, color='r', alpha=0.7, label=data_labels[1], align='center')
ax2.set_ylabel(data_labels[1], color='r')

# Create another y-axis for the scatter chart
ax3 = ax1.twinx()
ax3.scatter(line_labels, data[:,2], color='b', label=data_labels[2])
ax3.set_ylabel(data_labels[2], color='b')

# To avoid overlapping of y-axes
ax3.spines['right'].set_position(('outward', 70))

# Create another y-axis for the area chart
ax4 = ax1.twinx()
ax4.fill_between(line_labels, data[:,3], color='g', alpha=0.5, label=data_labels[3])
ax4.set_ylabel(data_labels[3], color='g')

# To avoid overlapping of y-axes
ax4.spines['right'].set_position(('outward', 140))

# Title
plt.title('Tourism and Hospitality Trends: Visitor Count, Hotel Bookings, Spending, and Attractions')

# Legends
fig.legend(loc="upper left", bbox_to_anchor=(0,1), bbox_transform=ax1.transAxes)

# Grid
ax1.grid()

# Save figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/127_202312310108.png')

# Clear the current image state
plt.clf()
