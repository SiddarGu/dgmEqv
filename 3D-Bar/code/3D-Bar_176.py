import matplotlib.pyplot as plt
import numpy as np


# parsing given data
data = '''Year,Beverage Sales (Million Liters),Confectionery Sales (Million $),Snack Sales (Million $),Dairy Products Sales (Million $)
2019,180,200,230,280
2020,170,210,235,290
2021,190,235,255,310
2022,185,240,270,330
2023,205,280,295,350'''

data = [line.split(',') for line in data.split('\n')]

x_values = [line[0] for line in data[1:]]
y_values = data[0][1:]
data = np.array([list(map(np.float32, line[1:])) for line in data[1:]])

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

colors = ['r', 'g', 'b', 'y']
for i, yval in enumerate(y_values):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 
             0.4, 0.5, data[:, i], color=colors[i], alpha=0.6)

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45, ha="right")
ax.set_yticklabels(y_values, ha='left')
ax.view_init(30, -50)
plt.title("Food and Beverage Industry Sales Trends - 2019 to 2023")
plt.grid(True)

plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/102_202312302126.png")
plt.clf()
