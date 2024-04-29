import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# defining data details:
y_values = ["Movie Box Office Revenue (Million $)","Sporting Event Tickets Sold (Million)","Music Concert Tickets Sold (Million)","Video Game Sales (Million $)"]
x_values = ["2018","2019","2020","2021","2022"]
data = np.float32([
    [2000, 40, 30, 1000],
    [2500, 45, 35, 1200],
    [1500, 10, 15, 2000],
    [2000, 25, 20, 1800],
    [2200, 30, 25, 1900]
])

fig = plt.figure(figsize=(10,7))  
ax = fig.add_subplot(111, projection='3d')  

colors = ['r', 'g', 'b', 'y']
yticks = np.arange(0, len(y_values))
for c, k in zip(colors, yticks):
    ax.bar3d(np.arange(len(x_values)), [k]*len(x_values), np.zeros(len(x_values)),
             0.5, 0.5, data[:, k], color=c, alpha=0.5)

ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=90, va='center')

ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, ha='left')

ax.set_title('Sports and Entertainment Industry Trends - 2018 to 2022')
ax.view_init(elev=15, azim=220) # adjust viewing angles 

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/150_202312302235.png', format='png', dpi=300)
plt.clf()
