import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parse the given data string into a list of lists
data_string = "Year,Number of Internet Users (Billions),Global E-commerce Sales ($ Trillion),Smartphone Penetration (%)\n 2019,4.1,3.5,67.9\n 2020,4.6,4.2,70.4\n 2021,4.88,4.9,73.1\n 2022,5.3,5.6,75.7\n 2023,5.7,6.3,78.2"
data_lines = data_string.split("\n")
data_list = [line.split(",") for line in data_lines]

# Define the y values, x values and data 
y_values = data_list[0][1:]
x_values = [item[0] for item in data_list[1:]]
data = np.asarray([item[1:] for item in data_list[1:]], dtype=np.float32)

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111, projection='3d')
bar_width = 0.4
bar_depth = 0.2
colors = ['r', 'g', 'b']

for c, k in zip(colors, range(data.shape[1])):
    x = np.arange(data.shape[0])
    y = np.array([k]*len(x_values))
    z = data[:, k]
    ax.bar3d(x, y, np.zeros(len(z)), bar_width, bar_depth, z, color=c, alpha=0.6)

ax.set_title('Digital Trends: Internet Usage, E-commerce Sales, and Smartphone Penetration - 2019 to 2023')
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation = 45)
ax.set_yticklabels(y_values, ha='left')
ax.view_init(elev=20., azim=-35)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/230_202312302235.png')
plt.clf()
