import matplotlib.pyplot as plt
import squarify

# Define the data
data_labels = ['Electronics', 'Clothing and Apparel', 'Home and Garden', 'Health and Beauty', 
               'Sports and Outdoors', 'Books and Media', 'Food and Beverage', 'Toys and Games', 'Jewelry']
data = [25, 20, 15, 10, 10, 8, 7, 3, 2]

# Colors for different blocks
colors = [plt.cm.Spectral(i/float(len(data))) for i in range(len(data))]

# Create a figure with a specified size to prevent content from being displayed
plt.figure(figsize=(12, 8))

# Create a treemap using squarify
squarify.plot(sizes=data, label=data_labels, color=colors, alpha=0.8)

# Title of the figure
plt.title('Revenue Distribution Across Retail and E-commerce Categories in 2023', fontsize=14)

# Remove axes
plt.axis('off')

# Automatic resizing of the image
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/demo/treemap/png/1013.png')

# Clear the current image state so that the figure doesn't reside in memory
plt.clf()
