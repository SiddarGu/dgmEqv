import matplotlib.pyplot as plt

# Given data
data_labels = ['Research Funding ($Million)', 'Number of Projects']
line_labels = [
    '100-200', '200-300', '300-400', '400-500', 
    '500-600', '600-700', '700-800', '800-900', '900-1000'
]
data = [
    8, 10, 12, 14, 
    9, 7, 5, 4, 3
]

# Create figure and add a subplot
fig = plt.figure(figsize=(12, 8))  # specify the larger figure size
ax = fig.add_subplot(111)

# Plot data
ax.bar(line_labels, data, color=plt.cm.Paired.colors)  # Use the paired colormap for fancy colors

# Set the grid
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Set title and labels
ax.set_title('Research Funding Allocation Across Science and Engineering Projects')
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

# Set x-axis labels on separate lines if too long or rotate if necessary
ax.set_xticklabels(line_labels, rotation=45, ha="right")

# Automatically tighten the layout
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/151.png'
plt.savefig(save_path, format='png')

# Clear figure
plt.clf()
