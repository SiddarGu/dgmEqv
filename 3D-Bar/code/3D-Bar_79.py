import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Data preparation
data = np.array([
    [31,10,27.5,32],
    [33,12,27.2,33],
    [34.5,15,26.8,34],
    [32.2,17,26.5,35],
    [30.5,20,26,36],
    [28,22,25.5,36.5],
    [26,25,25,37]], dtype=np.float32)

y_values = ['Carbon Emissions (Million Tonnes)',
            'Renewable Energy Utilization (%)',
            'Water Consumption (Billion Cubic Meters)',
            'Forest Coverage Rate (%)']

x_values = ['2015','2016','2017','2018','2019','2020','2021']

# Create a 3D bar chart
fig = plt.figure(figsize=(12,10))
ax = fig.add_subplot(111, projection='3d')

# Plot bar chart
for c, z in enumerate(y_values):
    xs = np.arange(len(x_values))
    ys = data[:,c]
    ax.bar(xs, ys, zs=c, zdir='y', alpha=0.8)

# Set y ticks labels
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, ha='left')

# Set x ticks labels
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation='vertical')

# Set labels and title
ax.set_xlabel('Year')
ax.set_ylabel('Metrics')
ax.set_title('Sustainability Performance Indicators: an evolution from 2015 to 2021')

# Save the output
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/264_202312310050.png', dpi=300)

# Clear current figure
plt.clf()
