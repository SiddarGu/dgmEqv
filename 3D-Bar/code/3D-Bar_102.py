
import numpy as np
import matplotlib.pyplot as plt

y_values = ['Online Shopping Expenditure ($)', 'Retail Store Expenditure ($)', 'Total Spending ($)']
x_values = ['2019', '2020', '2021', '2022', '2023']
data = np.array([[400,600,1000],
                 [500,700,1200],
                 [550,750,1300],
                 [600,800,1400],
                 [650,850,1500]])

fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111, projection='3d')

for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i] * len(x_values)
    ax.bar3d(xs, ys, np.zeros(len(x_values)), 0.25, 0.25, data[:, i], shade=True, alpha=0.8)

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticklabels(y_values)
ax.set_title('Comparison of Retail and E-commerce Spending from 2019 to 2023')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/44_202312251044.png')
plt.clf()