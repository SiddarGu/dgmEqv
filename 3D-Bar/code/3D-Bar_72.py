import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data = "Organization,Number of Volunteers,Amount Donated ($000),Number of Beneficiaries /n Care International,300,450,800 /n Save the Children,500,700,1200 /n Amnesty International,350,650,1100 /n Medecins Sans Frontieres,450,750,1300 /n Habitat for Humanity,400,700,1200 "
data = data.split('/n')
x_values = [item.split(',')[0].strip() for item in data[1:]]
y_values = data[0].split(',')[1:]

data_values = [item.split(',')[1:] for item in data[1:]]
data_values = np.array(data_values, dtype=np.float32)

fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111, projection='3d')

colors = ['b', 'r', 'g', 'y', 'c']
width = 0.2
for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), width, width, data_values[:, i], color=colors[i%len(colors)], alpha=0.7)

ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=15, ha='right')
ax.set_yticklabels(y_values, ha='left')
ax.set_title('Volunteer Involvement and Impact of Major Nonprofit Organizations')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/257_202312310050.png')
plt.close()
