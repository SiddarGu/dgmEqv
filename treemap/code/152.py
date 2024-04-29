import matplotlib.pyplot as plt
import squarify

# Given data
data_labels = ["Personnel Distribution (%)"]
line_labels = ["Administration", "Sales", "Marketing", "Research and Development", "Customer Service", "Human Resources", "IT", "Logistics", "Finance"]
data = [15, 20, 15, 10, 10, 10, 10, 5, 5]

# Setting up colors (could be any color map or list of colors)
cmap = plt.cm.tab20c
mini = min(data)
maxi = max(data)
norm = plt.Normalize(vmin=mini, vmax=maxi)
colors = [cmap(norm(value)) for value in data]

# Create a figure with a defined size
plt.figure(figsize=(12, 6))

# Create a treemap
squarify.plot(sizes=data, label=line_labels, color=colors, alpha=.7)

# Set the title of the figure
plt.title("Personnel Distribution Across Departments in a Corporate Structure", fontsize=16)

# Remove the axes
plt.axis('off')

# Use tight_layout to automatically resize the image
plt.tight_layout()

# Save the figure
save_path = "/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/152.png"
plt.savefig(save_path, format='png')

# Clear the current figure state to avoid overlap if more figures are to be drawn
plt.clf()
