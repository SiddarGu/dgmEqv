import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parse the provided data
data_string = 'Year,Film Industry Revenue (Billion $),Music Industry Revenue (Billion $),Video Games Industry Revenue (Billion $)/n 2018,136,20,134.9/n 2019,101,21,152.1/n 2020,85,22,159.3/n 2021,112,23,174.9/n 2022,115,24,189.5'
data_lines = data_string.split('/n')
header = data_lines.pop(0)
y_values = header.split(',')[1:]
x_values = [line.split(',')[0] for line in data_lines]
data_arrays = [np.float32(line.split(',')[1:]) for line in data_lines]
data = np.array(data_arrays)

# Create plot
fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot(111, projection='3d')

for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), np.array([i]*len(x_values)), np.zeros(len(x_values)), 
             0.4, 0.5, data[:, i], alpha=0.4, color=np.random.rand(3,))

# Set labels and title
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45, ha='right')
ax.set_yticklabels(y_values, ha='left')
plt.title('Revenue Trends in Entertainment Industry from 2018 to 2022')

# Adjust viewing angle
ax.view_init(elev=10., azim=-30)

# Save plot
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/271_202312310050.png', dpi=300)

# Finally, clear figure
plt.clf()
