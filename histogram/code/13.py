import matplotlib.pyplot as plt

# Data setup
data_labels = ['Frequency of Shipments']
line_labels = ['Trucks', 'Trains', 'Cargo Ships', 'Air Freight', 'Delivery Vans', 'Bicycles', 'Motorcycles']
data = [650, 320, 220, 180, 500, 60, 100]

# Figure setup
plt.figure(figsize=(12, 8)) # Set a larger figure size to prevent label overlap
ax = plt.subplot(111) # Add a subplot

# Horizontal bar chart
bar_colors = plt.cm.viridis([0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0]) # Use colors to make the chart fancy
ax.barh(line_labels, data, color=bar_colors)

# Add grid
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Set title
plt.title('Frequency of Shipments by Vehicle Type in Logistics Industry')

# Set label rotation for readability
ax.xaxis.set_tick_params(rotation=45)

# Layout adjustment to make room for the labels
plt.tight_layout()

# Save figure to the specified path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/13.png'
plt.savefig(save_path, format='png')

# Clear the current figure state
plt.clf()
