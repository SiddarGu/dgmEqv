
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Mental Health','Physical Health','Immunization','Vaccination','Nutrition','Hygiene','Reproductive Health','Preventive Care']
data = [200, 150, 120, 90, 70, 50, 40, 30]
line_labels = ['Category','Number of Cases']

# Transform data into three variables: data_labels, data, line_labels

# Plot the data with rose chart
fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')

# Set the width of each sector corresponding to the data
sector_angle = (2 * np.pi) / len(data_labels)

# Draw sectors corresponding to different categories with different colors
for i, data_label in enumerate(data_labels):
    ax.bar(i * sector_angle, data[i], width=sector_angle, label=data_label, color=plt.cm.Set1(i))

# Set the legend and ensure it does not overlap with chart
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

# Set ticks angle for each sector and label for each sector
ax.set_xticks(np.linspace(0, 2*np.pi, len(data_labels), endpoint=False))
ax.set_xticklabels(data_labels, wrap=True)

# Set the title of the figure
plt.title("Number of Cases of Healthcare and Health in 2021")

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_122.png')

# Clear the current image state
plt.clf()