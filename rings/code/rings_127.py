
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle

# Transform the given data into three variables: data_labels, data, line_labels. 
data_labels = ['Curriculum','Student Performance','Teaching Quality','Infrastructure','Research Output']
data = np.array([25,20,35,12,8])
line_labels = ['Area','ratio']

# Plot the data with the type of rings chart. 
fig, ax = plt.subplots(figsize=(8, 8))

# Create only one pie chart using the `ax.pie()` method and setting the `startangle` and `counterclock` parameters for better layout.
ax.pie(data, startangle=90, counterclock=False,labels=data_labels, autopct='%1.1f%%', pctdistance=0.5, labeldistance=1.2, wedgeprops={'linewidth': 2, 'edgecolor':'w'})

# To change the pie chart into a ring chart in your code, you need to correctly add a white circle to the center of the pie chart. After creating the circle with `plt.Circle`, you must add this circle to the axes using `ax.add_artist()`.
circle = Circle((0,0), 0.75, color='white')
ax.add_artist(circle)

# For the plot of legend, do not plot the legend of gridlines or the legend of ax.fill output, only the data_labels are needed to provide the legend, i.e., ax.legend(data_labels). The positioning of the legend should not interfere with the chart and title.
ax.legend(data_labels, bbox_to_anchor=(1.3, 0.9))

# Drawing techniques such as background grids can be used.
ax.grid(linestyle='--', linewidth=0.5)

# The title of the figure should be  Education Quality Report - 2023.
plt.title('Education Quality Report - 2023', fontsize=14)

# Automatically resize the image by tight_layout().
plt.tight_layout()

# The image must be saved as /cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_79.png.
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_79.png")

# Clear the current image state at the end of the code.
plt.clf()