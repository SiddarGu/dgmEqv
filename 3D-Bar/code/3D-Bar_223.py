import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Transform the data
original_data = """Country,Milk Production (Billion Litres),Egg Production (Billion Dozens),Meat Production (Million Tonnes),Fruit Production (Million Tonnes)
USA,99,110,135,140
Canada,20,28,33,36
Germany,30,40,52,56
Australia,10,15,23,28
China,35,60,90,100"""
lines = original_data.split("\n")
header_line = lines[0]
data_lines = lines[1:]

x_values = [line.split(",")[0] for line in data_lines]
y_values = header_line.split(",")[1:]
data = np.array([list(map(np.float32, line.split(",")[1:])) for line in data_lines])

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection="3d")

colors=['b', 'r', 'g', 'y']

for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros_like(data[:, i]), 0.4, 0.4, data[:, i], shade=True, color=colors[i%len(colors)], alpha=0.7)

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45, ha='right')
ax.set_yticklabels(y_values)

plt.title('Comparison of Agricultural and Food Production by Country')
plt.grid(True)
ax.view_init(25, -50) # adjust the viewing angles
fig.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/248_202312310050.png')
plt.close(fig)
