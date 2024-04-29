import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# given data
raw_data = """Country,Number of Art Galleries,Number of Film Festivals,Number of UNESCO Heritage Sites
USA,800,500,24
France,1200,420,44
Japan,480,300,22
Germany,750,520,46
Italy,900,375,55"""

lines = raw_data.split("\n")
y_values = lines[0].split(",")[1:]  
x_values = [line.split(",")[0] for line in lines[1:]]  
data = np.array([list(map(int, line.split(",")[1:])) for line in lines[1:]], dtype=np.float32)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

colors = ['r', 'g', 'b']
for i, y in enumerate(y_values):
    ax.bar3d(np.arange(len(x_values)), np.array([i]*len(x_values)), np.zeros(len(x_values)), 
             0.4, 0.8, data[:, i], color=colors[i%len(colors)], alpha=0.75)

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45, horizontalalignment='right')
ax.set_yticklabels(y_values, ha='left')

ax.set_title('Comparison of Cultural Parameters across Different Countries')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/113_202312302126.png')
plt.clf()
