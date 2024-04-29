import matplotlib.pyplot as plt
import squarify

# Data
data_labels = ['Professional Sports', 'Movies', 'Music Concerts', 'Broadcasting Rights', 'Video Games', 'Theatre Performances', 'Amusement Parks']
data = [28, 22, 19, 14, 10, 4, 3]
line_labels = [f"{label} ({str(value)}%)" for label, value in zip(data_labels, data)]

# Create a treemap
plt.figure(figsize=(12, 8))
squarify.plot(sizes=data, label=line_labels, alpha=.8)

# Title and styling
plt.title('Revenue Distribution in Sports and Entertainment Industry')

# Improve the layout
plt.axis('off')  # Turn off the axis
plt.tight_layout()  # Automatically adjust subplot params

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/1016.png'
plt.savefig(save_path, format='png', bbox_inches='tight', transparent=True, dpi=300)  # Save with high resolution

# Clear the current figure to prevent overlapping of figures
plt.clf()
