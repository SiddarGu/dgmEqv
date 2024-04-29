import matplotlib.pyplot as plt
import squarify

# Given data
data_labels = ['Revenue Share (%)']
line_labels = ['Professional Sports', 'Film', 'Music', 'Televised Entertainment', 'Video Gaming', 'Live Performances']
data = [35, 30, 15, 10, 6, 4]

# Choose some nice colors for the treemap
colors = plt.cm.Spectral(range(len(data)))

# Set the figure size to ensure readability
plt.figure(figsize=(12, 8))

# Create a treemap using squarify
squarify.plot(sizes=data, label=line_labels, color=colors, alpha=0.7, edgecolor='white', text_kwargs={'fontsize':12})

# Set the title of the figure
plt.title('Revenue Share Distribution in the Sports and Entertainment Industry', fontsize=16)

# Remove axis and show the plot
plt.axis('off')

# Automatically resize the image to fit the contents
plt.tight_layout()

# Save the image
save_path = '/cpfs01/user/liuqi/workspace/plotchart/demo/treemap/png/1031.png'
plt.savefig(save_path, format='png')

# Clear the current image state
plt.clf()
