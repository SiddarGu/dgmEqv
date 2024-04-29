
import numpy as np
import matplotlib.pyplot as plt

y_values = ["Automotive Production (Units)", "Electronics Production (Units)", "Textiles Production (Units)", "Pharmaceuticals Production (Units)"]
x_values = ["2019", "2020", "2021", "2022", "2023"]
data = np.array([[25000, 30000, 45000, 50000],
                  [30000, 35000, 40000, 51000],
                  [35000, 40000, 42000, 52000],
                  [40000, 45000, 46000, 53000],
                  [45000, 50000, 50000, 54000]])

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 0.5, 0.5, data[:,i], cmap='Blues')

ax.set_title('Global Manufacturing and Production Trends - 2019 to 2023')
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=30)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, ha='left')

ax.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/15_202312251036.png')
plt.clf()