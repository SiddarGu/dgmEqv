import matplotlib.pyplot as plt
import numpy as np

# Data
data = np.array([[2000, 47, 3912, 16000, 37100], [2005, 45, 4060, 15700, 38200],
                 [2010, 42, 4230, 14300, 39800], [2015, 39, 4390, 12500, 41700],
                 [2020, 35, 4578, 11000, 43800]])

line_labels = data[:, 0]
data = data[:, 1:]
data_labels = ['Air Pollution (Micrograms per cubic meter)', 'Water Consumption (Billions of cubic meters)',
               'Deforestation (Square km)', 'Global Warming Potential (Million metric tons of CO2 equivalent)']

# Create figure and add axes
fig = plt.figure(figsize=(26, 10))
ax1 = fig.add_subplot(111)

# Plot data on each axes
ax1.plot(line_labels, data[:, 0], color='b', label=data_labels[0])
ax2 = ax1.twinx()
ax2.plot(line_labels, data[:, 1], color='g', label=data_labels[1])

ax3 = ax1.twinx()
ax3.fill_between(line_labels, 0, data[:, 2], color='r', alpha=0.4, label=data_labels[2])
ax3.spines['right'].set_position(('outward', 60))

ax4 = ax1.twinx()
ax4.bar(line_labels, data[:, 3], color='c', alpha=0.5, width=0.8, label=data_labels[3])
ax4.spines['right'].set_position(('outward', 120))

# Set labels and title
ax1.set_xlabel('Year')
ax1.set_ylabel(data_labels[0], color='b')
ax2.set_ylabel(data_labels[1], color='g')
ax3.set_ylabel(data_labels[2], color='r')
ax4.set_ylabel(data_labels[3], color='c')

plt.title('Progression of Key Environmental and Sustainability Metrics from 2000 to 2020')

# Show legends
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
ax3.legend(loc='center left')
ax4.legend(loc='center right')

# Set grid
ax1.grid()

# Automatically adjust subplot
plt.tight_layout()

# Save and show figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/251_202312311051.png')

# Clear the current figure
plt.clf()
