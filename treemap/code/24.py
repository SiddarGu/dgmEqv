import matplotlib.pyplot as plt
import squarify

# Data preparation
data_labels = ['Machinery', 'Electronics', 'Pharmaceuticals', 'Food Products', 
               'Automotive', 'Textiles', 'Plastics', 'Aerospace']
line_labels = ['Percentage of Total Production (%)']
data = [22, 20, 17, 16, 10, 8, 4, 3]

# Creating a color palette
colors = plt.cm.tab20c.colors

# Plot
fig, ax = plt.subplots(figsize=(12, 8))
squarify.plot(sizes=data, label=data_labels, color=colors, alpha=0.8, text_kwargs={'fontsize':10, 'wrap':True})

# Title and settings
plt.title('Percentage Distribution of Manufacturing Production by Product Type in 2023')
plt.axis('off')

# Automatic resize of the image and adjust layout before saving
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/24.png'
plt.savefig(save_path, format='png', dpi=300)

# Clear the current image state
plt.clf()

