import matplotlib.pyplot as plt

# Transforming given data into three variables: data_labels, data, line_labels.
data_labels = ["0-10", "10-25", "25-40", "40-55", "55-70", "70-85", "85-100"]
data = [16, 21, 19, 13, 9, 5, 3]
line_labels = ["Number of Art Exhibits"]

# Create a figure and a horizontal barplot
plt.figure(figsize=(12, 8))
ax = plt.subplot()

# Plotting the data
ax.barh(data_labels, data, color=plt.cm.Paired.colors, edgecolor='black')

# Adding grid background
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Set the title of the figure
plt.title('Visitor Attendance Range at Art Exhibits')

# If the text length of the label is too long, use rotation
# plt.xticks(rotation=45, ha='right') # Not required as we are plotting a horizontal histogram

# Automatically resize the image
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/248.png'
plt.savefig(save_path, format='png')

# Clear the current image state
plt.clf()
