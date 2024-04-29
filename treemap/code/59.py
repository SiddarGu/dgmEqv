import matplotlib.pyplot as plt
import squarify

# Given data is transformed into three variables.
data_labels = ['Single-Family Homes', 'Apartments', 'Condominiums', 'Townhouses', 'Multi-Family Homes']
line_labels = ['Market Share (%)']
data = [30, 25, 20, 15, 10]

# Plot the treemap
plt.figure(figsize=(12, 8))  # Set a larger figure size to improve readability
colors = plt.cm.Spectral([0.2, 0.4, 0.6, 0.8, 1.0])  # Use a color map for more fancy colors

# Create a treemap with squarify
squarify.plot(sizes=data, label=data_labels, color=colors, alpha=0.7, text_kwargs={'fontsize':10, 'wrap':True})
plt.title('Real Estate Market Composition by Housing Type')
plt.axis('off')  # Hide the axes

# Adjust layout for better structure and save the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/59.png', dpi=300)
plt.clf()
plt.close()
