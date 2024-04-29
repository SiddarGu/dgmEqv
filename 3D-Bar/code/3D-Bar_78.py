import numpy as np
import matplotlib.pyplot as plt

# Preparing data
data_str = 'Month,Air Cargo (Million Tonnes),Truck Deliveries (Million Tonnes),Marine Freight (Million Tonnes),Rail Freight (Million Tonnes)\
            /n January,15,20,35,45\
            /n February,10,18,30,38\
            /n March,14,19,28.5,36.2\
            /n April,15.2,25.2,33.7,42.4\
            /n May,20,28.8,35.6,45.2'
data_list = data_str.split('/n ')
header = data_list[0].split(',')
data_raw = [d.split(',') for d in data_list[1:]]
x_values = [row[0] for row in data_raw]
y_values = header[1:]
data = np.float32([row[1:] for row in data_raw])

# Create 3D figure
fig = plt.figure(figsize=(10, 7))
ax = plt.axes(projection='3d')

# Bar settings
width = 0.3
depth = 0.3
colors = ['r', 'g', 'b', 'y']
alpha = 0.7

# Plot each column of data
for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i]*len(x_values)
    zs = np.zeros(len(x_values))
    dx = np.full(len(x_values), width) 
    dy = np.full(len(x_values), depth) 
    dz = data[:, i]
    color = colors[i]
    ax.bar3d(xs, ys, zs, dx, dy, dz, color=color, alpha=alpha)

# Adjusting labels
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticklabels(y_values, ha='left')

# Additional chart settings
plt.title('Transportation and Logistics Freight Volumes - January to May')
ax.grid(True)
ax.view_init(25, 60)

# Adjust layout and save the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/246_202312310050.png', format='png')

# Clear the figure
plt.clf()
