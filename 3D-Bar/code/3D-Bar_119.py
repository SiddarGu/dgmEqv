import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Data transformation
y_values = ["Alcohol Sales (Million $)", "Non-Alcoholic Sales (Million $)", "Food Sales (Million $)"]
x_values = ["Coca-Cola", "PepsiCo", "Starbucks", "McDonald's", "KFC", "Burger King", "Domino's","Subway", "Dunkin' Brands", "Pizza Hut"]
data = np.array([[200, 1200, 800],
                 [220, 1100, 900],
                 [300, 700, 1300],
                 [180, 820, 1500],
                 [170, 770, 1400],
                 [150, 700, 1350],
                 [130, 600, 1300],
                 [120, 680, 1400],
                 [110, 650, 1500],
                 [105, 630, 1400]], np.float32)
                  
colors = ['r', 'g', 'b', 'y']

# Figure creation and plotting 
fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111, projection='3d')

# Creating 3D bars
_x = np.arange(len(x_values))
_y = np.arange(len(y_values))
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()

for i in range(len(y_values)):
    ax.bar3d(x[i * len(x_values):(i+1) * len(x_values)], y[i * len(x_values):(i+1) * len(x_values)], np.zeros(len(x_values)),
             0.4, 0.4, data[:,i], color=colors[i], alpha=0.7)

# Label and title setting
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation='vertical')
ax.set_yticklabels(y_values, ha='left')
plt.title('Food and Beverage Sales Analysis for Leading Companies')

# Viewing angle adjustment
ax.view_init(elev=20., azim=-35)

# Save figure and clear
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/221_202312302235.png')
plt.clf()
