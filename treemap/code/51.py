import matplotlib.pyplot as plt
import squarify

# Given data
data = [
    ["Assembly", 22],
    ["Casting", 18],
    ["Molding", 17],
    ["Machining", 15],
    ["Forming", 10],
    ["Welding", 8],
    ["Finishing", 5],
    ["3D Printing", 3],
    ["Additive Manufacturing", 2]
]

# Extracting labels and values
line_labels = [item[0] for item in data]
values = [item[1] for item in data]

# Setup parameters for the figure
plt.figure(figsize=(12, 8), dpi=100)

# Create a treemap
squarify.plot(sizes=values, label=line_labels, alpha=0.8, pad=True)

# Add title
plt.title("Efficiency Distribution in Manufacturing Processes")

# Remove axes
plt.axis('off')

# Adjust layout to prevent content from being cut off
plt.tight_layout()

# Save the figure
save_path = "/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/51.png"
plt.savefig(save_path, format='png')

# Clear the current state
plt.clf()
