import matplotlib.pyplot as plt

# Given data
data_labels = ["Annual Sales (Billion $)"]
line_labels = [
    "Soft Drinks", "Alcoholic Beverages", "Bottled Water", 
    "Fruit Juices", "Tea", "Coffee", "Energy Drinks", "Dairy-Based Drinks"
]
data = [189.1, 155.3, 118.9, 98.7, 60.5, 125.2, 86.5, 76.4]

# Initialize figure
plt.figure(figsize=(10, 8))
ax = plt.subplot()

# Create the horizontal histogram
ax.barh(line_labels, data, color=plt.cm.Paired.colors)

# Add gridlines
ax.grid(True, linestyle='--', which='both', alpha=0.75)

# Set title
plt.title('Annual Sales Comparison Among Beverage Categories')

# Add data labels
for i in range(len(data)):
    plt.text(data[i], i, f"{data[i]}", va='center')

# Adjust layout to fit all labels and minimize overlapping
plt.tight_layout()

# Save the figure with absolute path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/197.png'
plt.savefig(save_path, format='png')

# Clear figure
plt.clf()
