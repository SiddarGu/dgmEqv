import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator

data_str = '''Category,Number of Orders,Revenue (USD),Average Order Value (USD),Conversion Rate (%)
Clothing,5000,20000,40,10
Electronics,3000,50000,166.67,8
Home and Kitchen,4000,30000,75,12
Health and Beauty,2000,15000,75,6
Sports and Outdoors,2500,25000,100,10
Toys and Games,1500,10000,66.67,5
Books,1000,5000,50,4
Automotive,1000,10000,100,2
Grocery,3500,17500,50,15
Jewelry,2000,20000,100,8'''

# Process raw data
data_split = [row.split(",") for row in data_str.split("\n")]
data_labels = np.array(data_split[0][1:]).astype(str)
data = np.array([row[1:] for row in data_split[1:]]).astype(float)
line_labels = np.array([row[0] for row in data_split[1:]]).astype(str)

# Create the figure
fig, ax1 = plt.subplots(figsize=(15, 10))

# Plot Bar chart
ax1.bar(line_labels, data[:,0], color='b', alpha=0.5, label=data_labels[0])

ax1.set_ylabel(data_labels[0], color='b')  
ax1.tick_params(axis='y', colors='b')
ax1.yaxis.set_major_locator(AutoLocator())
ax1.grid(True)

# Plot Line chart
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:,1], 'r-', label=data_labels[1])
ax2.set_ylabel(data_labels[1], color='r') 
ax2.tick_params(axis='y', colors='r')
ax2.yaxis.set_major_locator(AutoLocator())

# Plot Line charts
for i in range(2, data.shape[1]):
    ax = ax1.twinx()
    ax.spines['right'].set_position(('outward', (i-1)*60))
    ax.plot(line_labels, data[:,i], label=data_labels[i], color='C{}'.format(i + 2))
    ax.set_ylabel(data_labels[i])
    ax.yaxis.set_major_locator(AutoLocator())
    ax.yaxis.label.set_color('C{}'.format(i + 2))
    ax.tick_params(axis='y', colors='C{}'.format(i + 2))

# Set title
plt.title('Retail and E-commerce Performance Analysis')
ax1.set_xticklabels(line_labels, rotation=45)

# Show and position the legend
fig.legend(loc="upper left", bbox_to_anchor=(0,1), bbox_transform=ax1.transAxes)

# Save the image
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/312_202312311430.png')

# Clear the current figure's state
plt.clf()

