import matplotlib.pyplot as plt
import squarify

# Data and labels
data_labels = ["E-Commerce", "Social Media", "Streaming Services", "Online Gaming", "Remote Work", "Education", "Cloud Services", "Cybersecurity"]
line_labels = ["Usage Percentage (%)"]
data = [18, 25, 20, 15, 10, 5, 4, 3]

# Create a sized figure
plt.figure(figsize=(12, 8))

# Creating a color palette
cmap = plt.cm.Spectral
mini = min(data)
maxi = max(data)
norm = plt.Normalize(mini, maxi)
colors = [cmap(norm(value)) for value in data]

# Plot the treemap
squarify.plot(sizes=data, label=data_labels, color=colors, alpha=0.7)

# Set title of the figure
plt.title('Online Usage Distribution Across Different Internet Activities', fontsize=14)

# Remove the axes
plt.axis('off')

# Use tight_layout to automatically adjust the size
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/67.png'
plt.savefig(save_path, format='png', bbox_inches='tight')

# Clear the current figure state after saving the plot
plt.clf()
