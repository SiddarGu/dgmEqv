import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parsing input data into 3D array
input_data = """
2019,3000,2500,3500,2000
2020,3300,2800,4000,2200
2021,3600,3100,4500,2400
2022,3900,3400,5000,2600
2023,4200,3700,5500,2800 
"""

rows = input_data.strip().split("\n")
x_values = [row.split(",")[0] for row in rows]
y_values = ["Internet Users (Millions)", "Smartphone Users (Millions)", "E-commerce Sales (Billions $)", "Online Advertisement Spending(Billions $)"]
data = np.array([list(map(np.float32, row.split(",")[1:])) for row in rows])

# Create a 3D Bar Chart
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

colors = ['b', 'r', 'g', 'y']
for c, z, i in zip(colors, [0, 1, 2, 3], range(4)):
    xs = np.arange(len(x_values))
    ys = data[:, i]
    ax.bar3d(xs, [i]*len(xs), np.zeros_like(xs), 0.4, 0.8, ys, color=c, alpha=0.7)

ax.set_xlabel('Year')
ax.set_ylabel('Category')
ax.set_title('Technology and the Internet Usage - 2019 to 2023')
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values)
ax.set_yticklabels(y_values, ha='left')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/166_202312302235.png')
plt.clf()
