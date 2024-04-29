import matplotlib.pyplot as plt
import squarify

# Provided data as raw strings separated by /n (mimicking newlines).
raw_data = """Product Category,Online Sales Share (%)
Electronics,25
Clothing,20
Home & Garden,15
Health & Beauty,10
Food & Beverage,10
Books & Media,8
Toys & Hobbies,7
Sporting Goods,5"""

# Parsing the raw data into variables.
lines = raw_data.split('\n')
header = lines[0].split(',')
data_labels = [header[1]]  # Extracting the second header as labels for the data.
line_labels = [line.split(',')[0] for line in lines[1:]]  # Extracting the product categories.
data = [float(line.split(',')[1]) for line in lines[1:]]  # Extracting the numerical data.

# Create a figure with larger size for better readability.
plt.figure(figsize=(12, 8))

# Plotting the treemap.
# `color` argument is optional and can be customized.
# colors = plt.cm.viridis(range(len(data)))
squarify.plot(sizes=data, label=line_labels, color=None, pad=True)

# Customizing the plot.
plt.title('E-commerce Sales Distribution Across Product Categories', fontsize=15)
plt.axis('off')  # Treemaps do not need axis.

# Before saving the figure, call tight_layout to automatically adjust the size.
plt.tight_layout()

# Save the figure to an absolute path.
save_path = '/cpfs01/user/liuqi/workspace/plotchart/chart_simulation_final/treemap/png/34.png'
plt.savefig(save_path, bbox_inches='tight', dpi=300)  # DPI can be set higher for clarity.

# Clear the current image state so that the code is idempotent.
plt.clf()
plt.close()

print(f"Treemap saved successfully at {save_path}")
