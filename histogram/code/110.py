import matplotlib.pyplot as plt
import os

# Assigning data_labels, data, and line_labels from the given data
data_labels = ['Property Value Range ($ \'000)', 'Number of Houses Sold']
line_labels = ['100-200', '200-300', '300-400', '400-500', '500-600', 
               '600-700', '700-800', '800-900', '900-1000', '1000+']
data = [112, 98, 75, 63, 50, 45, 30, 15, 10, 5]

# Creating figure and axis objects
plt.figure(figsize=(10, 8))
ax = plt.subplot(111)

# Plotting the data as a vertical histogram
ax.bar(line_labels, data, color='skyblue')

# Adding grid, title, labels and adjusting the appearance
ax.set_title('Housing Market Sales Distribution by Property Value', fontsize=14)
ax.set_xlabel(data_labels[0], fontsize=12)
ax.set_ylabel(data_labels[1], fontsize=12)
ax.set_xticklabels(line_labels, rotation=45, ha='right', fontsize=10)
plt.grid(axis='y', linestyle='--', linewidth=0.5)

# Adjust the layout to make sure content is not clipped
plt.tight_layout()

# Save the figure to the specified path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/110.png'
os.makedirs(os.path.dirname(save_path), exist_ok=True)
plt.savefig(save_path)

# Clear the current figure state
plt.clf()
