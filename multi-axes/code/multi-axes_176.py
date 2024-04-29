# Import required libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator

# Define the data
raw_data = """Primary Care,3550,15000,85
Specialty Care,2890,18200,81
Home Health Care,1760,9400,87
Hospitals,6900,50200,79
Pharmaceuticals,5380,28100,82
Mental Health Services,2010,8900,80
Emergency Services,8700,36100,76
Nursing Homes,4600,23800,83
Rehabilitation Services,2570,11100,88
Dental Services,3200,13000,84
Outpatient Care Centers,4000,17000,81
Diagnostic Laboratories,2800,12000,85
Substance Abuse Services,1090,5800,82
Ambulatory Services,4300,18200,86
Hospices,1390,6000,80
Community Health Centers,4360,19100,87"""

# Transform the raw data into numpy array
data_labels = ['Number of Patients (thousands)', 'Total Expenses (Millions)', 'Average Patient Satisfaction(%)']
line_labels = [row.split(',')[0] for row in raw_data.split('\n')]
data = np.array([list(map(int, row.split(',')[1:])) for row in raw_data.split('\n')])

# Create figure
fig = plt.figure(figsize=[24, 10])
ax1 = fig.add_subplot(111)

# Bar chart
ax1.bar(line_labels, data[:, 0], color='b', label=data_labels[0])

# Scatter chart
ax2 = ax1.twinx()
ax2.scatter(line_labels, data[:, 1], color='g', label=data_labels[1])

# Line chart
ax3 = ax1.twinx()
ax3.plot(line_labels, data[:, 2], color='r', label=data_labels[2])

# Area chart
ax4 = ax1.twinx()
ax4.fill_between(line_labels, 0, data[:,2], color='y', alpha=0.5, label=data_labels[2])

# Label axes
ax1.set_ylabel(data_labels[0], color='b')
ax2.set_ylabel(data_labels[1], color='g')
ax3.set_ylabel(data_labels[2], color='r')
ax4.set_ylabel(data_labels[2], color='y')

# Use AutoLocator for all axes
ax1.yaxis.set_major_locator(AutoLocator())
ax2.yaxis.set_major_locator(AutoLocator())
ax3.yaxis.set_major_locator(AutoLocator())
ax4.yaxis.set_major_locator(AutoLocator())

# Position axes
ax3.spines["right"].set_position(("axes", 1.2))
ax4.spines["right"].set_position(("axes", 1.4))

# Add legends
ax1.legend(loc='upper left')
ax2.legend(loc='upper center')
ax3.legend(loc='upper right')
ax4.legend(loc='lower right')

# Add title
plt.title('Comprehensive Analysis of Healthcare Services, Expenditures and Patient Satisfaction')

# Save figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/243_202312311051.png')

# Clear figure
plt.clf()
