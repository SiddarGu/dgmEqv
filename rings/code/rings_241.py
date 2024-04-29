
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Transform the given data into three variables: data_labels, data, line_labels. 
data_labels = ['Fundraising', 'Overhead Costs', 'Community Service', 'Resource Allocation', 'Public Awareness']
data = [32, 21, 33, 12, 2]
line_labels = ['Category', 'ratio']

# Create figure before plotting, i.e., add_subplot() follows plt.figure().
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)

# Plot the data with the type of rings chart.
ax.pie(data, labels=data_labels, startangle=90, counterclock=False, autopct=lambda pct: '{:.1f}%'.format(pct))

# To change the pie chart into a ring chart in your code, you need to correctly add a white circle to the center of the pie chart. 
centre_circle = plt.Circle((0,0),0.7,fc='white')

# After creating the circle with plt.Circle, you must add this circle to the axes using ax.add_artist().
ax.add_artist(centre_circle)

# For the plot of legend, do not plot the legend of gridlines or the legend of ax.fill output, only the data_labels are needed to provide the legend, i.e., ax.legend(data_labels).
ax.legend(data_labels, loc="best")

# Drawing techniques such as background grids can be used.
ax.grid(True)

# The title of the figure should be  Non-Profit Organization Performance - 2023.
plt.title('Non-Profit Organization Performance - 2023')

# Automatically resize the image by tight_layout().
plt.tight_layout()

# The image must be saved as /cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-104042_17.png.
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-104042_17.png')

# Clear the current image state at the end of the code.
plt.clf()