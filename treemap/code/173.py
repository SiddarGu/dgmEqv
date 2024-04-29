import matplotlib.pyplot as plt
import squarify

# Transforming the given data into variables
data_labels = ['Solar', 'Wind', 'Hydroelectric', 'Biomass', 'Geothermal', 'Nuclear', 'Others']
data = [22, 20, 17, 14, 11, 10, 6]
line_labels = ['Renewable Use (%)']

# Create a figure with a larger size for clarity
plt.figure(figsize=(12, 8), dpi=100)

# Using squarify to plot the treemap
color_list = plt.cm.tab20c.colors  # Using a pre-defined color map
squarify.plot(sizes=data, label=data_labels, color=color_list, alpha=0.6)

# Adding the title, and configuring the plot
plt.title('Renewable Energy Utilization Breakdown in Environment and Sustainability', fontsize=14, wrap=True)
plt.axis('off')

# Automatically resizing the image
plt.tight_layout()

# Saving the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/173.png'
plt.savefig(save_path, bbox_inches='tight')

# Clear the current image state to prevent interference with future plots
plt.clf()
