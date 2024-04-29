import matplotlib.pyplot as plt
import numpy as np

# Given input data
data_str = "Year,Box Office Revenue (Billion $),Ticket Sales (Million),Sports Event Attendance (Million),Growth in Digital Media Consumption (Percent)/n 2019,42.3,1125,270,72/n 2020,15,510,78,92/n 2021,20,610,100,97/n 2022,28.7,900,210,102/n 2023,35,1100,250,105 "

# Parse input data into appropriate variables
data_rows = [row.split(',') for row in data_str.replace('/n ', '/n').split('/n')]
y_values = data_rows[0][1:]
x_values = [row[0] for row in data_rows[1:]]
data = np.array([list(map(np.float32, row[1:])) for row in data_rows[1:]])

# Create 3D figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Widths, depths, etc for the bars
width = depth = 0.5
colors = ['b', 'r', 'g', 'orange']
alpha = 0.5

# Iterate over the y_values (columns of data)
for i in range(data.shape[1]):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 
              width, depth, data[:, i], color=colors[i % len(colors)], alpha=alpha)

# Labeling
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation='vertical')
ax.set_yticklabels(y_values, ha='left')

# Graph adjustments
ax.set_title('Trends in Global Sports and Entertainment Industry - 2019 to 2023')
ax.view_init(elev=20, azim=-35)
ax.grid(True)

# Save figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/227_202312302235.png')

# Clear figure
plt.clf()
