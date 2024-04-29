import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# data
data = np.array([[156, 79, 182, 150],
                [200, 80, 220, 160],
                [220, 85, 240, 180],
                [230, 90, 260, 200],
                [240, 100, 300, 230]], dtype=np.float32)
x_values = ['2001', '2002', '2003', '2004', '2005']
y_values = ['Number of Patients (thousand)', 'Surgical Procedures (thousand)', 'Emergency Visits (thousand)', 'Health Care Spending ($ Billion)']

# Create a 3D bar chart
fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111, projection='3d')

for i, y in enumerate(y_values):
    ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.ones(len(x_values)) * 50,
             0.4, 0.5, data[:, i], color=np.random.rand(3,),alpha=0.7)

# arrange label position with data position
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))

# label axis
ax.set_xticklabels(x_values, rotation=45, horizontalalignment='right')
ax.set_yticklabels(y_values, wrap=True)

# title and background grid
plt.title('Health Care Utilization and Spending Trends 2001-2005', fontsize=15)
ax.grid(True)

# Auto resize the image by tight_layout()
plt.tight_layout()

# Save the figure
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/96_202312302126.png", dpi=300)

# Clean up the plotting area
plt.close(fig)
