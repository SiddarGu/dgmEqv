import matplotlib.pyplot as plt

# Define the data
data_labels = ['Occupancy Rate (%)']
line_labels = ['Budget', 'Mid-Range', 'Luxury', 'Boutique', 'Resort', 'Business']
data = [72.5, 80.6, 85.4, 78.9, 82.3, 75.0]

# Create a figure object using plt.figure
plt.figure(figsize=(10, 6))

# Add a subplot to the figure
ax = plt.subplot(111)

# Plot a vertical histogram
ax.bar(line_labels, data, color='skyblue', edgecolor='black')

# Add a grid for better readability
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)

# Set the title of the figure
plt.title('Hotel Occupancy Rates by Category')

# Rotate X-axis labels if they're too long
plt.xticks(rotation=45, ha='right')

# Handle overlapping text by automatically resizing the image
plt.tight_layout()

# Save the figure to the specified path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/233.png'
plt.savefig(save_path, format='png')

# Clear the current image state
plt.clf()
