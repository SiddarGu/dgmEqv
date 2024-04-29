import matplotlib.pyplot as plt
import seaborn as sns

# Define the data
data_labels = ['Government Budget (Billion $)', 'Number of Departments']
line_labels = ['0-50', '50-100', '100-150', '150-200', '200-250', '250-300', '300-350', '350-400', '400-450', '450-500']
data = [20, 15, 12, 10, 8, 6, 5, 3, 2, 1]

# Create a figure
plt.figure(figsize=(12, 8))
ax = plt.subplot()

# Use seaborn to create a vertical bar plot
sns.barplot(x=line_labels, y=data, palette='viridis', ax=ax)

# Set the title
ax.set_title('Allocation of Government Budget Across Departments')

# Set the label for the x-axis to display vertically
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', wrap=True)

# Setting the axes labels
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

# Adjust layout to make sure everything fits without overlapping
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/45.png')

# Clear the current figure state
plt.clf()
