import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator

# Set the data
data_csv = "Organization,Donations Received (in $1000),Number of Volunteers,Number of Beneficiaries\n Health and Wellbeing Charity,500,200,3000\n Children's Aid Organization,450,150,2500\n Disaster Relief Fund,600,250,4000\n Animal Welfare Association,350,120,1500\n Environmental Nonprofit,400,180,2000\n Educational Charity,550,300,3500\n Housing and Shelter Charity,480,220,3300\n Arts and Culture Foundation,420,160,2700\n Food Bank,520,200,2900\n Women's Empowerment Organization,460,210,2800"
data_lines = data_csv.split("\n")
data_labels = data_lines[0].split(",")[1:]
data = np.array([list(map(float, line.split(",")[1:])) for line in data_lines[1:]])
line_labels = [line.split(",")[0] for line in data_lines[1:]]

# Create the figure and subplots
fig = plt.figure(figsize=(25, 12))
ax1 = fig.add_subplot(111)

# Plot the data
positions = np.arange(len(line_labels))
bar_width = 0.25
ax1.bar(positions - bar_width, data[:,0], width=bar_width, color='red', alpha=0.7)

# Overlay ax2
ax2 = ax1.twinx()
ax2.bar(positions, data[:,1], width=bar_width, color='blue', alpha=0.7)

# Overlay ax3
ax3 = ax2.twinx()
ax3.plot(positions, data[:,2], color='green')
ax3.spines['right'].set_position(('outward', 60)) 

# Set the x-axis
plt.xticks(positions, line_labels, rotation='vertical')

# Set the y-axis
ax1.set_ylabel(data_labels[0], color='red')
ax2.set_ylabel(data_labels[1], color='blue')
ax3.set_ylabel(data_labels[2], color='green')

# Auto adjust the range of y-axis 
ax1.yaxis.set_minor_locator(AutoMinorLocator())
ax2.yaxis.set_minor_locator(AutoMinorLocator())
ax3.yaxis.set_minor_locator(AutoMinorLocator())

# Add legends
ax1.legend([data_labels[0]], loc='upper left')
ax2.legend([data_labels[1]], loc='upper right')
ax3.legend([data_labels[2]], loc='center right')

# Add title
plt.title('Analysis of Charity and Nonprofit organizations\' Performance')

# Add grid
plt.grid(True)
 
# Save the figure
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/159_202312310108.png")

# Clear the current figure
plt.clf()
