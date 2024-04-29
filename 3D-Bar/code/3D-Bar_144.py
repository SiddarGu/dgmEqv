import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Data
table = '''Year, Undergraduate Enrollment, Graduate Enrollment, Faculty Members, Budget( $ Millions)
2018, 8000, 12000, 700, 50
2019, 8100, 12500, 710, 55
2020, 8200, 13000, 720, 60
2021, 8300, 13500, 730, 65'''
lines = table.split('\n')
x_values = [line.split(', ')[0] for line in lines[1:]]
y_values = lines[0].split(', ')[1:]
data = np.array([list(map(np.float32, line.split(', ')[1:])) for line in lines[1:]])

# Create figure
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot data
for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 
              0.4, 0.6, data[:, i], color=np.random.rand(3,), alpha=0.7)

# Set ticks and labels
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45, ha='right')
ax.set_yticklabels(y_values, ha='left')

# Set title
ax.set_title('University Annual Statistics: Enrollment, Faculty, and Budget')

# Set view angle
ax.view_init(30, -60)

# Save figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/145_202312302235.png', dpi=300)

# Clear figure
plt.clf()
