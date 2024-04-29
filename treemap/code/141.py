import matplotlib.pyplot as plt
import squarify

# Given data
raw_data = """
Category,Sales Percentage (%)
Clothing and Apparel,25
Electronics,20
Home & Garden,15
Health & Beauty,10
Sports & Outdoors,10
Toys & Hobbies,5
Food & Beverage,5
Books & Media,5
Automotive,3
Jewelry,2
"""

# Parsing the data
lines = raw_data.strip().split('\n')
data_labels = lines[0].split(',')[1:]  # Extract headers except for the first column
line_labels = [line.split(',')[0] for line in lines[1:]]  # Extract first column for labels
data = [float(line.split(',')[1]) for line in lines[1:]]  # Extract numerical data

# Create figure and axes
fig, ax = plt.subplots(figsize=(12, 8))

# Create a treemap
squarify.plot(sizes=data, label=line_labels, alpha=.8, text_kwargs={'fontsize':9, 'wrap':True})

# Remove the axes
plt.axis('off')

# Title of the figure
plt.title('Retail and E-commerce Sales Distribution by Category', fontsize=16, fontweight='bold')

# Adjust layout to prevent content from being cropped
plt.tight_layout()

# Save figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/141.png'
plt.savefig(save_path, format='png', bbox_inches='tight', dpi=300)

# Clear the current figure state to prevent overlap
plt.clf()
