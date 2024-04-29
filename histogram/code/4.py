import matplotlib.pyplot as plt

# Defined data
data_labels = ['Renaissance', 'Baroque', 'Neoclassicism', 'Romanticism', 'Impressionism', 'Modernism', 'Postmodernism', 'Contemporary']
data = [275, 320, 215, 198, 400, 180, 150, 225]

# Create a figure with defined figsize to prevent content overlap
plt.figure(figsize=(10, 8))

# Create an subplot to draw the histogram
ax = plt.subplot()

# Plot the data
ax.bar(data_labels, data, color=plt.cm.Paired.colors, edgecolor='black')

# Title and labels
ax.set_title('Artwork Sales Distribution by Historical Era')
ax.set_xlabel('Historical Era')
ax.set_ylabel('Number of Artworks Sold')

# Set x-axis labels with rotation for better readability
plt.xticks(rotation=45, ha='right')

# Enable grid for better readability
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Automatically adjust subplot params so the subplot(s) fits in to the figure area.
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/4.png'
plt.savefig(save_path, format='png')

# Clear the current figure after saving the image
plt.clf()
