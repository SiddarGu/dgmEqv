import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

data_str = "Period,Publications in Philosophy (Quantity),Publications in Sociology (Quantity),Publications in Psychology (Quantity),Number of Research Grants/n 2020,60,80,72,170/n 2021,60,79,75,185/n 2022,65,82,79,190/n 2023,70,85,83,195/n 2024,75,87,87,200"
data_list = [item.split(",") for item in data_str.split("/n ")]
x_values = [item[0] for item in data_list[1:]]
y_values = data_list[0][1:]
data = np.array([list(map(int, item[1:])) for item in data_list[1:]], dtype=np.float32)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)),
             0.2, 0.5, data[:, i],
             color=plt.cm.viridis(i/len(y_values)), alpha=0.8)

ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=45, ha='right')
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, ha='left')
ax.set_zlabel('Values')
ax.set_title('Analysis of Scholarly Publications and Research Grants in Social Sciences and Humanities (2020 - 2024)')

plt.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/131_202312302235.png', dpi=300)
plt.clf()
