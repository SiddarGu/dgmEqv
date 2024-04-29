
import matplotlib.pyplot as plt
import numpy as np

# Transform data into three variables
data_labels = ['Hiring', 'Onboarding', 'Training and Development', 'Performance Management', 
               'Benefits and Compensation', 'Employee Relations', 'Termination', 'Diversity and Inclusion']
data = [120, 96, 80, 64, 48, 32, 16, 0]
line_labels = ['HR Category', 'Number']

# Create figure
fig = plt.figure(figsize=(12.8, 9.6))
ax = fig.add_subplot(111, projection='polar')

# Set up axes in polar coordinates
ax.set_theta_direction(-1)
ax.set_theta_zero_location('N')

# Calculate sector angle
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Plot data
for i, d in enumerate(data):
    ax.bar(sector_angle * i, d, width=sector_angle, label=data_labels[i])

# Set ticks
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels)

# Set title
ax.set_title('Number of Employees Involved in Each Human Resources Category in 2021', fontsize=20)

# Set legend
ax.legend(bbox_to_anchor=(1, 1), loc='upper left')

# Save image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231225-125808_11.png')

# Clear current image state
plt.clf()