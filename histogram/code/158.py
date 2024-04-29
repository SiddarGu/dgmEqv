import matplotlib.pyplot as plt
import os

# Given data
data_labels = ['Highly Engaged', 'Engaged', 'Moderately Engaged', 'Barely Engaged', 'Disengaged', 'Highly Disengaged']
data = [320, 480, 150, 95, 45, 10]
line_labels = ['Number of Employees']  # Assuming only one line_label as per the given data structure

# Set the size of the figure
plt.figure(figsize=(10, 8))

# Add a subplot
ax = plt.subplot()

# Create a histogram
ax.bar(data_labels, data, color='skyblue', edgecolor='black')

# Add title and labels
plt.title('Employee Engagement Levels Across the Organization')
plt.xlabel('Engagement Level')
plt.ylabel('Number of Employees')

# Customize labels to prevent overlap
plt.xticks(rotation=30, ha='right')  # Rotate the x labels for better readability
plt.yticks()

# Add grid to the background
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Auto-adjust layout to ensure the content fits well and is clear
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/158.png'
os.makedirs(os.path.dirname(save_path), exist_ok=True)  # Ensure the directory exists
plt.savefig(save_path)

# Clear the current image state
plt.clf()
