
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables
data_labels = ["Academic Performance", "Enrollment Rate", "Student Satisfaction", 
               "Teacher Performance", "Graduation Rate"]
data = [0.28, 0.20, 0.35, 0.10, 0.07]
line_labels = ["Area", "Ratio"]

# Plot the data with the type of rings chart
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_title('Education and Academics in 2023')

# Create only one pie chart
ax.pie(data, startangle=90, counterclock=False, colors=['#98FB98', '#9370DB', '#FF4500', '#ADFF2F', '#DCDCDC'])

# Add a white circle to the center of the pie chart
centre_circle = plt.Circle((0, 0), 0.7, fc='white')
ax.add_artist(centre_circle)

# Add legend
ax.legend(data_labels, loc="best", bbox_to_anchor=(1, 0.5))

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231225-122818_11.png')

# Clear the current image state
plt.clf()