import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# process the data
raw_data = 'Country,Life Expectancy (Years),Healthcare Spending ($ Billion),Number of Hospitals\n USA,78.6,3700,6000\n Germany,81.1,470,2000\n Japan,84.1,430,8500\n UK,81.2,270,1400\n Canada,82.1,200,700 '
rows = raw_data.strip().split('\n')
y_values = rows[0].split(',')[1:]
x_values = [row.split(',')[0] for row in rows[1:]]
z_data = np.array([list(map(np.float32, row.split(',')[1:])) for row in rows[1:]]).T  # transpose the data

# create figure and draw bars
fig = plt.figure(figsize=(12, 8))  # create figure
ax = fig.add_subplot(111, projection='3d')  # add 3d subplot

for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 0.4, 0.8, z_data[i], alpha=0.6)

# set labels
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45, ha='right')
ax.set_yticklabels(y_values, ha='left')

# enhance view
plt.tight_layout()
plt.title('A comparison of Healthcare Metrics by Country')
plt.grid(True)

# save and close
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/197_202312302235.png', dpi=300)
plt.clf()
