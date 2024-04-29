
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels. 
data_labels = ["Recruiting", "Training and Development", "Employee Relations", "Benefits Administration", "Performance Management", "Labor Relations", "Compensation", "Organizational Development"]
data = [58, 49, 45, 39, 25, 20, 17, 10]
line_labels = ["HR Activity", "Number of Employees"]

# Create a figure and set up a polar axes
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='polar')

# Calculate the sector angle
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Plot the data with the type of rose chart
# Set up different colors for different sectors
colors = ['#E16736', '#FFB347', '#EDB92E', '#8FBF26', '#3F7F93', '#1B3F8F', '#2E1488', '#9D1B7F']
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i], color=colors[i])

# Set up the ticks and legend
ax.set_xticks(np.pi / 180. * np.linspace(0, 360, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=12)
ax.set_title("Employee Count in Human Resources Activities in 2020", fontsize=14)
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=12)

# Automatically resize the image
plt.tight_layout()

# Save the file
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_150.png')

# Clear the current image state
plt.clf()