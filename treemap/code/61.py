import matplotlib.pyplot as plt
import squarify

# Given data
data_labels = ['Social Networking', 'Search Engines', 'Online Shopping', 'Content Streaming', 'News Portals', 'Email Services', 'Online Gaming', 'Cloud Storage']
data = [30, 20, 15, 13, 9, 7, 4, 2]
line_labels = data_labels  # In this case, each line label corresponds to the data label as there's only one data point per label

# Choose some pleasant colors
colors = plt.cm.Spectral_r([0.1*x/max(data) for x in data])

# Create a figure
plt.figure(figsize=(12, 8))

# Create a treemap
squarify.plot(sizes=data, label=line_labels, color=colors, alpha=0.7, text_kwargs={'fontsize':10, 'wrap':True})

# Set title
plt.title('Web Usage Distribution Across Different Social Media and Online Platforms')

# Remove axes
plt.axis('off')

# Automatically resize the image
plt.tight_layout()

# Save figure to specified path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/61.png'
plt.savefig(save_path, format='png', dpi=300)

# Clear the figure
plt.clf()
