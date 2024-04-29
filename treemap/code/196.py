import matplotlib.pyplot as plt
import squarify

# Extracting the data into the required variables
data_labels = ['Research Funding (%)']
line_labels = ['Biotechnology', 'Aerospace Engineering', 'Renewable Energy', 'Medical Research', 'Robotics', 'Materials Science', 'Information Technology', 'Environmental Science']
data = [22, 18, 16, 14, 12, 10, 5, 3]

# Choose a color palette
cmap = plt.cm.get_cmap('Spectral')
mini=min(data)
maxi=max(data)
colors = [cmap((i-mini)/(maxi-mini)) for i in data]

# Create a figure and a treemap
fig = plt.figure(figsize=(12, 8))
axes = fig.add_subplot(1, 1, 1)

# Plotting the treemap with label adjustments for better readability
squarify.plot(sizes=data, label=line_labels, color=colors, alpha=0.7, text_kwargs={'wrap': True})

# Set the title of the figure
plt.title('Allocation of Research Funding in Science and Engineering Fields', fontsize=18)

# Removing axis for a cleaner look
plt.axis('off')

# Ensure content is well displayed
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/196.png'
plt.savefig(save_path, format='png', dpi=300, bbox_inches='tight')

# Clear the current image state
plt.clf()
