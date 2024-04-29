
import numpy as np
import matplotlib.pyplot as plt

y_values = ["Government Expenditure ($Billion)", "Tax Revenue ($Billion)", "Public Debt (% of GDP)"]
data = np.array([[2.3, 3.5, 8], [2.4, 3.6, 8.2], [2.5, 3.7, 8.4], [2.6, 3.8, 8.6], [2.7, 3.9, 8.8]])
x_values = ["2019", "2020", "2021", "2022", "2023"]

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection="3d")
for i in range(data.shape[1]):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 
             0.8, 0.5, data[:, i], alpha=0.5, color=[plt.cm.jet(i/data.shape[1])])

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45, wrap = True)
ax.set_yticklabels(y_values, ha='left')
ax.set_title("Government Fiscal Policy Analysis - 2019 to 2023")
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/6.png')
plt.clf()