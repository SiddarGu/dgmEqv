
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels.
data_labels = ['Adoption', 'Connectivity', 'Performance', 'Security', 'Innovation']
data = [31, 19, 12, 38, 0]
line_labels = ['Category', 'Ratio']

# Plot the data with the type of rings chart. Create figure before plotting, i.e., add_subplot() follows plt.figure().
fig, ax = plt.subplots(figsize=(6, 6))

# Plot the pie chart.
ax.pie(data, startangle=90, counterclock=False, autopct='%1.1f%%')

# To change the pie chart into a ring chart in your code, you need to correctly add a white circle to the center of the pie chart.
centre_circle = plt.Circle((0, 0), 0.5, color='white')

# After creating the circle with `plt.Circle`, you must add this circle to the axes using `ax.add_artist()`.
ax.add_artist(centre_circle)

# Draw a background grid.
ax.grid(True)

# For the plot of legend, do not plot the legend of gridlines or the legend of ax.fill output, only the data_labels are needed to provide the legend, i.e., ax.legend(data_labels).
# The positioning of the legend should not interfere with the chart and title.
ax.legend(data_labels, loc='best', bbox_to_anchor=(1.5, 1.0))

# Automatically resize the image by tight_layout().
plt.tight_layout()

# The title of the figure should be  Technology and Internet Usage - 2023.
ax.set_title('Technology and Internet Usage - 2023')

# The image must be saved as /cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-112353_122.png.
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-112353_122.png')

# Clear the current image state at the end of the code.
plt.clf()