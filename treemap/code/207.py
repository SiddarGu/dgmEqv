import matplotlib.pyplot as plt
import squarify

# Given data transformed into variables
data_labels = ['Exhibition Attendance (%)']
line_labels = ['Painting', 'Sculpture', 'Photography', 'Digital Art', 'Performing Arts', 'Film', 'Literature', 'Multimedia Art']
data = [25, 20, 15, 15, 10, 7, 5, 3]

# The size of the figure is set to be larger to prevent content from being truncated
plt.figure(figsize=(12, 8))

# Plotting the treemap with labels rotated for better visibility if they are too long
squarify.plot(sizes=data, label=line_labels, alpha=.8)

plt.title('Exhibition Attendance Distribution Across Art Forms', fontsize=16)
plt.axis('off')

# Using tight_layout to automatically adjust the size and position of subplots to fit into the figure area
plt.tight_layout()

# Saving the figure to the specified absolute path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/207.png'
plt.savefig(save_path, format='png', dpi=300)

# Clearing the current figure's state for further use
plt.clf()
