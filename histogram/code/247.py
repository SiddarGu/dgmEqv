import matplotlib.pyplot as plt

# Data extraction and transformation
data_labels = ['Occupancy Rate (%)', 'Number of Hotels']
line_labels = ['0-20', '20-40', '40-60', '60-80', '80-100']
data = [6, 12, 20, 26, 16]

# Create figure and histogram
plt.figure(figsize=(10, 8))
ax = plt.subplot()

# Plot horizontal bar chart
ax.barh(line_labels, data, color=plt.cm.tab20c.colors)

# Set title and labels
ax.set_title('Hotel Occupancy Rates Across the Country')
ax.set_xlabel(data_labels[1])
ax.set_ylabel(data_labels[0])

# Improve layout and aesthetics
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(rotation=45)
plt.tight_layout()

# Setting a larger bottom to prevent overlapping of x-tick labels
plt.subplots_adjust(bottom=0.2)

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/247.png'
plt.savefig(save_path, dpi=300)

# Clear the current figure's state
plt.clf()
