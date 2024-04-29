import matplotlib.pyplot as plt
import squarify

# Given data being transformed into labels and numerical array
data_labels = ['Consumer Electronics', 'Automobiles', 'Pharmaceuticals', 'Food and Beverage',
               'Textiles', 'Aerospace', 'Chemicals', 'Machinery']
data = [22, 20, 18, 15, 10, 8, 5, 2]
line_labels = ['Production Volume (%)']

# Set the size of the plot to ensure content readability
plt.figure(figsize=(12, 8))

# Plot the data using squarify
colors = plt.cm.Spectral_r(range(len(data)))
squarify.plot(sizes=data, label=data_labels, color=colors, alpha=0.8, text_kwargs={'fontsize':9})

# Set title of the treemap
plt.title('Proportional Manufacturing Output by Category', fontsize=14)

# Remove axes
plt.axis('off')

# Use tight layout to automatically adjust subplot params for the image
plt.tight_layout()

# Save the figure to the specified location
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/1133.png'
plt.savefig(save_path, format='png', dpi=300)

# Clear the current figure state after saving the plot to start fresh next time
plt.clf()
