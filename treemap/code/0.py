import matplotlib.pyplot as plt
import squarify

# Data
data_labels = ['Renewable Energy Production', 'Emission Reduction Initiatives', 
               'Sustainable Agriculture', 'Waste Management and Recycling', 
               'Water Conservation', 'Biodiversity Preservation', 
               'Sustainable Fishing Practices', 'Environmental Education']

data = [30, 25, 15, 10, 7, 6, 4, 3]

# Colors for the treemap parts
colors = plt.cm.viridis_r([0.1+0.7*i/8 for i in range(len(data_labels))])

# Figure setup
plt.figure(figsize=(16, 9))

# Create the treemap
squarify.plot(sizes=data, label=data_labels, color=colors, alpha=0.8)

# Title
plt.title('Allocation of Sustainability Efforts in\nEnvironmental Protection', fontsize=18)

# Remove axes
plt.axis('off')

# Use tight_layout to automatically adjust the size of the figure.
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/0.png'
plt.savefig(save_path, format='png', dpi=300, bbox_inches='tight')

# Clear the current figure state after saving to avoid overlap with any future plots.
plt.clf()
