import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Transform the given data into variables
y_values = ['Number of Tourists (Millions)', 'Average Expenditure Per Tourist ($)', 'Total Tourism Revenue ($ Billions)']
x_values = ['USA', 'France', 'Spain', 'UK', 'Italy']
data = np.array([[18, 20, 30], [20, 19, 32], [17, 22, 28], [14, 23, 25], [13, 24, 22]], dtype=np.float32)

# Create the figure
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot each column of data
width = depth = 0.8 # dimensions of bars
colors = ['r', 'g', 'b'] # colors for each y_value

for i in range(len(y_values)):
    x = np.arange(len(x_values))
    y = [i] * len(x_values)
    z = np.zeros(len(x_values))
    dx = dy = np.ones(len(x_values)) * width
    dz = data[:, i]
    color = colors[i % len(colors)]
    ax.bar3d(x, y, z, dx, dy, dz, color=color, alpha=0.8)

# Set labels and ticks
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45, ha='right')
ax.set_yticklabels(y_values, ha='left')

ax.set_title('Analysis of Tourism Revenue by Country')

# Save the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/133_202312302235.png')

# Clear the current image state
plt.close()
