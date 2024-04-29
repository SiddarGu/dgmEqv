
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ["Federal Government", "Local Government", "City Planning", "Public Education", "Public Safety", "Social Services", "Public Health", "Transportation"]
data = [17, 25, 14, 30, 45, 60, 75, 90]
line_labels = ["Category", "Number"]

# Plot the data with the type of rose chart
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='polar')

# Calculate sector angle
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Draw sectors corresponding to different categories
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'purple']
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, color = colors[i], label=data_labels[i])
    
# Set the ticks and labels
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels)

# Add legend
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1))

# Add title
plt.title("Number of Government Agencies and Programs by Category in 2021")

# Automatically resize the image 
plt.tight_layout()

# Save the image
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_144.png")

# Clear the current image state
plt.clf()