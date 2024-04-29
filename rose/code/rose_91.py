
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Surgery', 'Diagnostics', 'Radiology', 'Oncology', 'Cardiology', 'Physical Therapy', 'Endocrinology', 'Immunology']
line_labels = ['Treatment', 'Number of Patients']
data = np.array([[45, 87, 37, 98, 63, 72, 50, 40]])

# Plot the data with the type of rose chart
fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot(111, polar=True)

# Different sectors represent different categories with the same angle, whose radius is proportional to the corresponding value
sector_angle = (2 * np.pi) / len(data_labels)
for i in range(len(data_labels)):
    ax.bar(i * sector_angle, data[0][i], width=sector_angle, label=data_labels[i])

# Create figure before plotting
ax.set_theta_direction(-1)
ax.set_theta_zero_location('N')
ax.set_title('Number of Patients Treated in Healthcare Institutions in 2021', y=1.08)

# Set the angle parameters in the ax.set_xticks method
ax.set_xticks(np.linspace(0, 2*np.pi, len(data_labels), endpoint=False))
# Set the category labels
ax.set_xticklabels(data_labels, fontsize=12)

# Position the legend so that it does not cover any part of the chart
ax.legend(data_labels, bbox_to_anchor=(1.2, 1.1))
# Display gridlines
ax.grid(color='gray', linestyle='--', linewidth=1, alpha=0.5)

# Save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_78.png')
# Clear the current image state
plt.clf()