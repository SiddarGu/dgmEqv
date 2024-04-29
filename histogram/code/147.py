import matplotlib.pyplot as plt
import seaborn as sns

# Data processing
data_labels = ['Exhibition Visitors (\'000)', 'Number of Exhibitions']
line_labels = ['0-50', '50-100', '100-150', '150-200', '200-250', '250-300', '300-350', '350-400', '400-450', '450-500']
data = [35, 27, 23, 19, 15, 12, 8, 5, 4, 1]

# Create the figure and axis
plt.figure(figsize=(10, 8))
ax = plt.subplot()

# Create a bar plot using seaborn
sns.barplot(x=line_labels, y=data, ax=ax)

# Set labels, title, and grid
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.set_title('Visitor Attendance at Art Exhibitions')
ax.grid(True)

# Rotate labels if they are too long
plt.xticks(rotation=45)

# Adjust layout
plt.tight_layout()

# Save the image
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/147.png'
plt.savefig(save_path)

# Clear the current figure state to avoid confusion with further plotting
plt.clf()
