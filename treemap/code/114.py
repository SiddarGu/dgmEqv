import matplotlib.pyplot as plt
import squarify

# Data variables
data_labels = ['Professional Sports', 'Movies', 'Music Industry', 'Video Gaming', 'Television', 'Books and Publishing', 'Theater', 'Amusement Parks']
data = [25, 20, 18, 15, 10, 7, 3, 2]
line_labels = ['25%', '20%', '18%', '15%', '10%', '7%', '3%', '2%']

# Create a figure
plt.figure(figsize=(12, 8))
ax = plt.gca()

# Create a treemap
colors = plt.cm.tab20c.colors
squarify.plot(sizes=data, label=data_labels, value=line_labels, ax=ax, color=colors)

# Wrap label texts
ax.set_xticks([])
ax.set_yticks([])
ax.axis('off')

# Set the title of the figure
plt.title('Sports and Entertainment Industry Market Share Distribution', fontsize=16)

# Automatically resize the image
plt.tight_layout()

# Save the image to the specified path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/114.png'
plt.savefig(save_path, format='png', dpi=150)

# Clear the current image state
plt.clf()
