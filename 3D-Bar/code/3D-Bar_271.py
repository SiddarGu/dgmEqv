import matplotlib.pyplot as plt
import numpy as np

# Initialize the data
data = np.array([
    [30, 75, 350],
    [28, 70, 330],
    [31, 80, 360],
    [27, 72, 320],
    [33, 83, 380],
    [29, 75, 335]
], dtype=np.float32)

x_values = ['January', 'February', 'March', 'April', 'May', 'June']
y_values = ['Total Shipments (in \'000)', 'Freight Cost ($M)', 'Number of Dispatched Units (in \'000)']

# Create the figure
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

colors = ['r', 'g', 'b']
yticks = np.arange(len(y_values))
xticks = np.arange(len(x_values))

# Plot the data
for i in range(data.shape[1]):
    ax.bar3d(xticks, [i]*len(xticks), np.zeros(len(x_values)), 0.6, 0.6, data[:, i], color=colors[i], alpha=0.8)

ax.set_xticks(xticks)
ax.set_xticklabels(x_values, rotation=45, ha='right')

ax.set_yticks(yticks)
ax.set_yticklabels(y_values, ha='left')

ax.set_zlim([0, np.max(data)])

ax.set_title('Monthly Trends in Transportation and Logistics')
ax.grid(True)

# Save image
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/147_202312302235.png', format='png')

# Clear current image
plt.clf()
