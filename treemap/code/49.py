import matplotlib.pyplot as plt
import squarify

# Data preparation
data_labels = ['Market Share (%)']
line_labels = [
    'Snack Foods',
    'Non-Alcoholic Beverages',
    'Dairy Products',
    'Alcoholic Beverages',
    'Confectionery',
    'Meat and Poultry',
    'Seafood',
    'Grains and Cereals'
]
data = [20, 20, 15, 15, 10, 10, 5, 5]

# Set larger figsize to prevent content from being undisplayed
plt.figure(figsize=(12, 8))

# Create a treemap
colors = plt.cm.viridis([0.5 + (i / max(data)) * 0.5 for i in data])
squarify.plot(sizes=data, label=line_labels, color=colors, alpha=0.7)

# Add title and format it
plt.title('Market Share of Product Types in the Food and Beverage Industry')

# Resize the image using tight_layout and save it
plt.tight_layout()
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/49.png')

# Clear the current image state
plt.clf()
