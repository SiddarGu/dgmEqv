from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

# Make this easier to replicate by setting seed
np.random.seed(0)

# Parse provided data
data = np.array([[70, 105, 85, 120], [80, 110, 90, 125], [75, 115, 100, 130], [90, 120, 105, 135]], dtype=np.float32)
x_values = ['2018', '2019', '2020', '2021']
y_values = ['Truckload (Million Tons)','Intermodal (Million Tons)','Less-than-Truckload (Million Tons)','Air Cargo (Million Tons)']

fig = plt.figure(figsize=(12, 10))

# Use 3D projection for subplot
ax = fig.add_subplot(111, projection='3d')

# Set the colors
colors = ['r', 'g', 'b', 'y']

# Iterate over y_values to plot each column of data
for i in range(data.shape[1]):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 
             0.5, 0.5, data[:, i], color=colors[i], alpha=0.6)

# Set ticks and labels
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45, ha='right')
ax.set_yticklabels(y_values, ha='left')

# Set the title
plt.title('Annual Volume of Goods Transported in Different Modes from 2018 to 2021')

# Make layout tighter
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/167_202312302235.png')

# Clear current figure
plt.clf()
