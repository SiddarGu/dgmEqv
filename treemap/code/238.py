import matplotlib.pyplot as plt
import squarify

# Transformed variables
data_labels = ['Percentage of Practicing Lawyers (%)']
line_labels = ['Criminal Defense', 'Corporate Law', 'Family Law', 'Immigration Law', 'Personal Injury', 
               'Estate Planning', 'Intellectual Property', 'Tax Law', 'Environmental Law']
data = [18, 22, 15, 10, 12, 8, 7, 5, 3]

# Create a figure with a larger size to prevent content from being cramped
plt.figure(figsize=(12, 8))

# Create a color palette
cmap = plt.cm.viridis
mini = min(data)
maxi = max(data)
norm = plt.Normalize(vmin=mini, vmax=maxi)
colors = [cmap(norm(value)) for value in data]

# Use squarify to plot the treemap
squarify.plot(sizes=data, label=line_labels, color=colors, alpha=0.8, edgecolor="white", linewidth=2)

# Set the title of the figure
plt.title('Proportion of Practicing Lawyers in Various Legal Fields')

# Remove the axes
plt.axis('off')

# To deal with long label texts, wrap the text with set_size and set_horizontalalignment
for label in plt.gca().texts:
    label.set_size(10)
    label.set_horizontalalignment('center')

# Automatically resize the image and tidy up the layout
plt.tight_layout()

# Save the image to the absolute path as specified
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/238.png'
plt.savefig(save_path, bbox_inches='tight', dpi=300)  # Ensure high resolution for clarity

# Clear the current state
plt.clf()

