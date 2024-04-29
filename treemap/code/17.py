import matplotlib.pyplot as plt
import squarify

# Given data
data_str = """Product Category,Online Sales (%)
Electronics,25
Apparel,22
Home Furnishings,17
Health & Beauty,13
Food & Beverage,10
Books & Media,8
Toys & Games,5"""

# Extracting line labels and data
lines = data_str.split('\n')
data_labels = lines[0].split(',')[1:]  # Extract column labels
line_labels = [line.split(',')[0] for line in lines[1:]]  # Extract row labels
data = [float(line.split(',')[1]) for line in lines[1:]]  # Extract numerical data

# Treemap plot
plt.figure(figsize=(10, 8))  # Set figure size
squarify.plot(sizes=data, label=line_labels, alpha=0.7)  # Draw treemap

# Additional style configurations
plt.title('E-commerce Sales Distribution by Product Category', fontsize=16)
plt.axis('off')  # Turn off the axis

# Prevent content from being crowded
plt.tight_layout()

# Save the figure to the specified path
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/17.png', format='png')

# Clear the current figure state to avoid overlap in case of further plotting
plt.clf()
