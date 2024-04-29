import matplotlib.pyplot as plt
import squarify

# The provided data
data_labels = ['Cereals', 'Vegetables', 'Fruits', 'Oilseeds',
               'Meat, Dairy, and Eggs', 'Fisheries', 'Spices', 'Beverages']
line_labels = ['Production Share (%)']
data = [30, 25, 20, 10, 8, 4, 2, 1]

# Plotting the treemap
plt.figure(figsize=(12, 8))
colors = plt.cm.Paired(range(len(data)))  # Choose a color palette
squarify.plot(sizes=data, label=data_labels, color=colors, alpha=0.7, text_kwargs={'wrap': True})

# Setting the title
plt.title('Global Agriculture: Production Share by Crop Type', fontsize=16)

# Removing the axes
plt.axis('off')

# Automatic adjustment of plot parameters to give specified padding
plt.tight_layout()

# Saving the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/150.png'
plt.savefig(save_path, format='png', dpi=300)

# Clear the current figure's state to prevent interference with any future plots
plt.clf()
