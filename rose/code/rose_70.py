
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels. 
data_labels = ['Economics', 'Psychology', 'Sociology', 'Philosophy', 'Anthropology', 'Political Science', 'History', 'Linguistics']
data = [108, 70, 100, 60, 50, 40, 30, 20]
line_labels = ['Category', 'Number']

# Create figure and set polor coordinates.
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

# Set sector angle and draw sectors.
sector_angle = (2 * np.pi) / len(data_labels)
for i in range(len(data_labels)):
    ax.bar(i*sector_angle, data[i], width=sector_angle, label=data_labels[i], color=plt.cm.Set2(i))

# Set ticks and labels.
ax.set_xticks(np.linspace(0, 2*np.pi, len(data_labels), endpoint=False))
ax.set_xticklabels(data_labels, fontsize=7, rotation=30, wrap=True)

# Place legend outside of the main chart area.
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 0.9))

# Set figure title
plt.title('Number of Majors in Social Sciences and Humanities in 2021')

# Resize image
plt.tight_layout()

# Save figure
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_39.png', dpi=200)

# Clear the current image state
plt.clf()