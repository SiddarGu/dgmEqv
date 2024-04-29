
import matplotlib.pyplot as plt
import numpy as np

y_values = ['Coal Production (Million Tonnes)', 'Oil Production (Million Barrels)', 'Nuclear Energy Generation (GWh)', 'Renewable Energy Generation (GWh)']
data = np.array([[2600, 3000, 3000, 4000], 
                 [2580, 3200, 3200, 4300],
                 [2650, 3500, 3500, 4700],
                 [2630, 3700, 3700, 5000],
                 [2650, 4000, 4000, 5400]])
x_values = ['2019', '2020', '2021', '2022', '2023']

fig = plt.figure(figsize=(15, 8))
ax = fig.add_subplot(111, projection='3d')
X = np.arange(len(x_values))
for i in range(len(y_values)):
    ax.bar3d(X, [i]*len(x_values), np.zeros(len(x_values)), 1, 1, data[:, i], shade=True, color='r')

ax.set_xticks(X)
ax.set_yticks(range(len(y_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticklabels(y_values, ha='left')
ax.set_title('Energy Production and Generation Trends - 2019 to 2023')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/20_202312270030.png')
plt.clf()