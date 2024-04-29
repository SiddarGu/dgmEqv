import matplotlib.pyplot as plt
import squarify

# Transformed data
data_labels = ['Dairy Products', 'Bakery Goods', 'Beverages', 'Meat & Poultry', 'Seafood', 'Confectionery', 'Snacks', 'Grains & Cereals']
data = [18, 15, 22, 19, 8, 10, 5, 3]
line_labels = [f'{label} ({percent}%)' for label, percent in zip(data_labels, data)]

# Set image size
plt.figure(figsize=(12, 8))

# Create a color palette, lighter to darker shades for larger areas
colors = [plt.cm.Spectral(i/float(len(data))) for i in range(len(data))]

# Create a treemap
squarify.plot(sizes=data, label=line_labels, color=colors, alpha=0.7)

# Add title
plt.title("Sales Distribution Across Food and Beverage Categories in 2023")

# Remove axes
plt.axis('off')

# Resize the image
plt.tight_layout()

# Save the figure to the specified path
plt.savefig("/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/86.png")

# Clear current figure to prevent overwriting on subsequent plots
plt.clf()
