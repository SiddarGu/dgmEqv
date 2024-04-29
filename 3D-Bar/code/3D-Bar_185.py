import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the data
data = np.array([
    [120, 150, 180],
    [110, 160, 190],
    [135, 155, 200],
    [140, 165, 220],
    [120, 180, 230]
])

# Define the y_values and x_values
y_values = ['Movie Ticket Sales (Millions)', 'Sports Ticket Sales (Millions)', 'Music Concert Ticket Sales (Millions)']
x_values = ['January', 'February', 'March', 'April', 'May']

# Create a new figure and add a 3D subplot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot each column of data
for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 0.4, 0.5, data[:, i], alpha=0.5)

# Set the x and y ticks and labels
ax.set_xticks(range(len(x_values)))
ax.set_yticks(range(len(y_values)))
ax.set_xticklabels(x_values, rotation=30)
ax.set_yticklabels(y_values, ha='left')

# Set the title
ax.set_title('Monthly Comparison of Tickets Sales in Sports and Entertainment Industry')

# Save the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/238_202312310050.png', dpi=300)

# Clear the current figure
plt.clf()
