import matplotlib.pyplot as plt
import squarify

# Given data in a text block
data_text = """Category,Market Share (%)
Banking,25
Insurance,20
Investments,22
Real Estate,15
Financial Tech,10
Retail Banking,5
Corporate Finance,3"""

# Process the given data into three variables
data_lines = data_text.strip().split('\n')
data_labels = data_lines[0].split(',')[1:]  # Ignore the first element 'Category'
line_labels = [line.split(',')[0] for line in data_lines[1:]]
data_values = [float(line.split(',')[1]) for line in data_lines[1:]]

# Create the treemap
plt.figure(figsize=(12, 8))
squarify.plot(sizes=data_values, label=line_labels, alpha=.7)

# Set the title and customize
plt.title('Market Share Distribution in the Finance Sector', fontsize=18)

# Ensure all characters show and are not overwritten
plt.tick_params(labelsize=10)
plt.xticks(rotation=45, ha='right')
plt.gca().invert_yaxis()  # Labels will be displayed from top to bottom
plt.axis('off')  # Hide the axes

# Use tight layout to automatically adjust subplot params
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/108.png'
plt.savefig(save_path, format='png', bbox_inches='tight')

# Clear the current figure state
plt.clf()
