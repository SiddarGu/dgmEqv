import matplotlib.pyplot as plt

# Given data setup
data_labels = ['Freight Volume (million metric tons)']
line_labels = ['Road', 'Rail', 'Air', 'Water', 'Pipeline']
data = [1450, 1750, 320, 2400, 1850]

# Create the figure with a specified figsize to prevent content cut-off
plt.figure(figsize=(10, 8))
ax = plt.subplot(111)  # add a subplot in the figure

# Create the histogram
ax.bar(line_labels, data, color=['blue', 'green', 'red', 'cyan', 'magenta'])

# Set title
ax.set_title('Freight Volume Comparison by Transportation Mode')

# Set label rotation to prevent overlap
plt.xticks(rotation=45, ha='right')

# Show grid
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Automatically adjust the figure layout
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/201.png', dpi=300)

# Clear the current figure state to prevent interference with other plots that might follow
plt.clf()
