
import numpy as np
import matplotlib.pyplot as plt

# Transform data into three variables
y_values = ["Gas Production (Million Cubic Feet)", "Electricity Consumption (Billion kWh)", "Coal Production (Million Tonnes)"]
data = np.array([[250, 300, 600], [245, 290, 580], [248, 280, 590], [246, 285, 620], [252, 295, 650]])
x_values = ["2019", "2020", "2021", "2022", "2023"]

# Plot 3D bar chart
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i]*len(x_values)
    ax.bar3d(xs, ys, np.zeros(len(x_values)), 1, 1, data[:,i], shade = True)

ax.set_title("Energy and Utilities Trends - 2019 to 2023")
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticklabels(y_values, ha='left')

plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/23_202312270030.png")
plt.clf()