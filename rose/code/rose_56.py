
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels. 
data_labels = ['Recruiting', 'Onboarding', 'Training', 'Performance Review', 
               'Salary Management', 'Benefits Administration', 'Talent Management',
               'Career Development', 'Termination']
data = np.array([100, 95, 90, 85, 80, 75, 70, 65, 60])
line_labels = ['Activity', 'Number of Employees']

# Create figure before plotting, i.e., add_subplot() follows plt.figure(). 
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111, projection='polar')

# Modify the axes to use polar coordinates 
ax.set_theta_direction(-1)
ax.set_theta_zero_location('N')

# Different sectors represent different categories with the same angle, 
# whose radius is proportional to the corresponding value
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Draw sectors corresponding to different categories by making the 
# width parameter in "ax.bar" sector_angle.
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, bottom=0.0, 
           label=data_labels[i])

# Assign a label to each sector when you create them with `ax.bar`. 
# Then, when you call `ax.legend()`, it will display labels for all categories.
ax.legend(loc='upper right', bbox_to_anchor=(1.25, 0.95))

# Set the angle parameters in the `ax.set_xticks` method to match the
# center position of each sector, and then use `ax.set_xticklabels` 
# to set these category labels.
ax.set_xticks(sector_angle * np.arange(num_categories))
ax.set_xticklabels(data_labels, rotation=90)

# Ensure that the number of ticks set with `ax.set_xticks()` matches 
# exactly the number of categories or labels you have in `data_labels`.
ax.set_xticks(sector_angle * np.arange(num_categories))

# Set the title of the figure
plt.title('Number of Employees Involved in Human Resources Activities')

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_16.png')

# Clear the current image state at the end of the code
plt.clf()