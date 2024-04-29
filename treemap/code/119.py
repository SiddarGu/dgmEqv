import matplotlib.pyplot as plt
import squarify

# Given data in string format
raw_data = """Bakery & Confectionery,22
Dairy Products,18
Beverages,20
Meat & Poultry,15
Fruits & Vegetables,10
Snack Foods,8
Grains & Cereals,5
Seafood,2"""

# Parsing the data
data_lines = raw_data.split('\n')
line_labels = [line.split(',')[0] for line in data_lines]
data = [float(line.split(',')[1]) for line in data_lines]
# Since there is only one column of data, we have a single data label
data_labels = ["Market Share (%)"]

# Treemap plot
plt.figure(figsize=(12, 8), dpi=100)
squarify.plot(sizes=data, label=line_labels, alpha=0.7)

# Customizations
plt.title('Market Share Distribution in the Food and Beverage Industry')
plt.axis('off')  # Turns off the axis lines and labels

# To prevent content from being cut off
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/119.png'
plt.savefig(save_path, format='png')  # Saving the figure as png

# Clear the current image state
plt.clf()
