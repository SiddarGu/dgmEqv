import matplotlib.pyplot as plt
import squarify

# Data to be plotted
data_labels = ['Biology', 'Engineering', 'Physics', 'Chemistry', 'Environmental Science', 'Computer Science', 'Mathematics', 'Biotechnology']
data = [18, 24, 15, 14, 9, 10, 7, 3]

# Plotting the treemap
plt.figure(figsize=(12, 8))
squarify.plot(sizes=data, label=data_labels, alpha=0.7)

# Adding title and style adjustments
plt.title('Allocation of Research Funding Across Science and Engineering Fields')
plt.axis('off')  # Removes the axes to have a clean treemap

# Resizing to fit the content
plt.tight_layout()

# Saving the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/21.png'
plt.savefig(save_path, format='png', bbox_inches='tight')

# Clearing the figure to prevent overlap with future plots
plt.clf()
