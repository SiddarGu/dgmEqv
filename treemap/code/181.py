import matplotlib.pyplot as plt
import squarify

# Given data
data_str = """Healthcare Category,Spending (%)
Hospital Care,38
Physician Services,22
Prescription Drugs,15
Dental Services,7
Nursing Home Care,6
Home Health Care,4
Medical Equipment,3
Other Services,5"""

# Split the string into lines and then split each line into a list
lines = data_str.split('\n')
data_labels = lines[0].split(',')[1:]

# Extract line_labels and data from the remaining lines
line_labels = []
data = []

for line in lines[1:]:
    parts = line.split(',')
    line_labels.append(parts[0])
    data.append(float(parts[1]))

# Plotting the treemap
plt.figure(figsize=(12, 8))
squarify.plot(sizes=data, label=line_labels, alpha=0.7)

# Add title and remove axes
plt.title('Healthcare Spending Distribution by Category')
plt.axis('off')

# Resize the figure to fit contents
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/181.png'
plt.savefig(save_path, format='png', dpi=300)

# Clear the current figure to prevent replotting of old data
plt.clf()
