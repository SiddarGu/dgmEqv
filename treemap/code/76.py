import matplotlib.pyplot as plt
import squarify

# Given data
data_labels = ['Sustainability Effort (%)']
line_labels = [
    'Renewable Energy',
    'Pollution Reduction',
    'Resource Management',
    'Biodiversity Conservation',
    'Sustainable Agriculture',
    'Waste Management',
    'Climate Change Mitigation'
]
data = [40, 20, 15, 10, 8, 5, 2]

# Setup the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Create a treemap
squarify.plot(sizes=data, label=line_labels, color=None, alpha=0.8, text_kwargs={'fontsize':9, 'wrap':True})

# Set the title of the figure
plt.title('Proportional Efforts in Environment and Sustainability Initiatives')

# Remove the axes
plt.axis('off')

# Resize the plot
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/chart_simulation_final/treemap/png/76.png'
plt.savefig(save_path, format="png", dpi=300)

# Clear the current figure after saving to prevent reuse
plt.clf()
