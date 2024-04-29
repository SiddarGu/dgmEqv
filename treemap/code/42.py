import matplotlib.pyplot as plt
import squarify

# Transform the provided data into three variables
data_labels = ['Professional Sports', 'Movies', 'Music Industry', 'Gaming', 'Television', 'Live Events', 'Publishing', 'Amusement Parks']
line_labels = ['Revenue Share (%)']
data = [40, 20, 15, 10, 5, 5, 3, 2]

# Define the color palette (with 8 colors)
colors = plt.cm.tab20c.colors[:len(data_labels)]

# Create a figure with larger figsize to prevent content from being displayed
plt.figure(figsize=(12, 8))

# Create a treemap
squarify.plot(sizes=data, label=data_labels, color=colors, alpha=0.6)

# Add a title to the figure
plt.title('Revenue Distribution in Sports and Entertainment Industry')

# Remove the axes
plt.axis('off')

# Pad the figure to prevent content from getting cut off
plt.tight_layout()

# Define the save path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/42.png'

# Ensure the directory exists
import os
os.makedirs(os.path.dirname(save_path), exist_ok=True)

# Save the figure
plt.savefig(save_path, dpi=300)

# Clear the current image state so that the IPython notebook interface remains clear
plt.clf()
