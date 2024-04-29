import matplotlib.pyplot as plt
import textwrap

# Data provided
data_labels = ['Visual Arts Visitors (Thousands)', 'Exhibit Count']
line_labels = ['Painting', 'Sculpture', 'Photography', 'Digital Art', 'Mixed Media', 'Ceramics']
data = [75, 60, 82, 58, 50, 47]

# Create figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

# Plot
ax.bar(line_labels, data, color=plt.cm.Paired(range(len(data))))

# Set the title
ax.set_title('Exhibit Attendance in the Visual Arts Sector')

# Label the axes
ax.set_xlabel(data_labels[1])
ax.set_ylabel(data_labels[0])

# Add grid
ax.yaxis.grid(True)

# Rotate x-axis labels if too long
ax.set_xticklabels([textwrap.fill(label, 10) for label in line_labels], rotation=45, ha='right')

# Layout and save
plt.tight_layout()
save_path = '/cpfs01/user/liuqi/workspace/plotchart/demo/histogram/png/616.png'
plt.savefig(save_path)

# Clear the current image state
plt.clf()
