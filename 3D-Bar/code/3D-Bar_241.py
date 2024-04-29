import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Prepare and transform the data
raw_data = '''
Department,Number of Employees,Staff Retention (%),Promotion Rate (%)
Human Resources,120,85,10
Finance,200,80,15
Marketing,150,90,20
Operations,180,85,18
IT,100,80,12
'''.strip().split('\n')

raw_data = [item.split(',') for item in raw_data]

x_values = [item[0] for item in raw_data[1:]]
y_values = raw_data[0][1:]
data = np.array([item[1:] for item in raw_data[1:]], dtype=np.float32)

# Plotting the data on a 3D bar chart
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection='3d') 

bar_width = 0.4
bar_depth = 0.4
alpha = 0.8

for c, z in zip(y_values, range(len(y_values))):
    xs = np.arange(len(x_values))
    ys = data[:, z]
    ax.bar3d(xs, [z]*len(x_values), np.zeros(len(x_values)), bar_width, bar_depth, ys, color=['b', 'r', 'g', 'y', 'c'][z], alpha=alpha)

# Adjusting view and label positions
ax.view_init(elev=25, azim=-10)
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45, horizontalalignment='right')
ax.set_yticklabels(y_values, ha='left')

# Setting titles and labels
ax.set_title('Employee Management Analysis by Department')
ax.set_xlabel('Department')
ax.set_zlabel('Counts')

# Adjust layout and save plot
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/116_202312302126.png')
plt.clf()
