import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Prepare data
data = '''Quarter,Net Profit ($M),Revenue ($B),Market Share (%)
         Q1-2020,5,1.4,20
         Q2-2020,6,1.6,22
         Q3-2020,7,1.8,24
         Q4-2020,8,2.0,26
         Q1-2021,9,2.2,28'''

lines = data.split("\n")
x_values = [line.split(',')[0].strip() for line in lines[1:]]
y_values = lines[0].split(',')[1:]
numbers = [list(map(np.float32, line.split(',')[1:])) for line in lines[1:]]
data = np.array(numbers)

# Create figure
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Iterate over y_values to plot each column of data
for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 0.4, 0.8, data[:, i], color=plt.cm.viridis(data[:, i]/np.max(data)), alpha=0.7)

# Set xticks and yticks
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))

# Rotate the X-axis labels for better readability
ax.set_xticklabels(x_values, rotation=50, horizontalalignment='right')
ax.set_yticklabels(y_values, horizontalalignment='left')

# Other settings for visualization
ax.view_init(elev=20, azim=-35)
ax.grid(True)
plt.title('Company Financial Performance - 2020 to 2021')
plt.tight_layout()

# Save figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/213_202312302235.png', format='png')

# Clear the current figure
plt.clf()
