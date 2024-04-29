import matplotlib.pyplot as plt
import squarify

# Prepare the data
data_labels = ['Banking', 'Insurance', 'Investment', 'Real Estate', 'Retail', 'Technology', 'Manufacturing', 'Healthcare']
data = [22, 18, 20, 15, 10, 8, 5, 2]

# Since there are no line labels in the given dataset, we'll have to omit line_labels
# But if it were needed, it could be something like this:
# line_labels = ['Q1', 'Q2', 'Q3', 'Q4']  # Example, actual line_labels might differ

# Create a color palette, mapped to these values
cmap = plt.cm.Blues
mini = min(data)
maxi = max(data)
norm = plt.Normalize(vmin=mini, vmax=maxi)
colors = [cmap(norm(value)) for value in data]

# Draw the treemap
plt.figure(figsize=(12, 8))
squarify.plot(sizes=data, label=data_labels, color=colors, alpha=0.7)

# Add title
plt.title('Proportional Investment Across Business and Finance Sectors', fontsize=16)

# Remove the axes
plt.axis('off')

# Adjust subplot parameters to give the plot more room
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/65.png'
plt.savefig(save_path, format='png', dpi=300)

# Show the plot for debugging purposes, you can comment this line if you don't want to see the plot on screen
plt.show()

# Clear the matplotlib current figure state
plt.clf()
