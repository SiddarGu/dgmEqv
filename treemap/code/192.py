import matplotlib.pyplot as plt
import squarify

# Data processing
data = [35, 25, 20, 15, 5]
data_labels = ['Road', 'Rail', 'Air', 'Sea', 'Pipeline']
line_labels = ['Logistics Market Share (%)']

# Create figure and axes
fig = plt.figure(figsize=(12, 8))

# Create a treemap
colors = plt.cm.viridis(range(len(data)), alpha=0.7)
squarify.plot(sizes=data, label=data_labels, color=colors, alpha=0.7)

# Add title and style
plt.title('Market Share Distribution in Transportation and Logistics Industry', fontsize=16)
plt.axis('off')

# Resize the plot automatically
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/192.png'
plt.savefig(save_path, format='png', bbox_inches='tight')

# Clear the current figure state after saving
plt.clf()
