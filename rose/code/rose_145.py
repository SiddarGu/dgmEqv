
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Cardiology', 'Endocrinology', 'Oncology', 'Gastroenterology', 'Pulmonology', 'Nephrology', 'Hematology', 'Infectious Diseases']
data = [200, 175, 150, 125, 100, 75, 50, 25]
line_labels = ['Number of Patients']

# Plot the data with the type of rose chart
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, polar=True)

# Calculate the sector angle
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Create sectors for different categories
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i], color=plt.cm.Set2(i))

# Set the ticks
ax.set_xticks(np.linspace(0.0, 2 * np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=12)

# Modify the legend position
ax.legend(loc='upper right',bbox_to_anchor=(1.3, 1.0))

# Set the title of the figure
plt.title('Number of Healthcare Patients by Specialty in 2021', fontsize=16)

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-075144_25.png')

# Clear the current image state at the end of the code
plt.clf()