import matplotlib.pyplot as plt
import squarify

# Parsing the data into variables
data_labels = ['Automotive', 'Electronics', 'Pharmaceuticals', 'Textiles', 'Machinery', 'Food and Beverage', 'Chemicals', 'Aerospace']
line_labels = 'Share of Manufacturing Output (%)'  # No line_labels as per your instruction, only column label as a title
data = [25, 20, 15, 10, 10, 8, 7, 5]

# Normalize the data to fit the treemap area
norm_data = squarify.normalize_sizes(data, dx=100, dy=100)

# Create the figure with larger figsize to prevent content cutoff
plt.figure(figsize=(12, 8))

# Create the treemap
squarify.plot(sizes=norm_data, label=data_labels, alpha=0.6)

# Additional styling
plt.title('Share of Manufacturing Output by Production Component in 2023', fontsize=18)
plt.axis('off')  # Turn off axes

# Automatically resize the image by tight_layout() before savefig()
plt.tight_layout()

# Save the figure to the specified path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/chart_simulation_final/treemap/png/292.png'
plt.savefig(save_path, dpi=300)  # Save with high dpi for better clarity

# Clear the current image state
plt.clf()