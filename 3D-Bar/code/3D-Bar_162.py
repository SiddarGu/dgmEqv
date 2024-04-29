import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

string_data = """Year,Donations Received ($000),Number of Volunteers,Number of Beneficiaries
2018,130,150,200
2019,135,155,225
2020,200,220,250
2021,190,230,270
2022,215,250,300"""

data_arr = np.array([i.split(',') for i in string_data.split('\n')])

x_values = data_arr[1:, 0]
y_values = data_arr[0, 1:]
data = np.float32(data_arr[1:, 1:])

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

colors = ['b', 'r', 'g']

for c, z, i in zip(colors, np.zeros(len(y_values)), range(len(y_values))):
    xs = np.arange(len(x_values))
    ys = data[:, i]
    ax.bar(xs, ys, zs=i, zdir='y', color=c, alpha=0.8)

ax.set_xlabel('Year')
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=-45)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, ha='left')

ax.view_init(45, -30)
plt.title('Analysis of Charity and Nonprofit Organizations Progress from 2018 to 2022')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/235_202312310050.png')
plt.clf()
