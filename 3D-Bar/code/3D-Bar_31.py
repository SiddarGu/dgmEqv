
import numpy as np
import matplotlib.pyplot as plt

y_values = ['Average Temperature (°C)', 'Carbon Emissions (Gigatonnes of CO2)', 'Renewable Energy Production (Hundred Kilowatt-hours)']
data = np.array([[15,38,30],[17,36,32],[16,37,34],[18,35,36],[17,38,38]])
x_values = ['2019','2020','2021','2022','2023']

fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111, projection='3d')

for i in range(len(y_values)):
    xpos = np.arange(len(x_values))
    ypos = [i] * len(x_values)
    ax.bar3d(xpos, ypos, np.zeros(len(x_values)), 1, 1, data[:,i], alpha=0.5, color='red')

ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values,rotation=45)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, ha='left', rotation=-20)
plt.title('Climate Change and Renewable Energy Trends - 2019 to 2023')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/7_202312270030.png')
plt.cla()