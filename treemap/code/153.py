import matplotlib.pyplot as plt
import squarify

# Given data
data_labels = ['Market Share (%)']
line_labels = ["Bakery & Confectionery", "Dairy Products", "Beverages", "Processed Foods",
               "Meat & Poultry", "Organic Foods", "Seafood", "Snack Foods"]
data = [22, 18, 15, 14, 13, 10, 5, 3]

# The color list size should be at least as large as the number of labels
colors = plt.cm.tab20c.colors

# Creating the treemap
plt.figure(figsize=(12, 8))
squarify.plot(sizes=data, label=line_labels, color=colors[:len(data)], alpha=0.7, text_kwargs={'fontsize':9, 'wrap':True})

# Title
plt.title("Market Share Distribution within the Food and Beverage Industry", fontsize=18)

# Removing the axes
plt.axis('off')

# Automatically resize the image
plt.tight_layout()

# Save the file 
save_path = "/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/153.png"
plt.savefig(save_path, format='png', dpi=300)

# Clear the current image state
plt.clf()
