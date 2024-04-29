import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# String of data
str_data = "Year,Online Sales ($ Billion),In-Store Sales ($ Billion),Total Sales ($ Billion)/n 2019,1000,600,1600/n 2020,1500,400,1900/n 2021,2000,500,2500/n 2022,2500,600,3100/n 2023,3000,700,3700"

# Splitting data based on line break
data_list = str_data.split("/n")

# Transforming data into y_values, x_values and data
y_values = data_list[0].split(",")[1:]
x_values = [item.split(",")[0] for item in data_list[1:]]
data = np.array([item.split(",")[1:] for item in data_list[1:]], dtype=np.float32)

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

# bar width and depth
width = 0.3
depth = 0.3

colors = ['b', 'r', 'g', 'y', 'c']

for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), width, depth, data[:, i], color=colors[i], alpha=0.8)
    
_ = ax.set_xticks(np.arange(len(x_values)))
_ = ax.set_yticks(np.arange(len(y_values)))
_ = ax.set_xticklabels(x_values, rotation=45)
_ = ax.set_yticklabels(y_values, ha='left')

ax.set_title( 'Retail And E-commerce Sales from 2019 to 2023')
ax.grid(True)

ax.view_init(azim=-45)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/207_202312302235.png')
plt.cla()  # Clear axis
plt.clf()  # Clear figure
