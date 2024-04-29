import matplotlib.pyplot as plt

# Transforming the given data into three variables: data_labels, data, line_labels
data_labels = ['Research Funds ($Million)', 'Number of Projects']
line_labels = ['0-50', '50-100', '100-150', '150-200', '200-250', '250-300', '300-350', '350-400', '400-450']
data = [28, 35, 22, 15, 9, 5, 3, 1, 1]

# Create a new figure and subplot
plt.figure(figsize=(12, 8))
ax = plt.subplot()

# Plot the data as a horizontal histogram
ax.barh(line_labels, data, color='skyblue', edgecolor='black')

# Adding the title
plt.title("Allocation of Research Funds Across Scientific and Engineering Projects")

# Labels
plt.xlabel(data_labels[1])
plt.ylabel(data_labels[0])

# Adding grid
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Automatically adjust subplot params for a better layout
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/206.png'
plt.savefig(save_path, format='png', dpi=300)

# Clear the current figure's state at the end of the code
plt.clf()
