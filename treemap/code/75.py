import matplotlib.pyplot as plt
import squarify

# Transforming the given data
data_labels = ["Yield (%)"]
line_labels = ["Grains", "Vegetables", "Fruits", "Dairy", "Meat", "Aquaculture"]
data = [40, 20, 20, 10, 6, 4]

# Create a figure for the treemap
plt.figure(figsize=(12, 8))
ax = plt.subplot()

# Create a treemap
squarify.plot(sizes=data, label=line_labels, pad=True, alpha=0.7, text_kwargs={'wrap': True})

# Title of the figure
plt.title("Proportional Yield Distribution in Agriculture and Food Production", fontsize=14)

# Customize the plot (You can adjust padding, border, dimensions, colors, labels, text styling as required)
plt.axis('off')

# Make layout tight to avoid issues like cutting off labels
plt.tight_layout()

# Save the figure
save_path = "/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/1125.png"
plt.savefig(save_path, dpi=300, bbox_inches='tight')

# Clear the current figure state to avoid overlap with any future plots
plt.clf()
