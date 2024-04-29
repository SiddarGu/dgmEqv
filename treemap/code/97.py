import matplotlib.pyplot as plt
import squarify

# Given data
raw_data = """\
Manufacturing Sector,Production Volume (%)
Consumer Goods,25
Automotive,20
Electronics,15
Pharmaceuticals,13
Machinery,10
Chemicals,7
Food Production,5
Textiles,3
Aerospace,2
"""

# Parsing the raw data into the required format
lines = raw_data.strip().split('\n')
data_labels = lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in lines[1:]]
data = [float(line.split(',')[1]) for line in lines[1:]]

# Create a figure
fig = plt.figure(figsize=(12, 8))

# Treemap plotting
squarify.plot(sizes=data, label=line_labels, alpha=0.8, pad=True)

# Set the title of the figure
plt.title('Proportion of Production Volume by Manufacturing Sector')

# Improve layout to accommodate large text
plt.axis('off')
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/97.png'
plt.savefig(save_path, bbox_inches='tight', dpi=300)

# Clear the current image state
plt.clf()
