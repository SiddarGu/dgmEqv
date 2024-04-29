import matplotlib.pyplot as plt
import squarify

# Given data
data_labels = ['Cloud Computing', 'E-commerce', 'Social Media', 'Cybersecurity',
               'Big Data', 'Internet of Things', 'Artificial Intelligence', 'Blockchain']
data = [25, 20, 15, 15, 10, 9, 4, 2]
line_labels = ['Usage Share (%)']

# Setting larger figsize to prevent content from being squeezed
plt.figure(figsize=(12, 8))

# Create a color palette, mapped to these values
colors = plt.cm.Spectral_r([float(val) / max(data) for val in data])

# Draw the treemap
squarify.plot(sizes=data, label=data_labels, color=colors, alpha=0.8)

# Add a title to the plot
plt.title('Technology and Internet Usage Distribution', fontsize=16)

# Remove the axes
plt.axis('off')

# Use tight layout to optimize the spacing of elements
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/165.png'
plt.savefig(save_path, format='png', pad_inches=0.1, bbox_inches='tight')

# Clear the current figure's state
plt.clf()
