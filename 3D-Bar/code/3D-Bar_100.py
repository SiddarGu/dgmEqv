import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Prepare data
raw_data = """Month,Vegetable Harvest (Tons),Meat Production (Tons),Dairy Production (Tons),Grain Yield (Tons)
January,150,300,400,500
February,120,250,440,500
March,200,315,400,520
April,220,350,510,600
May,300,400,560,700"""
lines = raw_data.split("\n")
y_values = lines[0].split(",")[1:]
x_values = [line.split(",")[0] for line in lines[1:]]
data = np.float32([line.split(",")[1:] for line in lines[1:]])

# Create a figure for the plot
fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111, projection='3d')

# Iterate over y_values
for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 
             0.5, 0.5, np.float32(data[:, i]), color=np.random.rand(3,), alpha=0.6)

# Set the x and y axis labels
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=45, ha='right')
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, ha='left')

# Set the title and show the grid
ax.set_title('Monthly Agriculture and Food Production Data')
ax.grid(True)

# Adjust the viewing angle for better readability
ax.view_init(elev=30., azim=-45.)

# Automatically adjust layout
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/210_202312302235.png', dpi=300)

# Clear the current figure
plt.clf()
