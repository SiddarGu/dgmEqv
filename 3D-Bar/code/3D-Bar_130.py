import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Data
data = np.array([[85, 70, 65, 100],
                 [75, 80, 70, 90],
                 [65, 75, 72, 80],
                 [60, 70, 75, 75],
                 [70, 65, 80, 70],
                 [75, 60, 85, 65],
                 [80, 55, 90, 60]], dtype=np.float32)
x_values = ['Under 18', '18-24', '25-34', '35-44', '45-54', '55-64', '65 and above']
y_values = ['Regular Check-ups', 'Physical Activity', 'Healthy Diet', 'Non-Smokers']

# Figure and Subplot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Create 3D bars for each group
x_labels = np.arange(len(x_values))
for i in range(len(y_values)):
    ax.bar3d(x_labels, [i]*len(x_values), np.zeros(len(x_values)), 0.4, 0.4, data[:, i], color='skyblue', alpha=0.8, edgecolor='white')

# Labels
ax.set_xticks(x_labels)
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45, horizontalalignment='right')
ax.set_yticklabels(y_values, ha='left')

# Title and other settings
ax.set_title('Health and Wellness Habits by Age Group')
ax.set_zlabel('Percentage (%)')
ax.view_init(elev=22, azim=-35)
plt.grid()
plt.tight_layout()

# Save the picture
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/106_202312302126.png')

# clear current figure after saving
plt.clf()
