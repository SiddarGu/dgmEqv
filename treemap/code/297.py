import matplotlib.pyplot as plt
import squarify

# Data provided in a formatted string
data_str = """Housing Segment,Market Share (%)
Single-Family Homes,35
Apartments,25
Condominiums,15
Townhouses,10
Manufactured Homes,5
Luxury Properties,5
Vacation Homes,3
Rental Properties,2"""

# Splitting the data into lines and then into labels and values
lines = data_str.split('\n')
data_labels = lines[0].split(',')[1:]
line_labels = []
data = []

for line in lines[1:]:
    parts = line.split(',')
    line_labels.append(parts[0])
    data.append(float(parts[1]))

# Plotting the treemap
plt.figure(figsize=(12, 8))
squarify.plot(sizes=data, label=line_labels, alpha=0.8)
plt.title('Market Share Distribution Across Housing Segments')

# Adjusting the plot parameters to ensure clarity and no text overlap
plt.axis('off')
plt.tight_layout()

# Save the figure to the specified absolute path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/demo/treemap/png/1047.png'
plt.savefig(save_path, format='png', bbox_inches='tight')

# Clear the current figure's state to prevent any overlap on next plots
plt.clf()
