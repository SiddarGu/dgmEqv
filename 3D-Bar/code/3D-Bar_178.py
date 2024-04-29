import matplotlib.pyplot as plt
import numpy as np

# parse and split data
data_str = "Policy Title,Proposed Budget ($M),Actual Budget ($M),Budget Utilization ($M)\n Health Care,400,450,500\n Education,600,650,750\n Defense,700,800,900\n Social Services,350,400,500\n Infrastructure,500,600,700"
data_lines = data_str.split('\n')
headers = data_lines[0].split(',')
rows = [line.split(',') for line in data_lines[1:]]

# transform the data
y_values = headers[1:]
x_values = [row[0].strip() for row in rows]
data = np.array([[np.float32(val) for val in row[1:]] for row in rows])

fig = plt.figure(figsize=(10, 7))
ax = plt.axes(projection="3d")

width=0.3
depth=0.3
colors=['r', 'g', 'b']

for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), width, depth, data[:, i], color=colors[i], shade=True, alpha=0.7)

ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values,ha='left')
ax.set_zlabel('Budget ($M)')
ax.view_init(elev=20, azim=-35)

plt.title('Government Spending on Public Policies')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/193_202312302235.png')
plt.clf()
