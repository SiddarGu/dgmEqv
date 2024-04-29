
import matplotlib.pyplot as plt
import numpy as np

y_values = ["Online Shopping Volume (Units)", "Store Shopping Volume (Units)", "Total Shopping Volume (Units)"]
data = np.array([[20,50,70], [25,60,85], [30,70,100], [35,80,115], [40,90,130]])
x_values = ["2020", "2021", "2022", "2023", "2024"]

fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111,projection='3d')

for i in range(len(y_values)):
    xpos = np.arange(len(x_values))
    ypos = [i]*len(x_values)
    dx = np.ones(len(x_values))
    dy = np.ones(len(x_values))
    dz = data[:,i]

    ax.bar3d(xpos, ypos, np.zeros(len(x_values)), dx, dy, dz, color='#86D2F4', alpha=1)

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values)
ax.set_yticklabels(y_values, ha='left')
ax.set_title("Retail and E-commerce Shopping Trends - 2020 to 2024")

plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/7_202312251044.png")
plt.clf()