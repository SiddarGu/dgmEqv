import matplotlib.pyplot as plt
import squarify

# Parsing data into variables
data_labels = ["Healthcare", "Education", "Defense", "Social Security", "Infrastructure", "Energy", "Science & Research", "Environment", "Agriculture"]
data = [25, 20, 15, 15, 10, 5, 5, 3, 2]
line_labels = ["Policy Spending (%)"]

# Plot the treemap
fig, ax = plt.subplots(1, figsize = (12, 8))
squarify.plot(sizes=data, label=data_labels, alpha=0.8)
plt.axis('off')
plt.title("Allocation of Government Spending on Public Policy Categories")

# Resize the figure
plt.tight_layout()

# Save the figure to an absolute path
plt.savefig("/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/1109.png", dpi=300, bbox_inches='tight')

# Clear the current figure state to avoid overlap with any future plots
plt.clf()
