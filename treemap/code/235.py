import matplotlib.pyplot as plt
import squarify

# Given data, converted to variables
data_labels = ["Online Sales (%)"]
line_labels = ["Electronics", "Clothing", "Home & Garden", "Health & Beauty", "Food & Groceries", "Books & Media", "Toys & Games", "Pet Supplies"]
data = [27, 20, 15, 13, 10, 7, 5, 3]

# Define colors
cmap = plt.cm.coolwarm
mini = min(data)
maxi = max(data)
norm = plt.Normalize(vmin=mini, vmax=maxi)
colors = [cmap(norm(value)) for value in data]

# Determine the size of the figure to prevent content from overlapping
fig = plt.figure(figsize=(12, 8))

# Create a treemap
squarify.plot(sizes=data, label=line_labels, color=colors, alpha=0.7, edgecolor="white", text_kwargs={'fontsize':10})

plt.title("E-commerce Sales Distribution Across Product Categories")
plt.axis('off')  # Disable the axis

# Resize the image to fit all text and labels
plt.tight_layout()

# Save the image to the absolute path
save_path = "/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/235.png"
plt.savefig(save_path, format='png', dpi=300, bbox_inches='tight')

# Clear the current figure after saving to prevent collisions with other plots
plt.clf()
