import matplotlib.pyplot as plt
import squarify

# Data transformation
data_labels = ["Market Share (%)"]
line_labels = ["Single-Family Homes", "Apartments", "Condominiums", "Townhouses", "Manufactured Homes", "Co-ops", "Vacation Homes"]
data = [40, 25, 15, 10, 5, 3, 2]

# Create a color list
colors = plt.cm.tab20c.colors

# Create figure and set title
plt.figure(figsize=(12, 8))
plt.title("Real Estate Market Share by Housing Type in 2023")

# Create a treemap
squarify.plot(sizes=data, label=line_labels, color=colors, alpha=.8, text_kwargs={'fontsize':9, 'wrap':True})

# Remove the axes
plt.axis('off')

# Automatically adjust subplot params so that the subplot(s) fits in to the figure area
plt.tight_layout()

# Save the figure
save_path = "/cpfs01/user/liuqi/workspace/plotchart/demo/treemap/png/1021.png"
plt.savefig(save_path, format='png', dpi=300)

# Clear the current figure after saving to prevent replotting it in the future
plt.clf()
