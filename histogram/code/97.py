import matplotlib.pyplot as plt
import os

# Given data transformation into variables
data_labels = ['0-50', '50-100', '100-150', '150-200', '200-250', '250-300', '300-350', '350-400', '400-450', '450-500']
data = [80, 120, 60, 45, 20, 10, 5, 3, 2, 1]

# Setting up the figure and axes
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot()

# Creating a horizontal bar plot 
ax.barh(data_labels, data, color=plt.cm.tab20b.colors)

# Customizing the plot
ax.set_title('Ticket Price Distribution for Sporting Events')
ax.set_xlabel('Number of Sporting Events')
ax.set_ylabel('Ticket Price Range ($)')

# Adding grid lines and layout settings
ax.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/97.png'
os.makedirs(os.path.dirname(save_path), exist_ok=True)
fig.savefig(save_path, format='png', bbox_inches='tight')

# Clear the current figure's state
plt.clf()
