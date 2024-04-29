import matplotlib.pyplot as plt
import squarify

# Given data
data_labels = ['Criminal Justice', 'Contract Law', 'Public Interest Law', 'Property Law',
               'Immigration Law', 'Healthcare Law', 'Antitrust Law', 'Securities Law', 'Maritime Law']
line_labels = ['Percentage (%)']
data = [25, 15, 13, 12, 10, 9, 8, 5, 3]

# Create a color palette
color_palette = plt.cm.Spectral_r(range(len(data)))

# Create a treemap
plt.figure(figsize=(12, 8))
squarify.plot(sizes=data, label=data_labels, color=color_palette, alpha=0.7, pad=True)
plt.axis('off')

# Title setup
plt.title('Proportional Focus within the Sphere of Law and Legal Affairs', fontsize=18)

# Resize the figure
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/30.png', format='png', bbox_inches='tight')

# Clear the current figure state
plt.clf()
