
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Engagement', 'Retention', 'Training', 'Performance', 'Diversity']
data = np.array([25, 20, 20, 20, 15])
line_labels = ['Element', 'ratio']

# Plot the data with the type of rings chart
fig, ax = plt.subplots(figsize=(8, 8))

# Create only one pie chart using the `ax.pie()` method and setting the `startangle` and `counterclock` parameters for better layout
ax.pie(data, startangle=90, counterclock=False, autopct='%1.1f%%')

# To change the pie chart into a ring chart in your code
# Create a white circle to the center of the pie chart
center_circle = plt.Circle((0, 0), 0.5, color='white')
# Add this circle to the axes
ax.add_artist(center_circle)

# For the plot of legend, do not plot the legend of gridlines or the legend of ax.fill output, only the data_labels are needed to provide the legend
ax.legend(data_labels, loc="lower center")

# Drawing techniques such as background grids can be used
ax.grid()

# The title of the figure should be  Employee Management - 2021
ax.set_title("Employee Management - 2021")

# Adjust the radius of the inner circle to create different ring widths
center_circle.set_radius(0.4)

# Automatically resize the image by tight_layout()
plt.tight_layout()

# The image must be saved as /cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-112353_22.png
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-112353_22.png')

# Clear the current image state at the end of the code
plt.clf()