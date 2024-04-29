import matplotlib.pyplot as plt
import os

# Given data processed into three variables
data_labels = ['<1', '1-2', '2-3', '3-4', '4-5', '5-6', '6-7', '7-8', '8-9', '9+']
data = [8.2, 32.5, 58.7, 44.1, 21.3, 12.5, 7.8, 3.9, 1.5, 0.8]
line_labels = ['Average Daily Hours Spent Online', 'Number of Individuals (Millions)']

# Create a figure object with a larger figsize
plt.figure(figsize=(12, 8))

# Add a subplot for a horizontal histogram
ax = plt.subplot(111)

# Creating the horizontal histogram
ax.barh(data_labels, data, color='skyblue', edgecolor='black')

# Setting the title of the histogram
plt.title('Online Activity: Average Time Spent on the Internet Per Day')

# Labelling the x and y axes
plt.xlabel(line_labels[1])
plt.ylabel(line_labels[0])

# Adding grid for better readability
plt.grid(axis='x', linestyle='--', alpha=0.7)

# If the text length in the data_labels is too long, rotate
plt.xticks(rotation=45)

# Adjust layout to prevent content from being cut off
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/101.png'
os.makedirs(os.path.dirname(save_path), exist_ok=True)
plt.savefig(save_path)

# Clear the current image state after saving the figure
plt.clf()
