import matplotlib.pyplot as plt
import squarify

# Transform data into three variables
# Data_labels
data_labels = ['Expenditure (%)']

# Line_labels
line_labels = ['Legislative', 'Judicial', 'Executive', 'Law Enforcement']

# Data
data = [25, 35, 15, 25]

# Set the size of the figure
plt.figure(figsize=(12, 8))

# Create a treemap
squarify.plot(sizes=data, label=line_labels, text_kwargs={'fontsize':10})

# Set title
plt.title('Allocation of Expenditure Across Legal Branches')

# Remove axis lines
plt.axis('off')

# Automatically adjust subplot params for a better layout
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/1102.png', format='png')

# Clear the current figure's state
plt.clf()
