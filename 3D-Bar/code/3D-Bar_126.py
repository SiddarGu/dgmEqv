import matplotlib.pyplot as plt
import numpy as np

# Define data
data_str = 'Platform,Monthly Active Users (Millions),Average Session Duration (Minutes),Annual Revenue ($Billions)\nFacebook,245,200,851\nTwitter,330,100,346\nInstagram,1000,280,200\nLinkedIn,260,170,860\nYouTube,2000,400,151'
data_list = [i.split(',') for i in data_str.split('\n')]

y_values = data_list[0][1:]
x_values = [i[0] for i in data_list[1:]]
data = np.array([i[1:] for i in data_list[1:]], dtype=np.float32)

# Create figure for 3D bar chart
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Set bar dimensions
x_dim = np.arange(len(x_values))
y_dim = 0.3
z_dim = 0.1

# Plot each column of data
for i in range(len(y_values)):
    ax.bar3d(x_dim, [i]*len(data[:, i]), np.zeros(len(data[:, i])), z_dim, y_dim, data[:, i], color='b', shade=True)

# Set label position and names
ax.set_xticks(x_dim)
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=18)
ax.set_yticklabels(y_values, rotation=-22, va='center')

# Set parameters for better readability and visualization
ax.view_init(elev=20, azim=-50)
ax.set_title('Comparison of Major Social Media Platforms')
plt.grid(True)
plt.tight_layout()

# Save fig
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/98_202312302126.png')
plt.close(fig)
