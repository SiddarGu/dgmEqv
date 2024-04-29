import matplotlib.pyplot as plt
import squarify

# Given data
data_labels = ['Recruitment', 'Training and Development', 'Compensation and Benefits', 
               'Workplace Safety', 'Employee Relations', 'Performance Management', 
               'Diversity and Inclusion', 'HR Technology']
data = [20, 18, 15, 5, 15, 10, 10, 7]
line_labels = ['Percentage (%)']

# Set up figure size
plt.figure(figsize=(12, 8))

# Choose color palette
colors = plt.cm.Paired(range(len(data)))

# Create a treemap
squarify.plot(sizes=data, label=data_labels, color=colors, alpha=0.7, pad=True)

# Add title and format it
plt.title('Human Resources Management: Key Focus Areas and Their Allocations', fontsize=16)

# Resize the image to fit the content
plt.tight_layout()

# Save the figure with an absolute path
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/demo/treemap/png/1037.png', format='png')

# Clear the image state
plt.close()
