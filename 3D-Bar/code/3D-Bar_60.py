import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Define data
x_values = ['2019', '2020', '2021', '2022', '2023']
y_values = ['Beef Consumption (Kg)', 'Pork Consumption (Kg)', 'Poultry Consumption (Kg)', 'Fish Consumption (Kg)']
data = np.array([
    [15, 20, 30, 18], 
    [17, 22, 32, 20], 
    [19, 24, 34, 22], 
    [20, 26, 36, 24], 
    [22, 28, 38, 26]
])

_x = np.arange(len(x_values))
_y = np.arange(len(y_values))
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()

# Initialize to 0 by default
z = np.zeros_like(x)

colors = ['b', 'g', 'r', 'c']

# Iterate over the y_values
for i in range(len(y_values)):
    ax.bar3d(x[i*len(x_values):(i+1)*len(x_values)], y[i*len(x_values):(i+1)*len(x_values)], z[i*len(x_values):(i+1)*len(x_values)],
             0.5, 0.5, data[:, i], color=colors[i], alpha=0.7)

ax.set_xticks(_x)
ax.set_yticks(_y + 0.25)
ax.set_xticklabels(x_values, rotation = 20)
ax.set_yticklabels(y_values, ha='left')

ax.set_title('Annual Meat Consumption Trends in Food and Beverage Industry (2019-2023)')

# Save the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/156_202312302235.png', format='png', dpi=300)
plt.clf()
