import numpy as np
import matplotlib.pyplot as plt

# define data
data = """Year,Number of Internet Users (Millions),Tech Startups Founded,Revenue from Online Sales ($Billion)
2019,4840,3200,3000
2020,5000,2900,4000
2021,5210,4100,4500
2022,5400,1425,5000
2023,5600,4500,5500"""
data = [item.split(',') for item in data.split('\n')]

x_values = np.array(data[1:])[:, 0]
y_values = np.array(data[0])[1:]
data = np.float32(np.array(data[1:])[:, 1:])

# Plotting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Create bars for each y_value (data column)
colors = ['b', 'r', 'g', 'y', 'c', 'm']
for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)),
              0.4, 0.6, data[:, i], color=colors[i % len(colors)], alpha=0.7)

# Set labels and ticks
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45, horizontalalignment='right')
ax.set_yticklabels(y_values, ha='left')

# Set chart title
ax.set_title('Internet Usage, Tech Startup Trends and Online Sales Revenue - 2019 to 2023')

ax.view_init(elev=10, azim=-65)   # adjust this for better viewing angle

fig.tight_layout()  # this auto-resizes the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/140_202312302235.png', format='png')

plt.show()
plt.clf()
