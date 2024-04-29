
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels. 
data_labels = ['Compliance', 'Regulations', 'Court Cases', 'Training', 'Research']
data = [30, 20, 40, 5, 5]
line_labels = ['Category', 'ratio']

# Plot the data with the type of rings chart. 
fig, ax = plt.subplots(figsize=(6,6))

# Create only one pie chart and set the `startangle` and `counterclock` parameters for better layout.
ax.pie(data, labels=data_labels, startangle=90, counterclock=False)

# Change the pie chart into a ring chart.
centre_circle = plt.Circle((0,0), 0.7, color='white')
ax.add_artist(centre_circle)

# Drawing techniques such as background grids can be used.
ax.grid(True)

# Provide the legend.
ax.legend(data_labels, loc='lower right', bbox_to_anchor=(1.3, 0.5))

# Set the title of the figure.
ax.set_title('Legal Affairs Overview - 2023')

# Automatically resize the image by tight_layout().
plt.tight_layout()

# Save the image.
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_37.png')

# Clear the current image state at the end of the code.
plt.clf()