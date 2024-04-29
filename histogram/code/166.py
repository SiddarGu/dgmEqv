import matplotlib.pyplot as plt

# Given data
data_labels = ['Average Annual Research Funding ($Million)']
line_labels = ['Mathematics', 'Biology', 'Computer Science', 'Physics', 
               'Social Sciences', 'Medicine', 'Engineering', 'Chemistry', 'Environmental Science']
data = [52.3, 150.7, 120.8, 95.6, 48.4, 200.5, 140.2, 110.9, 85.2]

# Create figure
plt.figure(figsize=(12, 8))
ax = plt.subplot()

# Plot horizontal bar chart
ax.barh(line_labels, data, color=plt.cm.tab10.colors)

# Set the title
ax.set_title('Average Annual Research Funding by Subject Area in Academia')

# Setting the grid
ax.grid(True, which='both', axis='x', linestyle='--', linewidth=0.7, alpha=0.7)

# Add data labels
for i in range(len(data)):
    ax.text(data[i], i, f'${data[i]:,.1f}M', va='center', ha='left')

# If the text length is too long, rotate the labels
ax.set_yticklabels(line_labels, rotation=45, ha='right', wrap=True)

# Automatically resize the image
plt.tight_layout()

# Save the image
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/166.png'
plt.savefig(save_path, bbox_inches='tight', dpi=300)

# Clear the current image state
plt.clf()
