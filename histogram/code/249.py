import matplotlib.pyplot as plt
import os

# Given data transformation
data_labels = ["Tons Transported (million)"]
line_labels = ["Trucking", "Rail", "Maritime", "Air", "Pipeline"]
data = [732, 540, 321, 98, 410]

# Set the larger figsize to prevent content from being displayed inappropriately
plt.figure(figsize=(10, 8))

# Create a subplot
ax = plt.subplot(1, 1, 1)

# Plot vertical histogram
ax.bar(line_labels, data, color=['blue', 'green', 'red', 'purple', 'orange'])

# Set the title of the figure
plt.title('U.S. Domestic Freight Transportation Modes by Tonnage')

# Add grids to the background
ax.set_axisbelow(True)
ax.yaxis.grid(color='gray', linestyle='dashed')

# Add x-axis label rotation if necessary
ax.set_xticklabels(line_labels, rotation=45, ha="right", wrap=True)

# Automatically resizing the image by tight_layout before saving
plt.tight_layout()

# Save the figure to the given absolute path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/249.png'
os.makedirs(os.path.dirname(save_path), exist_ok=True)
plt.savefig(save_path, format='png')

# Clear the current image state
plt.clf()
