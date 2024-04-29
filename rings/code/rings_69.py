
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels.
data_labels = ['Public Safety', 'Education', 'Social Services', 'Infrastructure', 'Taxation']
data = [14, 17, 26, 35, 8]
line_labels = ['Category','Ratio']

# Create figure before plotting, i.e., add_subplot() follows plt.figure()
fig, ax = plt.subplots(figsize=(8, 8))

# Plot the data with the type of rings chart.
ax.pie(data, labels=data_labels, startangle=90, counterclock=False)

# To change the pie chart into a ring chart in your code, you need to correctly add a white circle to the center of the pie chart. After creating the circle with `plt.Circle`, you must add this circle to the axes using `ax.add_artist()`.
centre_circle = plt.Circle((0, 0), 0.5, fc='white')
ax.add_artist(centre_circle)

# For the plot of legend, do not plot the legend of gridlines or the legend of ax.fill output, only the data_labels are needed to provide the legend, i.e., ax.legend(data_labels). The positioning of the legend should not interfere with the chart and title.
ax.legend(data_labels, bbox_to_anchor=(1.2, 0.8))

# Drawing techniques such as background grids can be used.
ax.grid(True)

# The title of the figure should be Government Policy Evaluation - 2023.
ax.set_title("Government Policy Evaluation - 2023")

# Automatically resize the image by tight_layout().
plt.tight_layout()

# The image must be saved as /cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_138.png.
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_138.png', bbox_inches='tight')

# Clear the current image state at the end of the code.
plt.clf()