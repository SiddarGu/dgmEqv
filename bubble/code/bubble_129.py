import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors
import matplotlib.cm as cm

# Data processing
data_str = "Facebook,2.8,70.7,79,8\nYouTube,2,15.15,84,9\nInstagram,1.082,20,82,7\nTwitter,0.330,3.46,72,6\nLinkedIn,0.310,8.05,86,7\nTikTok,0.689,1,87,8"
data_labels = ["Active Users (Billions)", "Revenue (Billions $)", "Satisfaction Rate (%)", "Popularity Score (Out of 10)"]
data = np.array([i.split(',')[1:] for i in data_str.split('\n')], dtype=float)
line_labels = [i.split(',')[0] for i in data_str.split('\n')]

# Normalization and colormap setup
norm = mcolors.Normalize(vmin=data[:, 3].min(), vmax=data[:, 3].max())
cmap = cm.get_cmap('viridis')

# Plotting
fig, ax = plt.subplots(figsize=(10, 8))
for i, line_label in enumerate(line_labels):
    color = cmap(norm(data[i, 3]))
    size = 10 * data[i, 2]  # Scaling size by active users
    ax.scatter(data[i, 0], data[i, 1], label=line_label + f' {data[i, 2]}', color=color, s=size, edgecolors='k')

# Legend and labels
ax.legend(title="Platforms", loc='lower right')
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.set_title('Social Media Performance Analysis in 2023')

# Colorbar for popularity score
sm = cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
cbar = plt.colorbar(sm)
cbar.set_label(data_labels[3])

plt.grid(True)
# Layout adjustments
plt.tight_layout()

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/194_202312310045.png')

plt.clf()
