
# Import Libraries
import matplotlib.pyplot as plt
import numpy as np

# Restructure data
data = [
    [20, 50, 70, 90, 120],
    [25, 60, 80, 95, 125],
    [30, 65, 75, 100, 130],
    [15, 55, 75, 85, 115],
    [35, 70, 80, 90, 110]
]

outliers = [
    [],
    [150],
    [95, 160],
    [150, 180],
    [125]
]

# Plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot()

ax.boxplot(data, whis=1.5)

# Add Outliers
for i, o in enumerate(outliers):
    if o:
        x = np.full(len(o), i + 1)
        ax.plot(x, o, 'ro', fillstyle='none', markersize=5)

# Set Labels
ax.set_title('Score Distribution of Sports Teams in 2020', fontsize=14)
ax.set_ylabel('Score (Points)', fontsize=12)
ax.set_xticklabels(['Team A', 'Team B', 'Team C', 'Team D', 'Team E'], fontsize=12, rotation=45, ha='right', wrap=True)

# Set Background
ax.grid(True, alpha=0.3, axis='y')

# Save Figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/48_202312270030.png', dpi=100)

# Clear
plt.cla()