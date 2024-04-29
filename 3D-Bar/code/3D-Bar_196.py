

import matplotlib.pyplot as plt
import numpy as np

#transform data
y_values = ['Electricity Generation (TWh)', 'Gas Consumption (Billion cubic metres)', 'Oil Consumption (Million Barrels/day)']
data = np.array([[270,350,92],[275,340,90],[280,325,88],[285,310,86],[289,295,84]])
x_values = ['2015','2016','2017','2018','2019']

#plot 3D bar chart
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection='3d')

for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i]*len(x_values)
    ax.bar3d(xs, ys, [0]*len(x_values), 0.5, 0.5, data[:,i], color=plt.cm.Set2(i))

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticklabels(y_values)
ax.set_xlabel('Year')
# Rotate the X-axis labels for better readability
ax.view_init(elev=30, azim=30)
ax.set_title('Energy and Utilities - An Overview from 2015 to 2019')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/9_202312251000.png')
plt.show()
plt.clf()