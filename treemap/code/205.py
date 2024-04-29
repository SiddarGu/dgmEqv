import matplotlib.pyplot as plt
import squarify

# Data provided in the format: Legal Branch,Expenditure (%)
data_str = """Legislative,25
Judicial,35
Executive,15
Law Enforcement,25"""

# Parsing the data into appropriate variables
data_labels = ["Expenditure (%)"]
line_labels = []
data = []

for line in data_str.split('\n'):
    parts = line.split(',')
    line_labels.append(parts[0])
    data.append(int(parts[1]))

# Set the size of the figure to accommodate the treemap
fig = plt.figure(figsize=(12, 8))

# Create a treemap
squarify.plot(sizes=data, label=line_labels, alpha=0.7)

plt.title('Allocation of Expenditure Across Legal Branches', fontsize=18)
plt.axis('off')

# Use tight_layout to automatically adjust the size
plt.tight_layout()

# The absolute save path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/1101.png'

# Save the figure
plt.savefig(save_path, format='png', bbox_inches='tight')

# Clear the current figure state to avoid overlap with subsequent plots
plt.clf()

print(f'Treemap has been saved to {save_path}')
