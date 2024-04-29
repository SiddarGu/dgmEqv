import matplotlib.pyplot as plt
import squarify

# Given data
data = [
    ("Anthropology", 18),
    ("Psychology", 15),
    ("History", 15),
    ("Linguistics", 12),
    ("Philosophy", 10),
    ("Sociology", 10),
    ("Economics", 9),
    ("Political Science", 8),
    ("Cultural Studies", 3)
]

# Transform data into variables
data_labels = [label for label, _ in data]
sizes = [size for _, size in data]
line_labels = ['Research Funding (%)']

# Define color palette
colors = plt.cm.Spectral_r([i / float(len(data)) for i in range(len(data))])

# Create a figure with larger figsize
plt.figure(figsize=(12, 8))

# Create the treemap
squarify.plot(sizes=sizes, label=data_labels, color=colors, alpha=0.8, text_kwargs={'wrap': True})

# Set the title
plt.title('Allocation of Research Funding Among Social Sciences and Humanities Fields', fontsize=16)

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/12.png'
plt.savefig(save_path, bbox_inches='tight', dpi=300)

# Clear the current figure state after saving the image
plt.clf()
