import matplotlib.pyplot as plt
import squarify

# Store the given data into three variables
data_labels = ['Single-Family Homes', 'Apartments', 'Condos', 'Townhouses', 'Manufactured Homes', 'Vacation Homes', 'Multi-Family Homes', 'Commercial Properties', 'Foreclosures']
line_labels = ['Market Share (%)']
data = [30, 25, 15, 10, 5, 5, 4, 3, 3]

# Create a color list
colors = [plt.cm.Spectral(i/float(len(data_labels))) for i in range(len(data_labels))]

# Create a figure
plt.figure(figsize=(12, 8))

# Create a treemap
squarify.plot(sizes=data, label=data_labels, color=colors, alpha=0.7, text_kwargs={'fontsize':10, 'wrap':True})

# Set the title
plt.title('Market Share Distribution Across Property Types in the Housing Market')

# Remove axes
plt.axis('off')

# Adjust the layout to be more compact and remove padding that might clip labels
plt.tight_layout()

# Save the figure with an absolute path
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/158.png', dpi=300, bbox_inches='tight')

# Clear the figure to release the memory
plt.clf()
