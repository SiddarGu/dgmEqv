import matplotlib.pyplot as plt
import squarify

# Data given in the question
raw_data = """Production Area,Percentage of Total Output (%)
Automobile,22
Electronics,18
Pharmaceuticals,15
Machinery,14
Food and Beverage,10
Textiles,8
Chemicals,7
Aerospace,6"""

# Split the data into lines and then into pairs
lines = raw_data.strip().split('\n')
data_tuples = [line.split(',') for line in lines[1:]]  # skip the header

# Extract labels for sectors and their corresponding data values
line_labels = [item[0] for item in data_tuples]
data = [float(item[1]) for item in data_tuples]
data_labels = [f'{l} ({v}%)' for l, v in zip(line_labels, data)]

# Set up a large figure to prevent content from being cropped
plt.figure(figsize=(12, 8))

# Create a color palette
color_palette = plt.cm.tab20.colors  # using tab20 colormap for coloring

# Create the treemap
squarify.plot(sizes=data, label=data_labels, color=color_palette, alpha=0.7)

# Set the title of the figure
plt.title('Percentage of Manufacturing Output by Sector in 2023')

# Ensure content fits within the figure window
plt.tight_layout()

# Make sure text labels are easy to read and don't overlap
plt.rc('font', size=9)

# Set a larger figure size
plt.gcf().set_size_inches(16, 9)

# Save the plot to the specified file path
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/1012.png', format='png', dpi=300)

# Clear the current figure state after saving to free memory
plt.clf()
