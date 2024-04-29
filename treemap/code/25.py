import matplotlib.pyplot as plt
import squarify

# Transform given data into variables: data_labels, data, line_labels
data_labels = ["Electronics", "Apparel", "Home & Garden", "Health & Beauty", 
               "Sporting Goods", "Books & Media", "Food & Beverage", "Toys & Hobbies", "Others"]

data = [22, 18, 15, 12, 10, 9, 8, 4, 2]

line_labels = ["Percentage (%)"]

# Set up the figure size and plot the treemap
plt.figure(figsize=(12, 8))
squarify.plot(sizes=data, label=data_labels, alpha=0.7)
plt.title("Retail and E-commerce Market Share by Category in 2023")

# Using tight_layout to automatically resize
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/1000.png'
plt.savefig(save_path, format='png', bbox_inches='tight')

# Clear the current figure to free memory
plt.clf()
