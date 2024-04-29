import matplotlib.pyplot as plt
import squarify

# Given data structured into three variables
data_labels = ['Life Sciences', 'Engineering', 'Social Sciences', 'Medicine', 'Humanities', 'Physics', 'Environmental Science', 'Computer Science', 'Mathematics']
data = [25, 20, 15, 13, 10, 7, 5, 3, 2]
line_labels = ['Research Funding (%)']

# Define color palette (optional)
colors = plt.cm.tab20c.colors  # Using tab20c colormap for variety of colors

# Create figure and axes for matplotlib
plt.figure(figsize=(12, 8))  # Set the figure size to prevent content from being cut off

# Create treemap with squarify
squarify.plot(sizes=data, label=data_labels, color=colors, alpha=0.6, text_kwargs={'wrap': True})

# Set title and parameters for aesthetics
plt.title('Allocation of Research Funding Across Academic Departments')
plt.axis('off')  # Turn off the axes

# Tight layout and save figures
plt.tight_layout()
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/101.png')  # Save the figure with an absolute path
plt.clf()  # Clear current figure state to avoid overlaps
