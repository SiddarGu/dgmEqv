import matplotlib.pyplot as plt

# Given data
data_labels = ['0-50', '50-100', '100-150', '150-200', '200-250', '250-300', '300-350', '350-400', '400-450']
data = [120, 95, 65, 30, 15, 8, 4, 3, 2]
line_labels = ['Number of Sports Events']

# Create the figure with larger figsize
plt.figure(figsize=(12, 7))

# Create one subplot
ax = plt.subplot()

# Plot vertical histogram
ax.bar(data_labels, data, color='skyblue')

# Set title and labels
ax.set_title('Price Distribution for Sports and Entertainment Events Tickets', fontsize=14)
ax.set_xlabel('Ticket Price Range ($)', fontsize=12)
ax.set_ylabel('Number of Sports Events', fontsize=12)

# Add grid to the plot
ax.grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.7)

# Prevent xlabel text from overlapping by rotating them
plt.xticks(rotation=45, ha='right')

# Automatically adjust subplot params for the figure to fit into the figsize window
plt.tight_layout()

# Save the figure to the specified absolute path
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/69.png', format='png', dpi=300)

# Clear the current figure state
plt.clf()
