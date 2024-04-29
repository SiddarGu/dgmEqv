import matplotlib.pyplot as plt

# Given data
data_labels = ["Housing Price Range (Thousands)", "Number of Houses Sold"]
line_labels = ["100-200", "200-300", "300-400", "400-500", "500-600", "600-700", "700-800", "800-900", "900-1000"]
data = [30, 45, 60, 50, 40, 20, 10, 5, 2]

# Setting up the figure and axis
plt.figure(figsize=(12, 8))
ax = plt.subplot()

# Creating the horizontal bar chart
ax.barh(line_labels, data, color='#1f77b4', edgecolor='black')

# Adding grid, title and labels
plt.title('Trends in Housing Sales Across Price Ranges')
ax.set_xlabel(data_labels[1])
ax.set_ylabel(data_labels[0])

# Rotate x-ticks labels if necessary
plt.xticks(rotation=45, ha='right')
plt.yticks(wrap=True)

# Adjust layout to fit everything and prevent content from being displayed too densely
plt.tight_layout()

# Saving the figure to the specified path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/236.png'
plt.savefig(save_path)

# Clear the current figure after saving to prevent replotting on the same figure
plt.clf()
