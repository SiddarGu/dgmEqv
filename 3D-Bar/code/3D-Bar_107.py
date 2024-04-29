

import numpy as np
import matplotlib.pyplot as plt

# Transform data into three variables
y_values = ['Total Listings', 'Average Price ($000)', 'Sales Volume (Units)']
data = np.array([[1000, 600, 500],
                 [800, 500, 300],
                 [650, 480, 450],
                 [750, 660, 550]])
x_values = ['North', 'South', 'East', 'West']

# Create figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the data
for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    bottom = 0
    width = depth = 1
    if i == 0:
        top = data[:, i]
        ax.bar3d(xs, ys, bottom, width, depth, top, color='#00B5FF', alpha=0.6)
    elif i == 1:
        top = data[:, i]
        ax.bar3d(xs, ys, bottom, width, depth, top, color='#FFA500', alpha=0.6)
    else:
        top = data[:, i]
        ax.bar3d(xs, ys, bottom, width, depth, top, color='#00FF00', alpha=0.6)

# Rotate X-axis labels
ax.set_xticklabels(x_values, rotation=45)
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values)
ax.set_title('Real Estate Market Overview by Regio')

# Resize image to fit content
plt.tight_layout()

# Save figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/39_202312251044.png')

# Clear current image state
plt.clf()