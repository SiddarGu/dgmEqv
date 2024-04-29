import matplotlib.pyplot as plt
import numpy as np

# Data
data = np.array([
    [50, 3.9, 40],
    [80, 3.6, 42],
    [70, 4.1, 38],
    [40, 3.7, 40],
    [100, 3.5, 44]
], dtype=np.float32)
x_values = ['HR', 'IT', 'Marketing', 'Finance', 'Production']
y_values = ['Number of Employees', 'Average Employee Satisfaction Score', 'Average Hours Worked Weekly']

# Plotting
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')

for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 0.4, 0.8, data[:, i], color='b', alpha=0.8)

# Axis Labels
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45, ha='right')
ax.set_yticklabels(y_values, ha='left')

# Figure Tweaks
plt.title('Employee Management Statistics by Department')
plt.grid(True)
ax.view_init(30, -45)
plt.tight_layout()

# Save Figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/228_202312302235.png')

# Clear The Plot
plt.clf()
