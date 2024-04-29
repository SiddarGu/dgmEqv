import numpy as np 
import matplotlib.pyplot as plt 

str_data = 'Year,Global Internet Users (Billion),Mobile Internet Users (Billion),Broadband Subscriptions (Billion),Number of Websites (Billion)/n 2015,3.24,2.03,0.81,0.9/n 2016,3.4,2.5,0.96,1.1/n 2017,3.57,2.73,1.07,1.3/n 2018,3.74,2.98,1.2,1.5/n 2019,3.93,3.26,1.34,1.7'

rows = str_data.split('/n')
header = rows[0].split(',')
rows = [row.split(',') for row in rows[1:]]

x_values = [row[0] for row in rows]
y_values = header[1:]
data = np.array([list(map(float, row[1:])) for row in rows])

fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111, projection='3d')

width = 0.3
depth = 0.3
colors = ['r', 'g', 'b', 'y']

for c, z, yi in zip(colors, range(4), y_values):
  xs = np.arange(len(x_values))
  ys = data[:, z]
  ax.bar3d(xs, [z]*len(xs), np.zeros(len(xs)), width, depth, ys, color=c, alpha=0.7)

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticklabels(y_values, ha='left')
ax.set_zlabel('Values in Billion')
ax.set_title('Global Internet Usage and Website Trends - 2015 to 2019')

plt.tight_layout()

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/267_202312310050.png')

plt.clf()
