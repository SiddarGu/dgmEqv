import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Data preparation
raw_data = """2019,300,250,20000
2020,350,280,21000
2021,370,300,22000
2022,390,330,23000
2023,425,350,24500 """.split('\n')

raw_data = [i.split(',') for i in raw_data]

# Convert into three variables
y_values = raw_data[0][1:]  
x_values = [i[0] for i in raw_data[1:]]
data = np.array([i[1:] for i in raw_data[1:]], dtype=np.float32)

# Create figure and axes
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot each column of data
for i in range(data.shape[1]):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 
              0.1, 0.1, data[:, i], color=np.random.rand(3), alpha=0.6)

# Labels and title
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticklabels(y_values, ha='left', va='bottom')
ax.set_title('Charitable Contributions, Grants, and Volunteer Work ⁠- 2019 to 2023')

# Adjust viewing angles
ax.view_init(elev=20., azim=-35)

# Save figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/163_202312302235.png')

# Clear the current image state
plt.clf()
