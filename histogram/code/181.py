import matplotlib.pyplot as plt
import os

# Given data
data_labels = ["Number of Concerts"]
line_labels = ["0-50", "50-100", "100-150", "150-200", "200-250",
               "250-300", "300-350", "350-400", "400-450", "450-500"]
data = [40, 55, 60, 45, 35, 20, 10, 5, 3, 2]

# Set the path for the output.
output_path = "/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/1003.png"

# Create figure and add subplot
fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(line_labels, data, color=plt.cm.Paired.colors, edgecolor='black')

# Title and labels
ax.set_title('Ticket Price Distribution for Live Entertainment Events', fontsize=15)
ax.set_xlabel('Ticket Price Range ($)', fontsize=12)
ax.set_ylabel('Number of Concerts', fontsize=12)

# Rotate the x labels if they are too long
plt.xticks(rotation=45, ha='right')

# Add grid for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Force layout to be tight
plt.tight_layout()

# Save the figure and clear the plot
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path)
plt.clf()
