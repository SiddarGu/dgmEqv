import matplotlib.pyplot as plt
import squarify

# Given data
data_str = """Administration,15
Sales,20
Marketing,17
Human Resources,8
Research and Development,12
Customer Service,13
IT Support,10
Production,5"""

# Parse data into lists
data_rows = data_str.strip().split('\n')
line_labels = [row.split(',')[0] for row in data_rows]
data_values = [int(row.split(',')[1]) for row in data_rows]

# Create sizes for the treemap
sizes = data_values

# Choose a color palette for the treemap
colors = plt.cm.tab20c.colors
custom_colors = colors[:len(data_values)]

# Create the treemap
plt.figure(figsize=(16, 9))
squarify.plot(sizes=sizes, label=line_labels, color=custom_colors, alpha=0.8)

# Set the properties of the plot
plt.title('Workforce Distribution Across Departments in an Organization')
plt.axis('off')

# Ensure everything is fitted and save the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/1200.png', dpi=300)

# Clear the current figure's state
plt.clf()
