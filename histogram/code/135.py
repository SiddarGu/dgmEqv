import matplotlib.pyplot as plt

# Data Transformation
data_labels = ['Sales Volume (Million)']
line_labels = ['Dairy Products', 'Bakery Goods', 'Meat and Poultry', 'Confectionery', 'Beverages', 'Frozen Foods', 'Snacks', 'Seafood']
data = [20.5, 15.0, 22.5, 12.0, 30.0, 16.5, 18.0, 10.5]

# Create figure and add subplot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

# Plotting Vertical Histogram
colors = plt.cm.viridis(range(len(data)))
ax.bar(line_labels, data, color=colors)

# Adding Details
ax.set_title('Sales Volume Across Food and Beverage Industry Categories')
ax.set_xlabel('Product Category')
ax.set_ylabel('Sales Volume (Million)')
ax.set_xticklabels(line_labels, rotation=45, ha='right', wrap=True)
ax.grid(True, which='both', linestyle='--', linewidth=0.5)

# Automatically adjust subplot params to give specified padding
plt.tight_layout()

# Save the image
save_path = '/cpfs01/shared/ADLab/datasets/chart_large_simulation_liuqi/histogram/png/135.png'
plt.savefig(save_path, format='png', bbox_inches='tight', dpi=300)

# Clear the figure to avoid memory issues
plt.clf()
