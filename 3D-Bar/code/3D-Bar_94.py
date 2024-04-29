import numpy as np
import matplotlib.pyplot as plt

# Input and format data
data = np.array([
    [2018, 600, 650, 700],
    [2019, 610, 660, 720],
    [2020, 625, 675, 730],
    [2021, 630, 680, 740],
    [2022, 640, 690, 750]
], dtype=np.float32)

x_values = data[:, 0]
y_values = ["Education", "Healthcare", "Defense"]
data = data[:, 1:]

# Create 3D figure and subplot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Set colors and alpha for the bars
colors = ['blue', 'green', 'red']
alpha = 0.7

# Plot data
for c, k in enumerate(y_values):
    xs = np.arange(len(x_values))
    ys = data[:, c]
    ax.bar(xs, ys, zs=c, zdir='y', color=colors[c], alpha=alpha, align='center')

ax.set_xticks(np.arange(len(x_values)))
ax.set_xticklabels(x_values, rotation=20)
ax.set_yticks(np.arange(len(y_values)))
ax.set_yticklabels(y_values, ha='left')

# Viewing angles
ax.view_init(elev=20., azim=-35)

# Set axes labels and title
ax.set_xlabel("Year")
ax.set_ylabel("Public Area")
ax.set_zlabel("Funding (Billion $)")
ax.set_title('Government Funding Allocation over the Years for Key Public Areas')

# Automatically resize the image
plt.tight_layout()

# Save figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/155_202312302235.png')

# Clear image
plt.close(fig)
