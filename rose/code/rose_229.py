
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels. 
data_labels = ["Math", "English", "Science", "History", "Art", "Physical Education", "Music", "Foreign Language", "Computer Science", "Civics"]
data = [100, 125, 132, 90, 80, 70, 60, 50, 45, 40]
line_labels = ['Subject', 'Number of Students']

# Plot the data with the type of rose chart.
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='polar')
num_categories = len(data_labels)

# Calculate the sector angle
sector_angle = (2 * np.pi) / num_categories

# Draw the sectors corresponding to different categories by making the width parameter in "ax.bar" sector_angle
# Assign a different color to each sector
for i, d in enumerate(data):
    ax.bar(sector_angle * i, d, width=sector_angle, label=data_labels[i], color=plt.cm.Set1(i/num_categories))

# Set the legend position
ax.legend(data_labels, bbox_to_anchor=(0.5, -0.05), loc='center', ncol=5)

# Set the ticks and labels
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=10)

# Display the title
ax.set_title("Number of Students Enrolled in Different Subjects in 2021", fontsize=15)

# Resize the image
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-032010_55.png')

# Clear the current image state
plt.clf()