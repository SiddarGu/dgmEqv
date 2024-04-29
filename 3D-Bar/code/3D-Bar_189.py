import numpy as np
import matplotlib.pyplot as plt

# Provide the data
full_data = [
    ['Facebook', 2475, 135, 350],
    ['Instagram', 1100, 53, 95],
    ['LinkedIn', 310, 17, 2],
    ['Twitter', 330, 46, 500],
    ['YouTube', 2000, 40, 300]
]

# Define x_values
x_values = [row[0] for row in full_data]

# Define y_values
y_values = ['Active Users (Millions)', 'Average Daily Usage Time (Minutes)', 'Posts Per Day (Millions)']

# Define data
data = np.array([row[1:] for row in full_data], dtype=np.float32)

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

colors = ['r', 'g', 'b']

# Create 3D bar chart
for i in range(len(data[0])):
    x = np.arange(len(x_values))
    y = np.full(len(x_values), i)
    z = np.zeros(len(x_values))
    dx = np.ones(len(x_values)) * 0.3
    dy = np.ones(len(x_values)) * 0.3
    dz = data[:, i]
    color = colors[i]
    ax.bar3d(x, y, z, dx, dy, dz, color=color, alpha=0.7)

# Add the labels
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=90)
ax.set_yticklabels(y_values, ha='left')

# Set title and labels
ax.set_title('Social Media Usage Analysis')
ax.set_xlabel('Social Media Platform')

plt.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/266_202312310050.png', dpi=300)
plt.close()
