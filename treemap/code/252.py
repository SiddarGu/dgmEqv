import matplotlib.pyplot as plt
import squarify

# Data processing
data_labels = ['Revenue Share (%)']
line_labels = ['Professional Sports', 'Cinema Box Office', 'Music Industry', 'Video Gaming', 'Television Broadcasts', 'Live Theatre']
data = [35, 15, 15, 20, 10, 5]

# Colors for the treemap
colors = plt.cm.viridis(range(len(data)), alpha=0.8)

# Create a figure
fig = plt.figure(figsize=(12, 8))

# Plotting the treemap with labels
squarify.plot(sizes=data, label=line_labels, color=colors, pad=True)

# Title of the figure
plt.title('Revenue Distribution Across Sports and Entertainment Sectors in 2023')

# Tight layout for better spacing
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/demo/treemap/png/1002.png'
plt.savefig(save_path, bbox_inches='tight', dpi=300)

# Clear the current figure state
plt.clf()
