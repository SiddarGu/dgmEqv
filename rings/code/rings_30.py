
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables
data_labels = ['Academic Performance', 'Student Engagement', 'Resource Allocation', 'Staff Efficiency', 'Facility Quality']
data = [25, 25, 25, 15, 10]
line_labels = ['Category', 'ratio']

# Plot the data with the type of rings chart
fig, ax = plt.subplots(figsize=(10,7))
ax.pie(data, startangle=90, counterclock=False,labeldistance=1.1, 
        colors=['#00A6ED', '#FFC300', '#FF5733', '#C70039', '#900C3F'])
# Change the pie chart into a ring chart
centre_circle = plt.Circle((0,0), 0.7, color='white')
ax.add_artist(centre_circle)
# Set legend
ax.legend(data_labels, loc=3, bbox_to_anchor=(0.5, 0.1))
# Set title
ax.set_title("Education Quality Assessment - 2023")
# Resize the image
plt.tight_layout()
# Save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231225-122818_40.png')
# Clear the current image state
plt.clf()