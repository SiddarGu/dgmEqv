import matplotlib.pyplot as plt
import squarify

# Given data transformation
data_labels = ['Funding Allocation (%)']
line_labels = ['Health', 'Education', 'Environment', 'Social Services', 'Arts & Culture', 'International Aid', 'Animal Welfare', 'Research & Advocacy']
data = [25, 20, 15, 15, 10, 10, 3, 2]

# Plotting the treemap
plt.figure(figsize=(12, 8))
colors = plt.cm.viridis(range(len(line_labels)))
squarify.plot(sizes=data, label=line_labels, color=colors, alpha=0.8, text_kwargs={'fontsize':9, 'wrap':True})

# Customizations
plt.title('Funding Distribution Across Nonprofit Sectors in 2023', fontsize=13)
plt.axis('off')  # Turn off the axis

# Automatically resize the image before saving
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/194.png'
plt.savefig(save_path, format='png')

# Clear the current figure state
plt.clf()
