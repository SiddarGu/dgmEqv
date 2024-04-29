import matplotlib.pyplot as plt

# Data provided
data = [
    [3500, 5700, 4300, 9300, 7100, 5700, 2800, 1300]
]

data_labels = ['No Formal Education', 'Elementary', 'Middle School', 'High School', 
               'Some College', 'Bachelor\'s Degree', 'Master\'s Degree', 
               'Doctorate or Professional Degree']

line_labels = ['Number of Individuals (Thousands)']

# Create a figure with a subplot and set the size to ensure content is displayed properly.
plt.figure(figsize=(14, 8))
ax = plt.subplot(111)

# Drawing the vertical bar chart
for i in range(len(data)):
    ax.bar(data_labels, data[i], label=line_labels[i])

# Adding grid
ax.yaxis.grid(True)

# Add title to the chart
ax.set_title('Educational Attainment of the Adult Population')

# Set x-axis labels to prevent overlapping and ensure they show completely
ax.set_xticklabels(data_labels, rotation=45, ha='right', rotation_mode='anchor', wrap=True)

# Apply tight_layout to automatically adjust subplot params
plt.tight_layout()

# Saving the figure to the given path
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/82.png')

# Clear the current state
plt.clf()
