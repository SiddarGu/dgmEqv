import numpy as np
import matplotlib.pyplot as plt

data = """Department,Number of Employees,Training Hours,Employee Satisfaction Score
HR,50,100,90
Marketing,70,150,85
Sales,100,110,95
Production,200,130,80
IT,50,120,85"""

lines = data.split("\n")
x_values = [line.split(",")[0] for line in lines[1:]]
y_values = lines[0].split(",")[1:]
values = np.array([list(map(int,line.split(",")[1:])) for line in lines[1:]], dtype=np.float32)

fig = plt.figure(figsize= (10,8))
ax = fig.add_subplot(111, projection='3d')

for i in range(values.shape[1]):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)),
    0.4, 0.5, values[:, i], color='b', alpha=0.5)

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation = 45, ha="right")
ax.set_yticklabels(y_values, ha='left')
ax.set_title("Human Resources Management Trends by Department")

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/174_202312302235.png', dpi=300)
plt.clf()
