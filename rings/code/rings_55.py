
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Transform the given data into three variables: data_labels, data, line_labels.
data_labels = ['Events', 'Sponsorships', 'Media Rights', 'Ticket Sales', 'Licensing']
data = [0.25, 0.1, 0.3, 0.2, 0.15]
line_labels = ['Category', 'ratio']

# Plot the data with the type of rings chart. Create figure before plotting, i.e., add_subplot() follows plt.figure().
fig, ax = plt.figure(figsize=(8, 8)), plt.subplot()

# The plottig of different data lines should use different colors and do not use the white color.
ring_colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'plum']
ax.pie(data, colors=ring_colors, startangle=90, counterclock=False, labels=data_labels,
       textprops={'fontsize': 10}, wedgeprops={'linewidth': 2, 'edgecolor': 'white'})

# To change the pie chart into a ring chart in your code, you need to correctly add a white circle to the center of the pie chart.
centre_circle = plt.Circle((0, 0), 0.4, fc='white')
ax.add_artist(centre_circle)

# For the plot of legend, do not plot the legend of gridlines or the legend of ax.fill output, only the data_labels are needed to provide the legend, i.e., ax.legend(data_labels). The positioning of the legend should not interfere with the chart and title.
ax.legend(data_labels, bbox_to_anchor=(1.1, 0.5), loc='center left', frameon=False)

# Drawing techniques such as background grids can be used.
ax.grid(color='gray', linestyle='-', linewidth=1)

# The title of the figure should be  Sports and Entertainment Business Analysis - 2023.
ax.set_title("Sports and Entertainment Business Analysis - 2023")

# Automatically resize the image by tight_layout().
plt.tight_layout()

# The image must be saved as /cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_119.png.
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_119.png')

# Clear the current image state at the end of the code.
plt.clf()