import matplotlib.pyplot as plt
import squarify

# Data
data_labels = ['Market Share (%)']
line_labels = ['Snack Foods', 'Beverages', 'Packaged Meals', 'Dairy Products', 'Confectionery', 'Health Foods', 'Frozen Foods']
data = [25, 30, 20, 10, 7, 5, 3]

# Colors for the squares
# colors = plt.cm.viridis_r

# Create a figure with figsize large enough to prevent content from overlapping
plt.figure(figsize=(12, 8))
# Create the treemap
squarify.plot(sizes=data, label=line_labels, alpha=0.8)
plt.title('Market Share Distribution in the Food and Beverage Industry', fontsize=18)

# Improving the layout
plt.axis('off')
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/chart_simulation_final/treemap/png/204.png', format='png', dpi=300)

# Clear the current image state
plt.clf()
