import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

# Assigned data
data_labels = ["Active Users (Millions)", "Engagement Rate (%)", "Advertising Revenue (Million $)", "Market Share (%)"]
line_labels = ["Facebook", "Instagram", "Twitter", "LinkedIn", "Snapchat", "Pinterest", "TikTok"]
data = np.array([[2400, 45, 30000, 25], [1000, 60, 8000, 15], [500, 50, 6000, 10], [300, 70, 5000, 8], [200, 65, 4000, 5], [100, 55, 3000, 3], [600, 75, 7000, 12]])

# Create figure
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)

# Normalize color and size value
bubble_size = np.interp(data[:,2], (data[:,2].min(), data[:,2].max()), (600,5000))
colors = mcolors.Normalize(data[:,3].min(), data[:,3].max())

# Plot the data
scatter = ax.scatter(data[:,0], data[:,1], c=data[:,3], s=bubble_size, cmap="viridis", alpha=0.6, edgecolors="w", linewidth=1, norm=colors, label=None)

# Plot empty points for legend
for i, line_label in enumerate(line_labels):
    ax.scatter([], [], c='k', alpha=0.3, label=line_label + f' {data[i, 2]}')

# Add legend and colorbar
ax.legend(title=data_labels[2], loc='upper right')
cbar = plt.colorbar(scatter, ax=ax)
cbar.ax.set_title(data_labels[3])

# Adjust settings
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.set_title('Social Media and Web Platform Analysis')
ax.grid(True)
plt.tight_layout()

# Save and show the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/392_202312311429.png', dpi=300)

# Clear figure
plt.clf()
