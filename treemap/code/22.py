import matplotlib.pyplot as plt
import squarify

# Given data transformation
data_labels = ['Government Spending (%)']
line_labels = ['Defense', 'Healthcare', 'Education', 'Welfare', 'Infrastructure',
               'Research & Development', 'Agriculture', 'Energy', 'Foreign Aid']
data = [22, 20, 17, 14, 10, 7, 5, 3, 2]

# Create a color palette, the same number of colors as data
colors = plt.cm.Dark2(range(len(data)))

# Create a figure with a defined size
plt.figure(figsize=(12, 8))

# Plot the treemap using squarify
squarify.plot(sizes=data, label=line_labels, color=colors, alpha=0.8)

# Add title
plt.title('Allocation of Government Budget Across Policy Areas in Fiscal Year', fontsize=16)

# Remove axes
plt.axis('off')

# Set tight layout to automatically resize subplots and save the figure
plt.tight_layout()

# Create the directories if they do not exist
import os
directory = "/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/"
if not os.path.exists(directory):
    os.makedirs(directory)

# Save the figure
plt.savefig(f'{directory}22.png', bbox_inches='tight', dpi=300)

# Clear the current figure state to prevent overlapping of figures
plt.clf()
