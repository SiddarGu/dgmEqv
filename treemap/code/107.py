import matplotlib.pyplot as plt
import squarify

# Transforming data into variables
data_labels = ['Workforce Distribution (%)']
line_labels = ['Sales', 'Operations', 'Marketing', 'Human Resources',
               'Product Development', 'Finance', 'Customer Support',
               'IT Services', 'Research and Development']
data = [20, 18, 15, 12, 10, 9, 8, 5, 3]

# Customize matplotlib figure and treemap
fig, ax = plt.subplots(figsize=(12, 8))
cmap = plt.cm.viridis
mini = min(data)
maxi = max(data)
norm = plt.Normalize(vmin=mini, vmax=maxi)
colors = [cmap(norm(value)) for value in data]

# Create the treemap
squarify.plot(sizes=data, label=line_labels, color=colors, alpha=0.8)

# Title and enhancements
plt.title("Workforce Distribution Across Different Departments in a Corporation")
plt.axis('off')

# Resize the figure in a way that content is fitted properly
plt.tight_layout()

# Save figure to the specified path
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/107.png', dpi=300)

# Clear the current figure's state for further plotting if necessary
plt.clf()
