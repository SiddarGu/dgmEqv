
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels.
data_labels = ['History', 'Literature', 'Philosophy', 'Art', 'Music', 'Anthropology', 'Political Science', 'Sociology']
data = [542, 633, 455, 741, 953, 1350, 1020, 1144]
line_labels = ['Subjects', 'Number of Enrolled Students']

# Plot the data with the type of rose chart.
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(1, 1, 1, polar=True)
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

for n in range(num_categories):
    ax.bar(sector_angle * n, data[n], width=sector_angle, label=data_labels[n], color=plt.cm.Dark2(n))

# Set the title and labels.
ax.set_title("Number of Students Enrolled in Social Sciences and Humanities Courses in 2021", fontsize=14)
ax.set_xticks(np.arange(0, 2 * np.pi, sector_angle))
ax.set_xticklabels(data_labels, rotation=0)

# Add the legend outside the chart and adjust the legend.
ax.legend(bbox_to_anchor=(1.04, 0.5), loc="center left")

# Ensure that the number of ticks set with ax.set_xticks() matches exactly the number of categories or labels you have in data_labels.
ax.set_xticks(np.arange(0, 2 * np.pi, sector_angle))
ax.set_xticklabels(data_labels, rotation=0)

# Ensure that each category label is correctly positioned at the center of its corresponding sector.
ax.set_xticks(np.arange(0, 2 * np.pi, sector_angle) + sector_angle/2)
ax.set_xticklabels(data_labels, rotation=0)

# Save the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-032010_15.png')

# Clear the current image state at the end of the code.
plt.clf()