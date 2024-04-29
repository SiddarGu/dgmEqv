import matplotlib.pyplot as plt
import numpy as np

# Data
data_labels = ['Meat and Poultry', 'Processed Foods', 'Dairy Products', 'Beverages', 'Snacks', 'Confectionery', 'Grains and Cereals', 'Fresh Produce', 'Frozen Foods']
data = [275.2, 315.5, 180.3, 290.4, 200.7, 150.2, 234.1, 212.9, 185.6]
line_labels = 'Sales Volume (Million Dollars)'

# Create a figure and a single subplot
fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(1, 1, 1)

# Plot histogram
ax.bar(data_labels, data, color=plt.cm.Paired(np.arange(len(data_labels))))

# Set title and labels
ax.set_title('Sales Volumes Across Various Food and Beverage Product Categories')
ax.set_xlabel('Product Category')
ax.set_ylabel(line_labels)

# Rotation for the x-axis labels
ax.set_xticklabels(data_labels, rotation=45, ha='right')
ax.set_yticks(np.arange(0, max(data) + 50, 50))

# Add grid for better readability
ax.grid(axis='y', linestyle='--')

# Layout adjustment to avoid layout issues
plt.tight_layout()

# Save figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/11.png'
plt.savefig(save_path)

# Clear the current figure state to avoid interfering with any subsequent plots
plt.clf()
