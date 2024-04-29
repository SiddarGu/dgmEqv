import matplotlib.pyplot as plt
import numpy as np

x_values = ['2018', '2019', '2020', '2021', '2022']
y_values = ['Soft Drink', 'Snack Food', 'Dairy Product', 'Alcoholic Beverage']
data = np.array([[300,200,500,700], [280,250,550,800], [330,300,570,870], [350,320,600,900], [370,350,630,950]], dtype=np.float32)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

colors = ['r', 'g', 'b', 'y']
yticks = np.arange(len(y_values))

for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 
              0.4, 0.4, data[:, i], color=colors[i], alpha=0.7)

ax.set_title('Sales Trend in Food and Beverage Industry - 2018 to 2022')

ax.set_xlabel('Year')
ax.set_ylabel('Product')
ax.set_zlabel('Sales (in Millions)')

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(yticks)
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticklabels(y_values, ha='left')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/111_202312302126.png')
plt.clf()
