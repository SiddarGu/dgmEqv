import matplotlib.pyplot as plt
import squarify

data_str = """Department,Workforce Distribution (%)
Administration,18
Sales,20
Marketing,15
Human Resources,12
Research and Development,10
IT Services,9
Customer Support,8
Finance,5
Production,3"""

# Preprocess the data
lines = data_str.split('\n')
data_labels = lines[0].split(',')[1:]  # The labels for data (column headers except the first one)
data = []
line_labels = []

# Extracting numerical data and the corresponding row labels
for line in lines[1:]:
    parts = line.split(',')
    line_labels.append(parts[0])  # The label of the row (Department names in this case)
    data.append(float(parts[1]))  # The numerical data as float (Workforce Distribution in this case)

# Now we create and save the treemap plot

# Use a larger figure size to prevent content being displayed incorrectly
fig = plt.figure(figsize=(12, 8))

# Create a treemap with custom sizes, labels, and colors
colors = plt.cm.Spectral([i / len(data) for i in range(len(data))])
squarify.plot(sizes=data, label=line_labels, color=colors, alpha=0.7)

# Set a title for the treemap
plt.title('Workforce Distribution Across Corporate Departments')

# Prevent content being cut off
plt.tight_layout()

# Save the image to the specified path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/172.png'
plt.savefig(save_path, bbox_inches='tight', dpi=300)

# Clear the current figure state to prevent reusing the same state for future plots
plt.clf()
