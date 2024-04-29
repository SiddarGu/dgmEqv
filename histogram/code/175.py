import matplotlib.pyplot as plt

# Extracting variables from the provided data
data_labels = ['Number of Visitors (in thousands)']
line_labels = ['Paintings', 'Sculptures', 'Installations', 'Photographs', 'Digital Art', 'Classical Antiquities', 'Modern Art', 'Performance Art']
data = [150, 95, 70, 85, 60, 80, 130, 50]

# Creating the figure and the horizontal histogram
fig, ax = plt.subplots(figsize=(10, 8))
ax.barh(line_labels, data, color=plt.cm.viridis(range(len(data))))

# Styling the chart to make it more intuitive and fancy
ax.set_xlabel(data_labels[0])
ax.set_title('Visitor Engagement with Different Types of Art Exhibits')
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Rotating and wrapping the labels if they are too long
ax.set_yticklabels(line_labels, rotation=45, wrap=True)

# Automatically adjusting subplot params so that the subplot(s) fits in to the figure area
plt.tight_layout()

# Saving the figure to the absolute path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/175.png'
plt.savefig(save_path, format='png')

# Clear the current figure state to avoid overlaps on subsequent plots
plt.clf()
