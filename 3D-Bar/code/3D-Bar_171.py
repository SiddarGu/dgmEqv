import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Prepare data
original_data = 'Country,Number of Universities,Number of Students (Millions),Education Budget ($ Billions)\n USA,15.71,20.5,75.6\n UK,13,2.3,15.2\n Australia,4.3,1.5,14.6\n Canada,9.6,2.1,23.4\n Germany,40,2.8,16.3'
data_lines = original_data.split('\n')
x_values = [line.split(',')[0] for line in data_lines[1:]]
y_values = data_lines[0].split(',')[1:]
data = np.array([list(map(np.float32, line.split(',')[1:])) for line in data_lines[1:]])

# Create 3D plot
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(projection='3d')

# Plot data
for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 0.4, 0.8, data[:, i], color='b', alpha=0.5)

# Set labels
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=45, ha='right')
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, ha='left')

# Set title
plt.title('Comparative Analysis of Higher Education Across Countries')

# Adjust view for better readability
ax.view_init(elev=20., azim=-35)

# Auto adjust labels
plt.tight_layout()

# Save figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/137_202312302235.png')

# Clear current figure
plt.clf()
