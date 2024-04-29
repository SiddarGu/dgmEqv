
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Retention', 'Training', 'Performance', 'Satisfaction', 'Recruitment']
data = [17, 10, 21, 35, 17]
line_labels = ['Category', 'Ratio']

# Plot the data with the type of rings chart
fig, ax = plt.subplots(figsize=(8, 8))
# Create only one pie chart using the `ax.pie()` method and setting the `startangle` and `counterclock` parameters for better layout
ax.pie(data, labels=data_labels, startangle=90, counterclock=False, autopct='%1.1f%%')
# To change the pie chart into a ring chart in your code, you need to correctly add a white circle to the center of the pie chart
inner_circle = plt.Circle((0, 0), 0.7, color='white')
# After creating the circle with `plt.Circle`, you must add this circle to the axes using `ax.add_artist()`
ax.add_artist(inner_circle)
# For the plot of legend, do not plot the legend of gridlines or the legend of ax.fill output, only the data_labels are needed to provide the legend, i.e., ax.legend(data_labels)
ax.legend(data_labels, loc="best", bbox_to_anchor=(1, 0, 0.5, 0.5))
# Drawing techniques such as background grids can be used
ax.grid()
# The title of the figure should be  Human Resources and Employee Management - 2021
ax.set_title("Human Resources and Employee Management - 2021")
# Automatically resize the image by tight_layout()
plt.tight_layout()
# The image must be saved as /cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231225-122818_50.png
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231225-122818_50.png")
# Clear the current image state at the end of the code
plt.clf()