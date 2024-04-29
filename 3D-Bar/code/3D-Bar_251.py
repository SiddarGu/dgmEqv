#import necessary libraries
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Data
data = '''
Year,Movie Released,Concerts Held,Sport Events
2018,320,56,235
2019,420,59,270
2020,285,42,190
2021,380,72,250
2022,450,77,305
'''

# Parse data
lines = data.split('\n')[1:-1]
y_values = lines[0].split(',')[1:]
x_values = [x.split(',')[0] for x in lines[1:]]
data = np.array([x.split(',')[1:] for x in lines[1:]], dtype=np.float32)

# Create figure
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot bars
for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 
             0.4, 0.4, data[:, i], color=plt.cm.viridis(i/len(y_values)), alpha=0.8)
    
# Setup axes
ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=45)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, ha='left')

# Setup title and labels
ax.set_title('Yearly Overview of Sports and Entertainment Events')
ax.set_xlabel('Year')
ax.set_zlabel('Count')
ax.view_init(elev=30, azim=-60)

# Adjust layout and save figure
plt.tight_layout()
fig.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/176_202312302235.png')
plt.close(fig)
