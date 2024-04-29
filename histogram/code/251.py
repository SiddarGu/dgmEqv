import matplotlib.pyplot as plt

# Data and labels
data_labels = ['Yield (tonnes per hectare)']
line_labels = ['Cereals', 'Vegetables', 'Fruits', 'Legumes', 'Tubers', 'Nuts']
data = [3.2, 12.6, 8.4, 2.8, 17.5, 1.1]

# Create figure and axis objects
plt.figure(figsize=(10, 6))
ax = plt.subplot()

# Create horizontal bar chart
ax.barh(line_labels, data, color=['skyblue', 'green', 'red', 'yellow', 'purple', 'orange'])

# Adding grid
ax.grid(True, linestyle='--', which='major', color='grey', alpha=.25)

# Rotate labels if they're too long and wrap
ax.set_yticklabels(line_labels, rotation=45, wrap=True)

# Automatic resizing before saving
plt.tight_layout()

# Add title
plt.title('Average Yield per Hectare by Crop Type in Agriculture Sector')

# Saving the file
save_path = '/cpfs01/user/liuqi/workspace/plotchart/demo/histogram/png/601.png'
plt.savefig(save_path, format='png', dpi=300)

# Clear the current figure state
plt.clf()
