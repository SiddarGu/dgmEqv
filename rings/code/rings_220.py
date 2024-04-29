

import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels.
data_labels = ['Regulatory Compliance', 'Litigation', 'Risk Management', 'Professional Advice', 'Corporate Governance']
data = [30, 27, 19, 13, 11]
line_labels = ['Topic', 'ratio']

# Plot the data with the type of rings chart. 
fig, ax = plt.subplots(figsize=(10, 10))

# Create only one pie chart using the `ax.pie()` method and setting the `startangle` and `counterclock` parameters for better layout.
ax.pie(data, labels=data_labels, startangle=90, counterclock=False, autopct="%1.1f%%")

# To change the pie chart into a ring chart in your code, you need to correctly add a white circle to the center of the pie chart.
centre_circle = plt.Circle((0,0),0.7,fc='white')
ax.add_artist(centre_circle)

# For the plot of legend, do not plot the legend of gridlines or the legend of ax.fill output, only the data_labels are needed to provide the legend, i.e., ax.legend(data_labels).
ax.legend(data_labels, loc='upper left',  bbox_to_anchor=(0.9, 0.8))

# Drawing techniques such as background grids can be used.
ax.grid()

# The title of the figure should be Legal Affairs Performance - 2023.
ax.set_title('Legal Affairs Performance - 2023')

# Automatically resize the image by tight_layout().
plt.tight_layout()

# The image must be saved as
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_79.png')

# Clear the current image state at the end of the code.
plt.clf()