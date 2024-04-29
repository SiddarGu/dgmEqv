import matplotlib.pyplot as plt
import squarify

# Transforming the given data into variables
data_labels = ['Natural Gas', 'Coal', 'Nuclear', 'Renewables', 'Oil']
line_labels = ['Utility Usage (%)']
data = [30, 25, 20, 15, 10]

# Set the size of the figure
plt.figure(figsize=(12, 8))

# Create a color palette
cmap = plt.cm.viridis
mini = min(data)
maxi = max(data)
norm = plt.Normalize(vmin=mini, vmax=maxi)
colors = [cmap(norm(value)) for value in data]

# Create a treemap
squarify.plot(sizes=data, label=data_labels, color=colors, alpha=0.8)

# Set title of the figure
plt.title('Utility Usage Distribution by Energy Source', fontsize=18)

# Remove axis
plt.axis('off')

# automatically resize the image
plt.tight_layout()

# Save the image with an absolute path as specified
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/demo/treemap/png/1018.png', bbox_inches='tight', dpi=300)

# Clear current figure state so it doesn't interfere with future plots
plt.clf()
