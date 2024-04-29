import matplotlib.pyplot as plt
import numpy as np

# Data Preparation
data = '''Year,Population Growth (%),Education Budget ($ Billion),Global Conflict Index,nr of Published Papers
2017,1.2,15,2.3,8.5
2018,1.3,16,2.1,8.8
2019,1.4,17.2,2.0,9
2020,1.5,18,2.4,9.2
2021,1.6,19,2.2,9.5'''
lines = data.split("\n")
x_values = [line.split(',')[0] for line in lines[1:]] 
y_values = lines[0].split(',')[1:]
data = np.array([list(map(np.float32, line.split(',')[1:])) for line in lines[1:]])

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection='3d')

colors = ['r','g','b','m']
yticks = np.arange(len(y_values))

for c, k in zip(colors,yticks):
    xs = np.arange(len(x_values))
    ys = data[:, k]
    ax.bar3d(xs, np.repeat(k, len(xs)), np.zeros(len(xs)), 0.4, 0.4, ys, color=c, alpha=0.8)

ax.set_xlabel('Year')
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticks(yticks)
ax.set_yticklabels(y_values, ha='left')
ax.set_zlabel('Values')
ax.set_title('Interdisciplinary Trends in Social Sciences and Humanities (2017-2021)')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/194_202312302235.png')
plt.clf()
