import matplotlib.pyplot as plt
import squarify

# Given data
data_labels = ['Production Volume (%)']
line_labels = ['Cereals', 'Vegetables', 'Fruits', 'Meat', 'Dairy', 'Fisheries', 'Oilseeds']
data = [25, 20, 20, 15, 10, 5, 5]

# Create a figure with larger figsize to prevent content being displayed improperly
plt.figure(figsize=(12, 8))

# Create a treemap
colors = plt.cm.viridis(range(len(data)))  # Generate colors for each section
squarify.plot(sizes=data, label=line_labels, color=colors, alpha=0.8, text_kwargs={'fontsize':12, 'wrap':True})

# Set the title
plt.title('Global Agriculture Production Distribution by Crop Type', fontsize=18)

# Remove axis
plt.axis('off')

# Automatically resize the image
plt.tight_layout()

# Save the image with the absolute path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/36.png'
plt.savefig(save_path, format='png', dpi=100)  # dpi can be adjusted for image clarity

# Clear the current image state
plt.clf()
