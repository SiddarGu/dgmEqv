import matplotlib.pyplot as plt

# Given Data
data_labels = ['Households (Millions)']
line_labels = ['Fiber Optic', 'Cable', 'DSL', 'Satellite', 'Fixed Wireless', 'Mobile Wireless']
data = [38.2, 62.5, 15.1, 4.8, 24.7, 56.3]

# Create a figure
plt.figure(figsize=(10, 6)) # The figsize is set larger to prevent content from being displayed poorly.

# Create a horizontal bar plot
ax = plt.subplot(111)
bars = ax.barh(line_labels, data, color=plt.cm.tab20.colors, edgecolor='black')

# Adding the data values on top of the bars
for bar in bars:
    width = bar.get_width()
    label_x_pos = width + 1 # make sure the label is slightly right from the bar end.
    ax.text(label_x_pos, bar.get_y() + bar.get_height()/2, f'{width}', va='center')

# Setting the title of the figure
plt.title('Household Internet Connection Types Distributio')

# Add grid lines in the background
plt.grid(True, linestyle='--', alpha=0.7)

# If the text length of the label is too long, use rotation
plt.yticks(rotation=30)

# Automatically adjust the layout
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/28.png', format='png')

# Clear the current figure state to prevent data from previous plots from displaying in future plots
plt.clf()
