import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator
import numpy as np

# Given data
data_str = """
Hotels and Resorts,4890,15700,120,65
Local Tours,3270,2200,75,85
Travel Agencies,4360,5450,115,50
Restaurants,8500,19600,70,92
Airline Bookings,9200,13600,150,70
Cruise Lines,2150,8700,210,80
Tourist Attractions,13400,7100,55,78
Car Rentals,3750,4200,20,60
Conferences and Events,1850,3300,290,75
Camping Sites,4020,1230,45,56
Amusement Parks,5520,7800,72,83
Museums and Cultural Sites,6180,1520,30,67
"""
data_lines = data_str.strip().split('\n')
data_labels = ['Number of Tourists (Thousands)', 'Revenue (Millions of Dollars)', 'Average Daily Rate (Dollars)', 'Hotel Occupancy Rate (%)']
line_labels = [line.split(',')[0] for line in data_lines]
data = np.array([line.split(',')[1:] for line in data_lines], dtype=float)

# Create larger figure to prevent content from being displayed cramped
plt.figure(figsize=(21, 9))

# Primary y-axis (Bar chart)
ax1 = plt.subplot(111)
bar_width = 0.2
bar_colors = 'skyblue'
ax1.bar(line_labels, data[:, 0], width=bar_width, color=bar_colors, alpha=0.8, label=data_labels[0])
ax1.tick_params(axis='y', labelcolor=bar_colors)
ax1.set_ylabel(data_labels[0], color=bar_colors)
ax1.yaxis.set_major_locator(AutoLocator())
ax1.set_ylim(ymin=0)

# Secondary y-axis (Line chart)
ax2 = ax1.twinx()
line_colors = 'darkorange'
ax2.plot(line_labels, data[:, 1], color=line_colors, marker='o', label=data_labels[1])
ax2.tick_params(axis='y', labelcolor=line_colors)
ax2.set_ylabel(data_labels[1], color=line_colors)
ax2.yaxis.set_major_locator(AutoLocator())
ax2.set_ylim(ymin=0)

# Third y-axis (Scatter chart)
ax3 = ax1.twinx()
scatter_colors = 'green'
ax3.scatter(line_labels, data[:, 2], color=scatter_colors, alpha=0.8, label=data_labels[2])
ax3.tick_params(axis='y', labelcolor=scatter_colors)
ax3.spines['right'].set_position(('outward', 60))
ax3.set_ylabel(data_labels[2], color=scatter_colors)
ax3.yaxis.set_major_locator(AutoLocator())
ax3.set_ylim(ymin=0)

# Fourth y-axis (Area chart)
ax4 = ax1.twinx()
area_colors = 'purple'
ax4.fill_between(line_labels, 0, data[:, 3], color=area_colors, alpha=0.5, label=data_labels[3])
ax4.tick_params(axis='y', labelcolor=area_colors)
ax4.spines['right'].set_position(('outward', 120))
ax4.set_ylabel(data_labels[3], color=area_colors)
ax4.yaxis.set_major_locator(AutoLocator())
ax4.set_ylim(ymin=0)

# Rotate x-axis labels if too long, wrap if needed
plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45, ha="right")
plt.setp(ax1.xaxis.get_majorticklabels(), wrap=True)

# Set title and show grid
plt.title('Global Trends in Tourism: Visitor Numbers, Revenue, and Accommodation Metrics')
ax1.grid(True)

# Position legends to avoid overlaps
ax1.legend(loc='upper left')
ax2.legend(loc='lower left')
ax3.legend(loc='upper right')
ax4.legend(loc='lower right')

# Automatically resize the image and save it
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/53_2023122291723.png')

# Clear the current figure's state
plt.clf()
