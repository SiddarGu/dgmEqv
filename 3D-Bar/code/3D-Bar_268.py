import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Data Preparation
data_string = "Department,Number of Employees,Employee Satisfaction (%),Employee Retention (%)/n HR,50,80,85/n Finance,30,75,80/n Marketing,70,85,90/n IT,90,70,75/n Operations,100,90,95"
data_string = data_string.replace("/n ", "\n")
data_string = data_string.split("\n")
x_values = [row.split(',')[0] for row in data_string[1:]]
y_values = data_string[0].split(',')[1:]
data = np.array([list(map(np.float32, row.split(',')[1:])) for row in data_string[1:]])

# Plotting
fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111, projection='3d')

for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 
        0.5, 0.5, data[:, i], alpha=0.8)

ax.set_title('Department-wise Employee Metrics in Human Resources Management')
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticklabels(y_values, ha='left')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/218_202312302235.png')
plt.clf()
