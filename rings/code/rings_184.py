
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels. 
data_labels = ['Raw Materials','Labor','Overhead','Machinery']
data = [41,23,11,25]
line_labels = ['Category','ratio']

# Create figure before plotting, i.e., add_subplot() follows plt.figure().
fig,ax = plt.subplots(figsize=(8,6))

# Plot the data with the type of rings chart. 
ax.pie(data, startangle=90, counterclock=False, labels=data_labels, autopct='%1.1f%%',
       wedgeprops={'linewidth':2,'edgecolor': 'white'})

# To change the pie chart into a ring chart in your code, you need to correctly add a white circle to the center of the pie chart. 
centre_circle = plt.Circle((0,0),0.7,fc='white')
ax.add_artist(centre_circle)

# For the plot of legend, do not plot the legend of gridlines or the legend of ax.fill output, only the data_labels are needed to provide the legend, i.e., ax.legend(data_labels). The positioning of the legend should not interfere with the chart and title.
ax.legend(data_labels, bbox_to_anchor=(1.05,0.5), loc="center left", borderaxespad=0.)

# Drawing techniques such as background grids can be used.
ax.grid(axis='x', linestyle='--', linewidth=0.6)

# The title of the figure should be Manufacturing and Production Costs - 2023.
ax.set_title("Manufacturing and Production Costs - 2023")

# Automatically resize the image by tight_layout().
plt.tight_layout()

# The image must be saved as /cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_30.png.
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_30.png")

# Clear the current image state at the end of the code.
plt.clf()