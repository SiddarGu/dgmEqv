
import matplotlib.pyplot as plt
import numpy as np

# Transform given data
data_labels = ["Mathematics", "Science", "English", "Social Studies", "Computer Science", "History", "Physical Education", "Music", "Art"]
data = [130, 110, 120, 90, 80, 60, 40, 10, 20]
line_labels = ["Subject", "Number of Students"]

# Create figure
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(1, 1, 1, projection="polar")

# Set up axes
ax.set_theta_direction(-1)
ax.set_theta_zero_location("N")

# Calculate sector angle
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Plot the data
for i in range(num_categories):
    ax.bar(i * sector_angle, data[i], width=sector_angle, label=data_labels[i], color=np.random.rand(3,))

# Set labels
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, wrap=True, fontsize=12)

# Position legend
ax.legend(bbox_to_anchor=(1.1, 1.1))

# Add title
plt.title("Number of Students Enrolled in Each Subject in 2021", fontsize=12)

# Resize the image by tight_layout()
plt.tight_layout()

# Save the image
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-054203_4.png")

# Clean up image state
plt.close()