
import numpy as np 
import matplotlib.pyplot as plt 

# Data preparation
data = np.array([[2015,17,37.4,68,0.9],
                 [2016,20,35.3,72,1.1],
                 [2017,22,37.2,77,1.3],
                 [2018,25,36.7,80,1.5],
                 [2019,27,35.4,82,1.7]])
y_values = data[0][1:]
x_values = data[1:,0]
data = data[1:,1:]

# Create figure
fig = plt.figure(figsize=(10,8)) 
ax = fig.add_subplot(111, projection='3d')

# Plotting
for i in range(len(y_values)):
    xs = np.arange(len(x_values)) 
    ys = [i] * len(x_values)
    ax.bar3d(xs, ys, np.zeros(len(x_values)), 0.8, 0.8, data[:,i], alpha=0.5, color=plt.cm.jet(i/len(y_values)))

# Set labels
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values)

# Rotate x-axis labels
for tick in ax.xaxis.get_major_ticks():
    tick.label1.set_rotation(70)

# Set title
ax.set_title("Environmental Sustainability Trends - 2015 to 2019")

# Set grids
ax.grid(False)

# Tight layout
plt.tight_layout()

# Save figure
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/31_202312251044.png")

# Clear the current image state
plt.clf()