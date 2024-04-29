import matplotlib.pyplot as plt
import squarify

# Given data
data_str = """Fruits and Vegetables,18
Dairy Products,16
Packaged Foods,15
Beverages,14
Meat and Poultry,12
Seafood,10
Confectionery,8
Grains and Cereals,5
Specialty Foods,2"""

# Transforming data into variables
data_lines = data_str.split('\n')
data_labels = [line.split(',')[0] for line in data_lines]
data = [float(line.split(',')[1]) for line in data_lines]

# Visualize data as treemap
plt.figure(figsize=(12, 8))
colors = plt.cm.tab20c.colors
squarify.plot(sizes=data, label=data_labels, color=colors, alpha=0.8)

# Configure and display the chart
plt.title('Market Share Distribution of Food and Beverage Categories')
plt.axis('off')
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/103.png'
plt.savefig(save_path, format='png', dpi=300, bbox_inches='tight')

# Clear the current image state
plt.clf()
plt.close()
