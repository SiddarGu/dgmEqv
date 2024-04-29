import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# parse the data
lines = """Year,Number of Internet Users (Million),Number of Smartphone Users (Million),Global E-commerce sales ($Billion)
2018,3500,2500,2300
2019,3600,2700,2500
2020,3700,2800,2800
2021,3800,2900,3100
2022,4000,3100,3300""".split('\n')

header = lines[0].split(',')
lines = lines[1:]

x_values = []
data = []
for line in lines:
    parts = line.split(',')
    x_values.append(parts[0])
    data.append([np.float32(part) for part in parts[1:]])

y_values = header[1:]

# create figure and add subplot
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

colors = ['r', 'g', 'b']

for c, k in enumerate(y_values):
    xs = np.arange(len(x_values))
    ys = np.array([data[i][c] for i in range(len(x_values))])
    ax.bar(xs, ys, zs=c, zdir='y', color=colors[c], alpha=0.8)

# set ticks and labels
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation='vertical')
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, ha='left')

# set title
plt.title("Global Internet and Technology Trends 2018-2022", y=1.1)

# adjust view
ax.view_init(30, -20)
plt.subplots_adjust(bottom=0.2)

# save the image and then clear the figure
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/72_202312302126.png", format='png')
plt.clf()
