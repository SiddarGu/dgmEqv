
import numpy as np
import matplotlib.pyplot as plt

y_values = ['Alcoholic Beverages (Litres)', 'Non-Alcoholic Beverages (Litres)', 'Food (Kilograms)']
data = np.array([[400, 600, 1000], [200, 500, 800], [300, 550, 750], [450, 620, 900]])
x_values = ['Fast Food', 'Fine Dining', 'Cafe', 'Catering']

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(1, 1, 1, projection='3d')

for i in range(len(y_values)):
    ax.bar3d(x=np.arange(len(x_values)), 
             y=[i]*len(x_values), 
             z=0, 
             dx=0.5, 
             dy=0.2, 
             dz=data[:, i], 
             color='#00a8f3')

ax.set_title('Food and Beverage Consumption in Different Establishments')
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=30)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, ha='left')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/19_202312270030.png')
plt.clf()