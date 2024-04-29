import matplotlib.pyplot as plt
import squarify

# Data representation
data_labels = ['Sales Contribution (%)']
line_labels = [
    'Snacks',
    'Beverages',
    'Ready-to-eat Meals',
    'Dairy Products',
    'Confectionery',
    'Bakery Goods',
    'Frozen Foods',
    'Organic Food'
]
data = [25, 20, 15, 14, 10, 8, 5, 3]

# Define colors
colors = plt.cm.tab20c.colors

# Create a figure
plt.figure(figsize=(12, 8), dpi=100)

# Create a treemap
squarify.plot(sizes=data, label=line_labels, color=colors, alpha=0.7)

# Set title
plt.title("Market Share of Product Categories in the Food and Beverage Industry", fontsize=18)

# Remove axes
plt.axis('off')

# Auto resize layout to prevent content from being cropped
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/239.png'
plt.savefig(save_path, format='png')

# Clear the current figure's state
plt.clf()
