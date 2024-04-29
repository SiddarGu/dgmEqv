import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoLocator

# Parse the data & labels
data_string = 'USA,2000,500,60000; UK,1590,350,43000; China,2150,650,5000; India,1850,470,3000; Germany,1100,300,20000; Australia,1200,270,35000; France,1550,400,23000; Canada,1380,330,26000; Brazil,950,230,1000; Japan,1050,280,8000'

row_strings = data_string.split('; ')
data = []
line_labels = []
for row in row_strings:
    row_data = row.split(',')
    line_labels.append(row_data[0])
    data.append(list(map(int, row_data[1:])))

data_labels = ['Number of Students (1000s)', 'Number of Professors (100s)', 'Average Tuition Fee ($)']

# Create figure and subplots
fig = plt.figure(figsize=(25,15))
ax1 = fig.add_subplot(111)

# Plot bar chart for the first column of data
ax1.bar(np.arange(len(data)), [row[0] for row in data], color='b', label=data_labels[0])
ax1.set_ylabel(data_labels[0], color='b')
ax1.tick_params(axis='y', labelcolor='b')

# Plot another bar chart for the second column of data on a new y axis
ax2 = ax1.twinx()
ax2.bar(np.arange(len(data)) + 0.4, [row[1] for row in data], color='r', width=0.4, label=data_labels[1])
ax2.set_ylabel(data_labels[1], color='r')
ax2.tick_params(axis='y', labelcolor='r')

# Plot an area chart for the third column of data on a new y axis
ax3 = ax1.twinx()
ax3.plot(np.arange(len(data)), [row[2] for row in data], color='g', alpha=0.5, label=data_labels[2])
ax3.fill_between(np.arange(len(data)), [row[2] for row in data], color='g', alpha=0.3)
ax3.set_ylabel(data_labels[2], color='g')
ax3.spines["right"].set_position(("axes", 1.1))
ax3.tick_params(axis='y', labelcolor='g')

# Set the shared x axis
ax1.set_xticks(np.arange(len(data)))
ax1.set_xticklabels(line_labels, rotation=45, ha='right')
plt.title('Comparative Study of Higher Education in Social Sciences and Humanities Across Different Countries')

# Add legends
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
ax3.legend(loc='center right')

# Update y axes range
ax1.yaxis.set_major_locator(AutoLocator())
ax2.yaxis.set_major_locator(AutoLocator())
ax3.yaxis.set_major_locator(AutoLocator())

# Save to file
plt.tight_layout() 
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/180_202312310150.png')
plt.close(fig) 
