import matplotlib.pyplot as plt
import squarify

# Given data
data_labels = ['Donation Share (%)']
line_labels = ['Health Services', 'Educational Programs', 'Environmental Causes', 
               'Disaster Relief', 'Arts and Culture', 'Human Rights Advocacy', 
               'Animal Welfare', 'International Aid']
data = [25, 20, 15, 15, 10, 8, 4, 3]

# Plot
plt.figure(figsize=(12, 8))
colors = plt.cm.Spectral_r(range(len(data)))
squarify.plot(sizes=data, label=line_labels, color=colors, alpha=0.6)

plt.title('Allocation of Donations Among Charity and Nonprofit Sectors')
plt.axis('off')  # Remove the axes

# Automatically resize the image
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/137.png'
plt.savefig(save_path, format='png')

# Clear the current image state
plt.clf()
