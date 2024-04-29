import matplotlib.pyplot as plt
import squarify

# Define the data, labels, and data labels
data_labels = ["Budget Allocation (%)"]
line_labels = ["Defense", "Education", "Health and Human Services", "Social Security",
               "Justice", "Transportation", "Energy", "Environmental Protection",
               "International Affairs", "Science and Technology"]
data = [28, 17, 15, 12, 8, 7, 5, 4, 2, 2]

# Create a color palette
colors = plt.cm.Spectral([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])

# Plot treemap
plt.figure(figsize=(12, 8))
squarify.plot(sizes=data, label=line_labels, color=colors, alpha=0.7, text_kwargs={'fontsize':9, 'wrap':True})
plt.title('Budget Allocation for U.S. Government Departments in 2023')

# Remove axes
plt.axis('off')

# Adjust layout to prevent content from being cut off
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/demo/treemap/png/1032.png', format='png', dpi=300)

# Clear the current figure state
plt.clf()
