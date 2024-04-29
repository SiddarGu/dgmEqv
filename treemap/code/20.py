import matplotlib.pyplot as plt
import squarify

# Given data
data_labels = ['Resource Allocation (%)']
line_labels = [
    'Primary Care',
    'Specialty Care',
    'Emergency Services',
    'Medical Research',
    'Pharmaceuticals',
    'Mental Health Services',
    'Preventive Care',
    'Long-term Care'
]
data = [25, 20, 15, 10, 10, 8, 7, 5]

# Create a figure with larger size for clarity
plt.figure(figsize=(12, 8))

# Create a color palette using a colormap in matplotlib
cmap = plt.cm.Blues
mini=min(data)
maxi=max(data)
norm = plt.Normalize(vmin=mini, vmax=maxi)
colors = [cmap(norm(value)) for value in data]

# Create a treemap with labels
squarify.plot(sizes=data, label=line_labels, color=colors, alpha=0.8)
plt.title('Healthcare Resource Distribution by Segment', fontsize=18)

# Improve layout to accommodate long labels and prevent overlap
plt.axis('off')
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/20.png', bbox_inches='tight')

# Clear the current figure's state to avoid memory issues
plt.clf()
