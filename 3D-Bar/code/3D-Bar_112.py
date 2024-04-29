import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from operator import itemgetter

# Parse data
txt = 'Year,Auto Production (Million Units),Electronics Production (Million Units),Textiles Production (Million Units),Food Manufacturing Production (Million Units)\n 2019,5,12,32,16\n 2020,10,11,33,25.1\n 2021,15,12,40,32.5\n 2022,16,14,35,31.6\n 2023,20,20,45,35.5'
lines = txt.split('\n')
header_line = next(line for line in lines if not line.isspace())
headers = header_line.split(',')
x_values = [row.split(',')[0] for row in lines[1:]]  # years
y_values = headers[1:]  # metrics
data = np.array([list(map(float,row.split(',')[1:])) for row in lines[1:]])  # the numerical data

# Plot 
fig = plt.figure(figsize=(12,8))
ax  = fig.add_subplot(111, projection='3d')
for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 0.4, 0.6, data[:,i])

# Set labels and ticks    
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, va='center')
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation = 45, ha='right')

# Set viewing angle
ax.view_init(azim=-65, elev=45)

# Title and settings
ax.set_title('Overview of Manufacturing and Production - 2019 to 2023')
plt.tight_layout()

# Save figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/222_202312302235.png', dpi=100)
plt.clf()
