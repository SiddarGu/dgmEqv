import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# data
data = """Quarter,Revenue (Million $),Operating Expenses (Million $),Net Income (Million $)
Q1 2020,500,400,600
Q2 2020,550,450,650
Q3 2020,600,500,700
Q4 2020,650,550,750
Q1 2021,700,600,800"""
data = data.split("\n")
x_values = [row.split(",")[0] for row in data[1:]]  # labels of x-axis
y_values = data[0].split(",")[1:]  # labels of y-axis
data = np.array([row.split(",")[1:] for row in data[1:]], dtype=np.float32)

# create figure and bar plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

colors = ['r', 'g', 'b']
for i, ypos in enumerate(y_values):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)),
              0.4, 0.6, data[:, i], color=colors[i % len(colors)], alpha=0.7)

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values)
ax.set_yticklabels(y_values, ha='left')
ax.set_title("Quarterly Financial Overview 2020 - Q1 2021")

# rotate the tick labels for clarity
for item in ax.get_xticklabels():
    item.set_rotation(45)

plt.tight_layout()
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/hancheng/3D-Bar/png_train/3D-Bar_230.png")
plt.clf()
