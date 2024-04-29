
import numpy as np
import matplotlib.pyplot as plt

y_values = ['Smartphone Usage (Million)', 'Internet Usage (Million)', 'Tablet Usage (Million)', 'Social Media Usage (Million)']
x_values = ['2019', '2020', '2021', '2022', '2023']
data = np.array([[1000, 750, 450, 200], [1100, 850, 500, 250], [1300, 900, 550, 300], [1400, 950, 600, 340], [1500, 1000, 650, 380]])

fig = plt.figure(figsize=(15, 9))
ax = fig.add_subplot(111, projection='3d')

for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    ax.bar3d(xs, ys, [0] * len(x_values), 0.7, 0.7, data[:, i], alpha=0.7, color=['#0099ff', '#00cc00', '#ff9900', '#cc00cc', '#9900ff'])

ax.set_xlabel('Year')
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=-20)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values)
ax.view_init(150, -15)

plt.title('Digital Technology Use - An Overview from 2019 to 2023')
plt.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/42_202312270030.png')
plt.clf()