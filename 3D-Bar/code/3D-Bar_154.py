import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#transform the data into three variables
y_values = ['Food Industry Revenue (Billion $)', 'Beverage Industry Revenue (Billion $)', 'Total Food and Beverage Revenue (Billion $)']
data = np.array([[300, 150, 450], [320, 170, 490], [360, 180, 540], [380, 200, 580], [400, 210, 610]], np.float32)
x_values = ['2018', '2019', '2020', '2021', '2022']

#Plot the data with the type of 3D bar chart
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

colors = ['r', 'g', 'b']
for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), np.ones(len(x_values))/5, np.ones(len(x_values))/5, data[:, i] , 
              color=colors[i], alpha=0.7)
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=45)

ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, ha='left')

#grid, viewing angles and title
ax.grid(True)
ax.view_init(30, -70)
plt.title('Revenue Trends in the Food and Beverage Industry - 2018 to 2022')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/141_202312302235.png')
plt.clf()
