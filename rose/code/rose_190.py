
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels. 
data_labels = ["Music", "Visual Arts", "Theatre", "Dance", "Architecture", "Literature", "Film"]
data = [43, 97, 17, 36, 96, 60, 68]
line_labels = ["Category", "Number"]

# Create figure before plotting, i.e., add_subplot() follows plt.figure(). 
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='polar')

# Modify the axes to use polar coordinates with `polar=True` or 'projection='polar'. 
ax.set_theta_direction(-1)
ax.set_theta_zero_location("N")

# Assign a different color to each sector
sector_colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b", "#e377c2"]
num_categories = len(data_labels)

# Calculate the sector angle 
sector_angle = (2 * np.pi) / num_categories

# Draw sectors corresponding to different categories
for i in range(len(data_labels)):
    ax.bar(i * sector_angle, data[i], width=sector_angle, label=data_labels[i], color=sector_colors[i])

# Set the x-axis tick labels to match the different categories
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=10, ha="center")

# Create the legend
ax.legend(bbox_to_anchor=(1.1,0.5), loc="center left", fontsize=10)

# Set the title
ax.set_title('Number of Arts and Culture Practices by Field', fontsize=12)

# Prettify the chart
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-112325_28.png')

# Clear the current image state
plt.clf()