import matplotlib.pyplot as plt
import squarify

# Given data
data_labels = ['Healthcare', 'Education', 'Defense', 'Welfare', 'Pensions', 'Transportation', 'Energy', 'Science/Technology']
data = [24, 20, 19, 14, 10, 6, 4, 3]
line_labels = ['Government Spending (%)']

# Create a figure of sufficient size to display content
plt.figure(figsize=(12, 8))

# Create a treemap with labels and sizes
squarify.plot(sizes=data, label=data_labels, pad=True, alpha=0.6)

# Set title of the treemap
plt.title('Allocation of Government Spending Across Policy Areas in 2023')

# Remove the axes
plt.axis('off')

# Use tight_layout to automatically adjust subplot params so that the subplot(s) fits in to the figure area
plt.tight_layout()

# Save the figure with an absolute path
output_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/82.png'
plt.savefig(output_path, bbox_inches='tight')

# Clear the current figure to reset for any future plots
plt.clf()
