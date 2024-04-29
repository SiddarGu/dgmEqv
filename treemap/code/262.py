import matplotlib.pyplot as plt
import squarify

# Data preparation
raw_data = """Property Type,Market Share (%)
Single-Family Home,35
Condominium,20
Townhouse,15
Multi-Family (2-4 units),10
High-Rise Apartment,7
Manufactured Home,5
Vacation Home,5
Co-op,3"""

# Parsing the raw data
lines = raw_data.split('\n')
data_labels = lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in lines[1:]]
data = [float(line.split(',')[1]) for line in lines[1:]]

# Create a figure for the treemap
plt.figure(figsize=(12, 8))
colors = plt.cm.Spectral_r([0.2 + 0.6 * (i/max(data)) for i in data])

# Create a treemap
squarify.plot(sizes=data, label=line_labels, color=colors, alpha=0.8, text_kwargs={'wrap':True})

# Set the title and adjust the image size
plt.title('Market Share of Property Types in the Housing Market')

# Eliminate the axes
plt.axis('off')

# Adjust layout
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/demo/treemap/png/1012.png', bbox_inches='tight')

# Clear the current figure state for future plots
plt.clf()
