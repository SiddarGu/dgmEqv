import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create the data
data_str = 'Year,CO2 Emission (Billion Tonnes),Global Average Temperature (°C),Total Global Forest Area (Billion Acres)\n \
            2018,36.7,14.7,3.1\n 2019,37.1,14.8,3.0\n 2020,34.2,14.8,2.9\n 2021,34.8,14.9,2.8'
data_lines = data_str.split("\n")

x_labels = [line.split(',')[0].strip() for line in data_lines[1:]]
y_labels = data_lines[0].split(',')[1:]
data = np.array([list(map(np.float32, line.split(',')[1:])) for line in data_lines[1:]])

# Create a new figure and add a 3D subplot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot data
for i in range(len(y_labels)):
    ax.bar3d(np.arange(len(x_labels)), [i]*len(x_labels), np.zeros(len(x_labels)), 
        0.5, 0.5, data[:, i], color=(np.random.uniform(0, 1), np.random.uniform(0, 1), np.random.uniform(0, 1)), alpha=0.7)

# Set labels
ax.set_xticks(np.arange(len(x_labels)))
ax.set_yticks(np.arange(len(y_labels)))
ax.set_xticklabels(x_labels, rotation=45, horizontalalignment='right')
ax.set_yticklabels(y_labels, ha='left')

# Set other properties
ax.set_title('Global Environmental and Sustainability Metrics 2018 to 2021')
ax.grid(True)

# Rotate for better view angle
ax.view_init(elev=30., azim=-45)

# Resize to fit all contents
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/123_202312302126.png', format='png', dpi=300)

# Clear the image
plt.clf()
