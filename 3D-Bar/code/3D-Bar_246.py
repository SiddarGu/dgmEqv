import numpy as np
import matplotlib.pyplot as plt

# Parse data
data_str = "Field,Book Publications,Grants Awarded ($000),Total Researchers/n Archaeology,200,500,80/n Anthropology,150,300,60/n Psychology,300,750,120/n Literature,400,850,160/n Philosophy,350,700,140"
data_str = data_str.replace("/n ", "\n")
data_list = [row.split(',') for row in data_str.split('\n')]

y_values = data_list[0][1:]
x_values = [row[0] for row in data_list[1:]]
data = np.array([list(map(float, row[1:])) for row in data_list[1:]], dtype=np.float32)

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

bar_width = 0.4
colors = ['r', 'g', 'b']

# Iterating over y_values to plot each column of data
for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), bar_width, bar_width, data[:, i], color=colors[i], alpha=0.5)

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=20)
ax.set_yticklabels(y_values, ha='left')

plt.title('Analysis of Resources in Social Sciences and Humanities Fields')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/153_202312302235.png')
plt.clf()
