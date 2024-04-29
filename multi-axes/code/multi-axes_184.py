import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# split and arrange the data
data_raw = """Category,Average Distance Traveled (Miles),Average Fuel Efficiency (Miles per Gallon),Fuel Cost (Dollars)
Car, 25, 30, 60
Truck, 100, 10, 120
Train, 500, 50, 200
Ship, 1000, 100, 500
Airplane, 10000, 200, 2000"""
data_row = data_raw.split('\n')

# Extract data_labels, line_labels and data arrays from the raw data
data_labels = data_row[0].split(',')
line_labels = [i.split(',')[0] for i in data_row[1:]]
data = np.array([i.split(',')[1:] for i in data_row[1:]], dtype=float).T

# set the size of the figure
fig = plt.figure(figsize=(30, 20))

# plotting data[:,0] with a unique y-axis
ax1 = fig.add_subplot(111)  
ax1.bar(line_labels, data[0], color='b', alpha=0.7, label=data_labels[1])
ax1.set_xlabel(data_labels[0])
ax1.set_ylabel(data_labels[1], color='b')
ax1.tick_params(axis='y', colors='b')
ax1.yaxis.set_major_locator(ticker.AutoLocator())

# overlay ax2 to share x-axis with ax1 
ax2 = ax1.twinx()
ax2.bar(line_labels, data[1], color='r', alpha=0.7, label=data_labels[2], width=0.4, align='center')
ax2.set_ylabel(data_labels[2], color='r')
ax2.tick_params(axis='y', colors='r')
ax2.yaxis.set_major_locator(ticker.AutoLocator())
ax2.spines['right'].set_position(('outward', 60)) 

# overlay ax3 to share x-axis with ax1
ax3 = ax1.twinx()
ax3.bar(line_labels, data[2], color='g', alpha=0.7, label=data_labels[3], width=0.4, align='edge')
ax3.set_ylabel(data_labels[3], color='g')
ax3.tick_params(axis='y', colors='g')
ax3.yaxis.set_major_locator(ticker.AutoLocator())
ax3.spines['right'].set_position(('outward', 120))   

plt.title("Fuel Efficiency and Cost Comparison across Transportation Modes") 

# showing all legends at different position
fig.legend(loc="upper left", bbox_to_anchor=(0,1), bbox_transform=ax1.transAxes)

# Automatically resize the image
plt.tight_layout()

# saving the file
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/331_202312311430.png')

# clear the current image state
plt.clf() 
