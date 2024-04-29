
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels.
data_labels = ["Mathematics", "English", "History", "Science", "Arts", "Physical Education", "Technology", "Foreign Language"]
data = [800, 1000, 800, 900, 500, 300, 200, 100]
line_labels = ["Course", "Number of Students"]

# Create figure before plotting
fig = plt.figure(figsize=(16, 12))
ax = fig.add_subplot(111, projection='polar')

# Plot the data with the type of rose chart
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Loop to assign a label to each sector
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i])

# Add legend
ax.legend(data_labels, bbox_to_anchor=(0.6, 0.9))

# Set labels
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=12)
ax.set_title("Number of Students Enrolled in Each Course in 2021", fontsize=20)

# Make sure the legend does not overlap with the chart
plt.tight_layout()

# Save the chart
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-070122_72.png')

# Clear the current image state
plt.cla()