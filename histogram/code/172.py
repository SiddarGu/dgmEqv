import matplotlib.pyplot as plt
import seaborn as sns

# Define the data
data_labels = ['Number of Employees']
line_labels = ['Very Unsatisfied', 'Unsatisfied', 'Neutral', 'Satisfied', 'Very Satisfied']
data = [75, 125, 300, 450, 250]

# Initialize the figure with a larger figure size
plt.figure(figsize=(10, 8))
ax = plt.subplot()

# Create a horizontal bar plot using seaborn
sns.barplot(x=data, y=line_labels, palette="viridis", ax=ax)

# Set the title of the figure
ax.set_title('Employee Job Satisfaction Levels across the Corporation')

# If the text length of the label is too long, rotate the labels
plt.xticks(rotation=45)

# Improve layout to prevent content cutoffs
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/172.png'
plt.savefig(save_path, format='png')

# Clear current figure's state
plt.clf()
