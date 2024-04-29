import matplotlib.pyplot as plt
import squarify

# Data extraction
data_labels = ['Online Sales (%)']
line_labels = ['Electronics', 'Fashion', 'Home & Garden', 'Health & Beauty',
               'Sports & Outdoors', 'Books & Media', 'Toys & Games', 'Food & Beverage']
data = [25, 20, 15, 13, 10, 9, 5, 3]

# Set the figure size to be larger to accommodate labels and prevent cluttering
plt.figure(figsize=(12, 8))

# Create a color palette
colors = plt.cm.Paired(range(len(data)))

# Create a treemap
squarify.plot(sizes=data, label=line_labels, color=colors, alpha=0.8)

# Set the title of the figure
plt.title('E-commerce Sales Distribution by Product Category', fontsize=18)

# Remove the axis
plt.axis('off')

# Automatically adjust subplot params for the figure to fit into the figsize.
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/244.png'
plt.savefig(save_path, format='png', dpi=100, bbox_inches='tight')

# Clear the current state of plt
plt.clf()
plt.close()
