import matplotlib.pyplot as plt

# Data transformation
data_labels = ['National Defense', 'Healthcare', 'Education',
               'Infrastructure', 'Science and Technology', 'Energy', 'Agriculture', 'Transportation']
line_labels = ['Budget Allocation ($ Billion)']
data = [120.5, 59.7, 51.3, 45.6, 34.2, 28.9, 20.3, 15.7]

# Plot setup
plt.figure(figsize=(10, 8))
ax = plt.subplot()

# Create vertical histogram
ax.bar(data_labels, data, color=plt.cm.tab20c.colors)

# Set title and axes labels
ax.set_title('U.S. Federal Budget Allocation by Department (Fiscal Year 2023)')
ax.set_xlabel('Government Department')
ax.set_ylabel('Budget Allocation ($ Billion)')

# Set the rotation of the x-axis labels to 45 degrees for better readability
plt.xticks(rotation=45, ha='right')

# Apply grid to the background 
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Automatically resize the image and apply tight layout
plt.tight_layout()

# Saving to the absolute path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/94.png'
plt.savefig(save_path, dpi=300)

# Clear the current figure state to prevent overlapping of figures
plt.clf()
