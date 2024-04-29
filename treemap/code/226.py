import matplotlib.pyplot as plt
import squarify

# Given data
data_labels = ['Research Funding (%)']
line_labels = ['Biotechnology', 'Aerospace Engineering', 'Computer Science', 
               'Mechanical Engineering', 'Electrical Engineering', 
               'Chemical Engineering', 'Environmental Science', 'Materials Science']
data = [22, 18, 17, 14, 12, 9, 6, 2]

# Setting up colors
colors = plt.cm.tab20c.colors  # Using tab20c colormap for varied colors

# Create a figure with a set size
plt.figure(figsize=(12, 8))

# Create a treemap with labels and data
squarify.plot(sizes=data, label=line_labels, color=colors[:len(data)], alpha=0.8)

# Set title of the treemap
plt.title('Allocation of Research Funding Across Science and Engineering Fields')

# Improve layout to avoid content being cut off
plt.tight_layout()

# Save the figure to the specified path
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/226.png')

# Clear the current figure state to prevent overlay of figures in the future
plt.clf()
