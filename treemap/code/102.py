import matplotlib.pyplot as plt
import squarify

# Given data in a CSV-like format, parsing it into variables
csv_data = """
Crop Type,Production Share (%)
Cereals,30
Vegetables,25
Fruits,20
Dairy,10
Meat,10
Fisheries,3
Poultry,2
"""

# Parse the CSV-like data
lines = csv_data.strip().split('\n')
data_labels = lines[0].split(',')[1:]
line_labels = []
data = []

# Process each row in the CSV-like data
for line in lines[1:]:
    parts = line.split(',')
    line_labels.append(parts[0])
    data.append(float(parts[1]))

# Plotting the treemap
plt.figure(figsize=(12, 8))
squarify.plot(sizes=data, label=line_labels, alpha=0.7)

# Customizations
plt.title('Percentage Share of Global Food Production by Crop Type')
plt.axis('off')  # Disable the axis

# Automatically resize the image and save it to the given path
plt.tight_layout()
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/102.png'
plt.savefig(save_path, format='png', dpi=300)

# Clear the current image state
plt.clf()
