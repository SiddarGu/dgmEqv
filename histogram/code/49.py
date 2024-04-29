import matplotlib.pyplot as plt
import seaborn as sns

# Data
data_labels = ['0-25', '25-50', '50-75', '75-100', '100-150', '150-200', '200-250']
data = [30, 45, 50, 40, 20, 15, 10]

# Create a figure and a single subplot
plt.figure(figsize=(10, 8))
ax = plt.subplot(1, 1, 1)

# Create the histogram
sns.barplot(x=data_labels, y=data, palette='viridis')

# Set title and labels
ax.set_title('Price Distribution for Tickets at Sporting Events')
ax.set_xlabel('Ticket Price Range ($)')
ax.set_ylabel('Number of Sporting Events')

# Improve layout to accommodate long labels
plt.xticks(rotation=45)  # Rotate the x labels to avoid overlapping

plt.grid(True, linestyle='--', alpha=0.7)  # Add grid with style

plt.tight_layout()  # Automatically adjust subplot params to fit the figure area.

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/49.png', format='png')

# Clear the current figure state to prevent overlap with future plots
plt.clf()
