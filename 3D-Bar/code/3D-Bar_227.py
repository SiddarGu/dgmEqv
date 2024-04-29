
import numpy as np
import matplotlib.pyplot as plt

# Transform data into variables
y_values = ['Hotel Rooms (Thousands)', 'Average Hotel Rate ($)', 'Average Restaurant Spending ($)']
x_values = ['North', 'South', 'East', 'West']
data = np.array([[20, 30, 50], [30, 62, 60], [40, 65, 70], [50, 63, 80]])

# Create 3D figure
fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot(111, projection='3d')

# Plot data
for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    ax.bar3d(xs, ys, np.zeros(len(x_values)), 1, 1, data[:,i], shade=True, color='b', alpha=0.9)

# Set X-axis and Y-axis labels
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values)
ax.set_yticklabels(y_values, ha='left')
ax.set_xlabel('Region')
ax.xaxis.labelpad = 15
ax.set_title('Trend Analysis of the Tourism and Hospitality Industry by Region')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/13_202312270030.png')
plt.clf()