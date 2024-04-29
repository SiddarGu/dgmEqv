import matplotlib.pyplot as plt
import squarify

# Data provided in CSV-like format
csv_data = """
Manufacturing Process,Percentage of Total Production (%)
Raw Material Acquisition,18
Component Fabrication,22
Assembly,25
Quality Control,15
Packaging,12
Warehousing,5
Distribution,3
"""

# Transform the CSV-like data to variables: data_labels, data, line_labels
lines = csv_data.strip().split('\n')
headers = lines[0].split(',')
data_labels = [headers[1]]
line_labels = [line.split(',')[0] for line in lines[1:]]
data = [float(line.split(',')[1]) for line in lines[1:]]

# Set up the figure size and style
plt.figure(figsize=(12,8), dpi=100)
cmap = plt.cm.viridis
mini=min(data)
maxi=max(data)
norm = plt.Normalize(vmin=mini, vmax=maxi)
colors = [cmap(norm(value)) for value in data]

# Create the treemap
squarify.plot(sizes=data, label=line_labels, color=colors, alpha=.7, text_kwargs={'fontsize':9, 'wrap': True})

# Add title
plt.title('Breakdown of Manufacturing and Production Processes by Percentage', fontsize=14)

# Remove axis lines
plt.axis('off')

# Resize the figure to fit all elements
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/1008.png'
plt.savefig(save_path, bbox_inches='tight')

# Clear the current figure's state to avoid any overlaps
plt.clf()
