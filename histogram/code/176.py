import matplotlib.pyplot as plt

# Given data
data_labels = ["0-1", "1-2", "2-3", "3-4", "4-5", "5-6", "6-7", "7-8", "8-9", "9-10"]
data = [85, 75, 60, 50, 45, 35, 30, 20, 15, 10]
line_labels = ["Research Funding ($Billion)", "Number of Projects"]

# Set up the figure size
plt.figure(figsize=(12, 6))

# Add a subplot
ax = plt.subplot()

# Create histogram
ax.bar(data_labels, data, color='skyblue')

# Set title
ax.set_title('Distribution of Research Funding for Science and Engineering Projects')

# Set the labels
ax.set_xlabel(line_labels[0])
ax.set_ylabel(line_labels[1])

# Rotate the x-axis labels if they're too long
ax.set_xticklabels(data_labels, rotation=45)

# Add background grid
ax.grid(True)

# Automatically adjust subplot params to give specified padding
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/176.png'
plt.savefig(save_path, format='png')

# Clear the current figure after saving
plt.clf()
