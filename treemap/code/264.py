import matplotlib.pyplot as plt
import squarify

# Transforming the given data
data_labels = ["Market Share (%)"]
line_labels = ["Banking", "Asset Management", "Insurance", "Fintech", "Private Equity", "Real Estate", "Venture Capital"]
data = [30, 25, 20, 10, 7, 5, 3]

# Preparing the colors (you can customize the color list according to your preference)
colors = plt.cm.Paired(range(len(data)))

# Drawing the treemap
plt.figure(figsize=(12, 8))
squarify.plot(sizes=data, label=line_labels, color=colors, alpha=0.7)
plt.title('Market Share Distribution Across Financial Sectors')

# Making sure everything fits and is clear
plt.axis('off')
plt.tight_layout()

# Saving the image to the specified absolute path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/demo/treemap/png/1014.png'
plt.savefig(save_path, format='png')

# Clearing the current figure's state after saving
plt.clf()
