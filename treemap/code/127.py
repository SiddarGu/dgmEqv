import matplotlib.pyplot as plt
import squarify

# Given data in a raw string format
raw_data = """
Product Category,Sales Share (%)
Electronics,25
Clothing,20
Home & Garden,15
Health & Beauty,13
Food & Beverage,12
Books & Media,7
Toys & Games,4
Sports Equipment,4
"""

# Processing the raw data to extract line_labels, data_labels, and data
# Splitting the string by lines and then by commas
lines = raw_data.strip().split('\n')
data_labels = lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in lines[1:]]
data = [float(line.split(',')[1]) for line in lines[1:]]

# Define colors for each category - optional for fanciness
colors = plt.cm.tab20c.colors

# Create a figure with larger size for better readability
plt.figure(figsize=(16, 9))

# Create a treemap using squarify
squarify.plot(sizes=data, label=line_labels, color=colors[:len(line_labels)], alpha=0.8)

# Add the title to the plot
plt.title('Retail and E-commerce Sales Distribution by Product Category')

# Prevent content from being cut off and resize image with tight_layout
plt.tight_layout()

# Save the image to the specified path, remembering to check for overwriting
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/127.png'
plt.savefig(save_path, format='png')

# Clear the current image state
plt.clf()
