import matplotlib.pyplot as plt
import squarify

# Data setup
data_labels = ['Renewable Energy Usage', 'Emission Reductions', 'Waste Management',
               'Water Conservation', 'Sustainable Agriculture', 'Green Building Practices',
               'Biodiversity Protection']
line_labels = ['Percentage (%)']
data = [40, 25, 15, 10, 5, 3, 2]

# Calculate sizes for the squares
sizes = data

# Color settings (you can choose a color map or define custom colors)
colors = plt.cm.viridis(range(len(data_labels)))

# Create a figure with a set size
plt.figure(figsize=(12, 8))

# Create treemap
squarify.plot(sizes=sizes, label=data_labels, color=colors, alpha=0.7)

# Title setup
plt.title('Proportional Investments in Sustainability Initiatives')

# Remove axis lines
plt.axis('off')

# Set tight_layout to handle sizing issues
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/1139.png'
plt.savefig(save_path, format='png', bbox_inches='tight')

# Clear the current figure's state to prevent any overlap with future plots
plt.clf()
