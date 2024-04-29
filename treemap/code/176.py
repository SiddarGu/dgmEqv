import matplotlib.pyplot as plt
import squarify

# Data
data_labels = ['Budget Allocation (%)']
line_labels = ['Defense', 'Healthcare', 'Education', 'Social Security',
               'Infrastructure', 'Science and Research', 'Energy and Environment', 'Agriculture']
data = [30, 20, 15, 12, 10, 8, 3, 2]

# Create a figure with a larger figsize
plt.figure(figsize=(12, 8))

# Color palette for the treemap
colors = plt.cm.Spectral_r([i/max(data) for i in data])

# Creating the treemap with labels
squarify.plot(sizes=data, label=line_labels, color=colors, alpha=0.7, text_kwargs={'fontsize':12, 'wrap':True})

# Title of the figure
plt.title('Budget Allocation Across Different Government Policy Areas in 2023', fontsize=14)

# Remove axis
plt.axis('off')

# Adjust subplots and layout to fit the content
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/176.png'
plt.savefig(save_path, format='png', bbox_inches='tight')

# Clear the current image state
plt.clf()
