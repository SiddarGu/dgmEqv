import matplotlib.pyplot as plt
import numpy as np

# setting data
x_values = np.array(['2017','2018','2019','2020','2021'])
y_values = np.array(['Processed Food Sales ($B)', 'Beverage Sales ($B)', 'Organic Food Sales ($B)', 'Health Drink Sales ($B)'])
data = np.array([[200, 150, 50, 70],
                 [220, 160, 60, 80],
                 [240, 180, 70, 90],
                 [260, 200, 80, 100],
                 [280, 220, 90, 120]], np.float32)

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

colors = ['r', 'g', 'b', 'y']
yticks = np.arange(len(y_values))

for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 0.4, 0.8, data[:, i], color=colors[i], alpha=0.7)

ax.set_title('Annual Sales Trends in the Food and Beverage Industry (2017-2021)')
ax.set_xlabel('Year')
ax.set_ylabel('Sales Category')
ax.set_zlabel('Sales ($B)')
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(yticks)
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticklabels(y_values, ha='left')
ax.view_init(elev=25, azim=165)

plt.subplots_adjust(bottom=0.2)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/244_202312310050.png')
plt.clf()
