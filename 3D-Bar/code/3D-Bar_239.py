import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data = '''Year,Electronics Production (Million Units),Automobile Production (Million Units),Textile Production (Million Units),Food Product Manufacturing (Million Units)
2018,250,330,450,500
2019,275,360,480,540
2020,310,390,500,590
2021,345,420,550,650
2022,370,460,600,700 '''

lines = data.split('\n')
x_values = [line.split(',')[0] for line in lines[1:-1]]  
y_values = lines[0].split(',')[1:]  
data = np.array([[np.float32(i) for i in line.split(',')[1:]] for line in lines[1:-1]])

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

colors = ['r', 'g', 'b', 'y']  
width_depth = 0.3  
x_ticks = np.arange(len(x_values))

for c, k, y_value in zip(colors, range(4), y_values):
    ax.bar3d(x_ticks, np.array([k]*len(x_values)), np.zeros(len(x_values)), 
             width_depth, width_depth, data[:, k], color=c, alpha=0.5)
             
plt.xticks(x_ticks, x_values, rotation=90)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, ha='left')
ax.set_xlabel('Year')
ax.set_title('Manufacturing and Production Trends - 2018 to 2022')

ax.view_init(elev=25, azim=-60)  
ax.grid(True)

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/237_202312310050.png', dpi=300)
plt.clf()
