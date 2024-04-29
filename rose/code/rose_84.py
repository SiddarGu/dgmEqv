
import matplotlib.pyplot as plt
import numpy as np

# Transform data into three variables: data_labels, data, line_labels
data_labels = ["English","History","Sociology","Psychology","Political Science","Anthropology","Economics","Philosophy","Languages", "Art"]
data = [90,80,60,50,45,40,35,30,25,20]
line_labels = ["Subject","Number of Students"]

# Create figure
fig = plt.figure(figsize=(10, 8))

# Plot data in rose chart
ax = fig.add_subplot(111, projection='polar') 
num_categories = len(data)
sector_angle = (2 * np.pi) / num_categories

# Assign different color to each sector
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#ffcc99', '#66b3ff','#99ff99','#ff9999','#c2c2f0','#ffb3e6']

# Draw sectors corresponding to different categories
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i], color=colors[i])

# Set labels
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels)

# Set legend and title
ax.legend(bbox_to_anchor=(1, 0.65), labels=data_labels)
ax.set_title("Enrollment of Students in Social Sciences and Humanities Subjects in 2021")

# Resize the image
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_63.png')

# Clear the current image state
plt.cla()