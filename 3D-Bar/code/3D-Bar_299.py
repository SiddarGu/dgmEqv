import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

data = np.array([[65.2, 108, 16.1, 275, 300],
                 [70, 112.4, 17.5, 284, 312],
                 [72, 115, 19, 295, 330],
                 [73.8, 116.8, 20, 305, 350],
                 [74, 117.4, 21, 311, 360]], dtype=np.float32)
y_values = ['Beef Consumption (lbs)', 'Poultry Consumption (lbs)', 'Fish Consumption (lbs)', 'Fruit Consumption (lbs)', 'Vegetable Consumption (lbs)']
x_values = np.array([2019, 2020, 2021, 2022, 2023], dtype=np.int32)

fig = plt.figure(figsize=(12, 8))
ax1 = fig.add_subplot(111, projection='3d')

colors = ['r', 'g', 'b', 'y', 'c']

for i in range(len(y_values)):
    ax1.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)),
              0.4, 0.6, data[:, i], color=colors[i], alpha=0.8)

ax1.set_yticks(np.arange(len(y_values)))
ax1.set_yticklabels(y_values, ha='left')
ax1.set_xticks(np.arange(len(x_values)))
ax1.set_xticklabels(x_values, rotation=45, ha='right')

ax1.set_title('Trends in Food Consumption in the Beverage Industry - 2019 to 2023')
plt.tight_layout()

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/186_202312302235.png')
plt.cla()
plt.clf()
plt.close()
