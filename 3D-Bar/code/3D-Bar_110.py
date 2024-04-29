import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

data="""Year,Processed Food Sales (Million $),Alcohol Beverage Sales (Million $),Non-alcoholic Beverage Sales (Million $),Total Revenue (Million $)
2017,300,100,150,550
2018,320,120,170,610
2019,350,140,200,690
2020,380,170,250,800
2021,420,190,280,890"""
data = [i.split(',') for i in data.split("\n")]

y_values = data[0][1:]
x_values = [i[0] for i in data[1:]]
data = np.array([i[1:] for i in data[1:]], dtype=np.float32)

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

colors = ['r', 'g', 'b', 'y']
yticks = [i for i in range(len(y_values))]

for c, k in zip(colors, range(len(y_values))):
    xs = np.arange(len(x_values))
    ys = data[:, k]
    ax.bar(xs, ys, zs=k, zdir='y', color=c, alpha=0.8)

ax.set_xlabel('Year')
ax.set_ylabel('Sales')
ax.set_zlabel('Revenue (Million $)')

ax.set_xticks(xs)
ax.set_yticks(yticks)

ax.set_xticklabels(x_values, rotation=45)
ax.set_yticklabels(y_values, ha='left')

plt.title('Food and Beverage Sales Revenue from 2017 to 2021')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/64_202312302126.png')
plt.clf()
