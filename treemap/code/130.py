import matplotlib.pyplot as plt
import squarify

# Data transformation
data_labels = ['Research Funding (%)']
line_labels = ['Mathematics', 'Physics', 'Biology', 'Chemistry', 'Engineering',
               'Environmental Science', 'Biotechnology', 'Computer Science', 'Astronomy']
data = [15, 20, 20, 15, 10, 7, 5, 5, 3]

# Create a color palette
cmap = plt.cm.Spectral
mini = min(data)
maxi = max(data)
norm = plt.Normalize(vmin=mini, vmax=maxi)
colors = [cmap(norm(value)) for value in data]

# Create a figure with specified size to prevent content from being displayed improperly.
fig = plt.figure(figsize=(12, 8))

# Create a treemap with the given data, color palette, and labels.
squarify.plot(sizes=data, label=line_labels, color=colors, alpha=0.8,
              text_kwargs={'wrap': True, 'fontsize': 10, 'fontweight': 'bold'})

# Set the title of the figure
plt.title('Allocation of Research Funding Across Science and Engineering Disciplines')

# Resize the image using tight_layout before saving
plt.tight_layout()

# Save the figure to the specified path
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/1131.png', dpi=300)

# Clear the current figure state for any further plotting
plt.clf()
