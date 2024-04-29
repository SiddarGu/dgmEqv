
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels.
data_labels = ['Retention Rates', 'Employee Satisfaction', 'Training Quality', 'Recruitment Efficiency', 'Performance Management']
data = [24, 22, 19, 19, 16]

# Create figure
fig = plt.figure(figsize=(8, 8))

# Plot the data with the type of rings chart
ax = fig.add_subplot(111)
ax.pie(data, startangle=90, counterclock=False, colors=['red', 'green', 'blue', 'orange', 'purple'])

# Change the pie chart into a ring chart
inner_circle = plt.Circle((0, 0), 0.7, color='white')
ax.add_artist(inner_circle)

# Create only one pie chart
ax.legend(data_labels, loc='best')

# Add gridlines to the chart
plt.grid(axis='both', linestyle='--')

# Add title to the figure
plt.title('Human Resources and Employee Management - 2023')

# Resize the image
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_32.png')

# Clear the current image state
plt.clf()