import matplotlib.pyplot as plt
import squarify

# Given data in text format
data_str = """Crop Type,Production Volume (%)
Cereals,30
Vegetables,25
Fruits,20
Livestock,15
Dairy,10"""

# Parsing the given data
lines = data_str.strip().split('\n')
data_labels = lines[0].split(',')[1:]  # ["Production Volume (%)"]
line_labels = [line.split(',')[0] for line in lines[1:]]  # ['Cereals', 'Vegetables', 'Fruits', 'Livestock', 'Dairy']
data = [float(line.split(',')[1]) for line in lines[1:]]  # [30.0, 25.0, 20.0, 15.0, 10.0]

# Creating the treemap
plt.figure(figsize=(12, 8))
colors = plt.cm.tab20c.colors
squarify.plot(sizes=data, label=line_labels, color=colors, alpha=0.7)

# Adding title and removing axis
plt.title('Percentage Share of Agriculture Production by Crop Type in 2023')
plt.axis('off')

# Automatically resize the image before saving
plt.tight_layout()

# Save the figure to the specified path
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/233.png', format='png', bbox_inches='tight')

# Clear the current figure's state
plt.close()
