import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Transforming the data

data = """City,Apartment Sales (Units),House Sales (Units),Land Sales (Units),Commercial Property Sales (Units)
New York, 650, 520, 100, 200
Chicago, 500, 480, 85, 175
Los Angeles, 600, 550, 70, 250
San Francisco, 700, 520, 130, 210
Houston, 520, 400, 98, 190"""
lines = data.split("\n")
header = lines[0].split(",")
rows = [line.split(",") for line in lines[1:]]
x_values = [row[0] for row in rows]
y_values = header[1:]
data = np.array([[np.float32(value) for value in row[1:]] for row in rows])

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

colors = ['r', 'g', 'b', 'y']
for c, k in zip(colors, range(4)):
    # Construct arrays for the bars.
    xpos = np.arange(len(x_values))
    ypos = np.ones(len(x_values))*k
    zpos = np.zeros(len(x_values))
    dx = np.ones(len(x_values))*0.8
    dy = np.ones(len(x_values))*0.4  
    dz = data[:, k]
    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=c, alpha=0.5)

ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation = 45, wrap=True)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, ha='left')

ax.set_title('Real Estate Sales Analysis by Property Type per City')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/180_202312302235.png')
plt.clf()
