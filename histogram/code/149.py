import matplotlib.pyplot as plt
import os

# Data provided
data_labels = ['Average Sales (Million)']
line_labels = ['Electronics', 'Clothing', 'Home & Garden', 'Health & Beauty', 'Sports & Outdoors', 'Food & Beverages', 'Books & Media', 'Toys & Games']
data = [73.5, 50.2, 62.4, 47.6, 55.3, 68.1, 37.9, 41.5]

# Create figure before plotting
fig, ax = plt.subplots(figsize=(12, 8))

# Plotting the histogram
ax.bar(line_labels, data, color=plt.cm.Paired(range(len(data))))

# Add grid, title, and labels
ax.set_title('Average Sales by Product Category in E-commerce Sector', fontsize=14, fontweight='bold')
ax.set_ylabel(data_labels[0], fontsize=12)
ax.set_xlabel('Product Category', fontsize=12)
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.yticks(fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Automatically resize the image by tight_layout() before saving
plt.tight_layout()

# Path where image will be saved. Ensure path exists or create it
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/149.png'
os.makedirs(os.path.dirname(save_path), exist_ok=True)

# Save the figure
plt.savefig(save_path)

# Clear the current image state
plt.clf()
