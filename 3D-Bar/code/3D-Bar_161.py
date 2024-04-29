
import numpy as np
import matplotlib.pyplot as plt

y_values = ["Coal Production (Million Tonnes)",
            "Oil Production (Million Barrels per day)",
            "Electricity Generation (Terawatt Hours)"]

data = np.array([[1.2, 5.3, 8.5],
                 [1.4, 8.2, 7.6],
                 [1.6, 6.3, 9.2],
                 [1.8, 10.4, 10.3],
                 [2.0, 3.2, 11.4]])

x_values = ["2019", "2020", "2021", "2022", "2023"]

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

for i in range(len(y_values)):
    xs = np.arange(len(x_values))
    ys = [i]*len(x_values)

    bottom = np.zeros(len(x_values))
    width = depth = 0.8

    ax.bar3d(xs, ys, bottom, width, depth, data[:, i],
             shade=True, color=np.random.rand(3))

ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values)
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_title("Energy and Utilities Production Trends - 2019 to 2023")

fig.tight_layout()
fig.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/31_202312270030.png")
plt.show()
plt.clf()