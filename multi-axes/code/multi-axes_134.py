import matplotlib.pyplot as plt
import numpy as np
import csv

# Prepare the data
data = """Chemical Compound,Energy Output (kJ/mol),Melting Point (°C),Density (g/cm³)
Water,285.8,0,1
Ethanol,1366.2,-114,0.79
Sodium Chloride,782.5,801,2.17
Methane,882.8,-182.5,0.67
Nitrogen,472.1,-210,1.25
Copper Sulfate,2363,110,3.6
Silver,334.6,960,10.5
Oxygen,498,-218.4,1.31
Carbon Dioxide,-393.5,-57,1.98
Titanium,473,1660,4.5
Aluminum,-943.5,660,2.7
Sulfur,-221,115.2,2.07
Carbon,394,3550,3.5
Gold,-68,1064,19.3
Iron,-275,1535,7.86
Silicon,-911,1410,2.33
Uranium,-2218,1132,19.1
Zinc,-213,420,7.14
Lead,-24.2,327,11.34"""
data = list(csv.reader(data.split('\n')))
line_labels = [row[0] for row in data[1:]]
data_labels = data[0][1:]
data = np.array([list(map(float, row[1:])) for row in data[1:]])


# Create the figure
fig = plt.figure(figsize=(25,10))
ax1 = fig.add_subplot(111)

# Plot the data
ax1.set_xlabel('Chemical Compounds')
ax1.set_ylabel(data_labels[0])
ax1.plot(line_labels, data[:,0], 'r-', label=data_labels[0])
ax1.tick_params(axis='y', labelcolor='r')

# Create a second y-axis
ax2 = ax1.twinx()
ax2.set_ylabel(data_labels[1])
ax2.scatter(line_labels, data[:,1], color='g', label=data_labels[1])
ax2.tick_params(axis='y', labelcolor='g')

# Create a third y-axis
ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60))
ax3.set_ylabel(data_labels[2])
ax3.bar(line_labels, data[:,2], color='b', alpha=0.3, width=0.4, label=data_labels[2])
ax3.tick_params(axis='y', labelcolor='b')

# Legend
fig.legend(loc="upper left", bbox_to_anchor=(0,1), bbox_transform=ax1.transAxes)

plt.xticks(rotation=45)
plt.title('Chemical Compound Properties: Energy Output, Melting Point, and Density')
plt.tight_layout()
plt.grid(True)
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/298_202312311430.png')
plt.cla()
plt.close()
