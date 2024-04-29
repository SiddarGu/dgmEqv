import numpy as np
import matplotlib.pyplot as plt

# Transforming the data
data = np.array([[50, 150, 75], [40, 120, 48], [35, 110, 38.5], [30, 130, 39], [25, 140, 35]])

y_values = ["Number of Tourists (Millions)", "Average Spending per Tourist ($)", "Total Revenue (Billion $)"]
x_values = ["USA", "France", "Spain", "UK", "Germany"]

# Creating figure
fig = plt.figure(figsize=(10, 8)) 
ax = fig.add_subplot(111, projection='3d') 

# Plotting data
for i in range(len(y_values)):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 0.4, 0.4, data[:, i], alpha=0.8)

# Setting properties
ax.set_xticks(np.arange(len(x_values)) + 0.2)
ax.set_yticks(np.arange(len(y_values)) - 0.2)
ax.set_xticklabels(x_values, rotation=30, horizontalalignment='right')
ax.set_yticklabels(y_values, ha='left')
ax.set_title('Tourism and Hospitality Industry Insights by Country')
ax.view_init(elev=25, azim=165)

# Saving figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/273_202312310050.png')

# Clearing figure
plt.clf()
