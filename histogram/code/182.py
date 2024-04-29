import matplotlib.pyplot as plt

# Transforming the given data
data_labels = ["Occupancy Rate (%)", "Number of Hotels"]
line_labels = ["0-20", "20-40", "40-60", "60-80", "80-100"]
data = [3, 5, 15, 25, 8]

# Create a figure with specified size to fit the content
plt.figure(figsize=(10, 8))

# Add a subplot to the figure
ax = plt.subplot()

# Plot horizontal histogram
ax.barh(line_labels, data, color=plt.cm.Paired.colors)

# Set the title of the figure
plt.title('Hotel Occupancy Rates Across Different Classes')

# Use tight_layout to automatically adjust the size
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/182.png')

# Clear the current image state
plt.clf()
