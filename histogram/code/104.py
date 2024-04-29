import matplotlib.pyplot as plt

# Data
data_labels = ['Number of Students']
line_labels = ['Math', 'Science', 'Literature', 'History', 'Art', 'Music', 'Physical Education', 'Foreign Languages', 'Computer Science', 'Philosophy']
data = [70, 65, 60, 55, 50, 45, 40, 35, 30, 25]

# Create figure and subplot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)

# Horizontal bar plot
bar_positions = range(len(data))
ax.barh(bar_positions, data, color='skyblue')

# Set labels, title, and grid
ax.set_yticks(bar_positions)
ax.set_yticklabels(line_labels, rotation=0, fontsize=10)
ax.set_xlabel(data_labels[0])
ax.set_title('Weekly Student Engagement in Academic Subjects')

# Adding the grid
ax.grid(color='gray', linestyle='--', linewidth=0.5)

# Adjust layout to be more tight to prevent content from being displayed improperly
fig.tight_layout()

# Save figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/1007.png'
plt.savefig(save_path, format='png')

# Clear the current figure state
plt.clf()
