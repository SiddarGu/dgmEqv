# Redoing the 3D bar plot as requested

import numpy as np
import matplotlib.pyplot as plt

# Data
y_values = ['Number of Museums', 'Number of Theatres', 'Number of Art Galleries', 'Number of Concerts']
data = np.array([[20, 50, 100, 300], [18, 60, 110, 250], [15, 70, 120, 280], [17, 40, 90, 320]])
x_values = ['Visual Arts', 'Performing Arts', 'Literary Arts', 'Music']

# Create figure
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Colors for each bar group
colors = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00']

# Plotting the data
for i in range(len(x_values)):
    ax.bar3d(i, np.arange(len(y_values)), np.zeros(len(y_values)), 0.8, 0.8, data[i, :], color=colors[i], shade=True)

# Setting the ticks and labels
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=17, fontsize=12)
ax.set_yticklabels(y_values, fontsize=12, ha='left')

# Adding title and adjusting layout
ax.set_title('Arts and Culture - A Comprehensive Look', fontsize=16)
plt.tight_layout()

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/1_202312251000.png')

# clear the current state
plt.clf()