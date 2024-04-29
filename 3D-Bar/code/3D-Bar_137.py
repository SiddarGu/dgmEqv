import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Data
dat = [
    ["2020", 5000, 70, 650],
    ["2021", 5100, 75, 700],
    ["2022", 5250, 78, 750],
    ["2023", 5450, 79, 800],
    ["2024", 5600, 80, 850]
]

# Transformation
x_values = [i[0] for i in dat]
y_values = ["Number of Enrollments (Thousands)", "Percent of Graduates (%)", "Research Expenditure ($Millions)"]
data = np.array([i[1:] for i in dat], dtype=np.float32)

# Setup
fig = plt.figure(figsize=(10, 10))  # you can change the figure size as needed
ax = fig.add_subplot(111, projection='3d')

# Bar settings
width = 0.3
far = 0.5
size = len(x_values)
colors = ['r', 'g', 'b']

# Plot each bar
for c, k in enumerate(y_values):
    ax.bar3d(np.arange(size), [c]*size, np.zeros(size), width, far, data[:, c], color=colors[c%len(colors)], alpha=0.5)

# Labels settings 
ax.set_xticks(np.arange(size))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45, ha='right')
ax.set_yticklabels(y_values, va='center')

# Title
plt.title('Trends in Higher Education: Enrollments, Graduation, and Research Expenditure (2020-2024)')

# Configuration
plt.grid(True)
ax.view_init(elev=20, azim=-35)
plt.tight_layout()

# Save
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/151_202312302235.png')

# Clear plot
plt.clf()
