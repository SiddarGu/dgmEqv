import matplotlib.pyplot as plt
import numpy as np

data = np.array([[150, 3.2, 170], [200, 3.8, 220], [250, 4.3, 280], [300, 4.7, 330], [350, 5.2, 380]], dtype=np.float32)
x_values = ['2019', '2020', '2021', '2022', '2023']
y_values = ['Donations Received ($M)', 'Number of Beneficiaries (Thousands)', 'Total Expenditure ($M)']

fig = plt.figure(figsize=(10, 8))
ax1 = fig.add_subplot(111, projection='3d')

colors = ['r', 'g', 'b']
xt = np.arange(data.shape[0])
for i, y_value in enumerate(y_values):
    ax1.bar3d(xt, np.array([i]*data.shape[0]), np.zeros(data.shape[0]), 0.3, 0.3, data[:,i], color=colors[i], alpha=0.7)

ax1.set_xticks(xt)
ax1.set_yticks(np.arange(len(y_values)))
ax1.set_xticklabels(x_values, wrap=True)
ax1.set_yticklabels(y_values, ha='left')

ax1.set_title('Annual Performance of Nonprofit Organizations - 2019 to 2023')
plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/231_202312310050.png")
plt.clf()
