import matplotlib.pyplot as plt
import squarify

# Creating data variables from the input data
data_labels = ['Aerospace', 'Biotechnology', 'Computer Science', 'Environmental Science', 
               'Mechanical Engineering', 'Chemical Engineering', 'Electrical Engineering', 'Civil Engineering']
data = [18, 17, 15, 14, 12, 10, 8, 6]
line_labels = ['Research Funding (%)']

# Drawing the treemap
plt.figure(figsize=(12, 8))
squarify.plot(sizes=data, label=data_labels, alpha=0.7)

# Formatting labels
plt.title('Allocation of Research Funding Across Science and Engineering Fields in 2023')
plt.axis('off')

# Optimize figure layout to prevent content from being cut off
plt.tight_layout()

# Saving the image to the specified path
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/74.png', format='png', dpi=300)

# Clear the current figure state after plotting
plt.clf()
