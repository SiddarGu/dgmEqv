
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

y_values = ['Gross Domestic Product (GDP) ($ Trillion)', 'Unemployment Rate (%)', 'Consumer Price Index (CPI)']
data = np.array([[1.5, 3.7, 26.4], 
                 [1.5, 5.8, 20.9], 
                 [2.7, 4.6, 24.7],
                 [4.1, 3.9, 26.8],
                 [5.3, 3.5, 20.1]])
x_values = ['2019', '2020', '2021', '2022', '2023']

for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i]*len(x_values)
    ax.bar3d(xs, ys, np.zeros(len(x_values)), 0.5, 0.5, data[:, i], alpha=0.8, color=(1, 0, 0, 1))

ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=90)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, ha='left')
fig.set_figwidth(15)
fig.set_figheight(10)
plt.tight_layout()
ax.set_title('Economic Performance of the US - 2019 to 2023')
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/20_202312251036.png')
plt.clf()