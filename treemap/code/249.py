import matplotlib.pyplot as plt
import squarify

# Given data in a structured format
data_labels = ["Healthcare", "Education", "Defense", "Welfare", "Environmental Protection", "Transportation", "Law Enforcement", "Science and Technology", "Energy"]
data = [25, 20, 15, 10, 10, 8, 6, 4, 2]
line_labels = ["Budget Share (%)"]

# Define color palette for treemap
cmap = plt.cm.viridis
mini = min(data)
maxi = max(data)
norm = plt.Normalize(vmin=mini, vmax=maxi)
colors = [cmap(norm(value)) for value in data]

# Create figure
plt.figure(figsize=(16, 9))

# Plots a treemap with the given labels and data
squarify.plot(sizes=data, label=data_labels, color=colors, alpha=0.6)

# Add title
plt.title("Budget Allocation Across Public Policy Areas", fontsize=16)

# Remove axis
plt.axis('off')

# Use tight_layout to automatically adjust subplot params so that the subplot(s) fits in to the figure area
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/249.png'
plt.savefig(save_path, format='png')

# Clear the current image state to avoid conflicts with subsequent plots
plt.clf()
