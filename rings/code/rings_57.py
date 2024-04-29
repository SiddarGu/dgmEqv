
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels 
data_labels = ['Network Security','Data Storage','Cloud Computing','Internet of Things','Artificial Intelligence']
data = np.array([20,10,30,15,25])
line_labels = ['Category','ratio']

# Plot the data with the type of rings chart. Create figure before plotting, i.e., add_subplot() follows plt.figure().
fig = plt.figure(figsize=(14,7))
ax = fig.add_subplot(111)

# The plottig of different data lines should use different colors and do not use the white color.
ax.pie(data, labels=data_labels, startangle=90, counterclock=False,colors=['green','red','blue','yellow','purple'])

# Create only one pie chart using the `ax.pie()` method and setting the `startangle` and `counterclock` parameters for better layout.
# To change the pie chart into a ring chart in your code, you need to correctly add a white circle to the center of the pie chart. After creating the circle with `plt.Circle`, you must add this circle to the axes using `ax.add_artist()`.
# You can adjust the radius of the inner circle to create different ring widths.
centre_circle = plt.Circle((0,0),0.5,fc='white')
ax.add_artist(centre_circle)

# For the plot of legend, do not plot the legend of gridlines or the legend of ax.fill output, only the data_labels are needed to provide the legend, i.e., ax.legend(data_labels). The positioning of the legend should not interfere with the chart and title.
ax.legend(data_labels,loc='best')

# Drawing techniques such as background grids can be used.
ax.grid(True)

# The title of the figure should be  Technology and the Internet: An Overview - 2023.
ax.set_title('Technology and the Internet: An Overview - 2023')

# Automatically resize the image by tight_layout().
plt.tight_layout()

# The image must be saved as /cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_120.png.
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_120.png')

# Clear the current image state at the end of the code.
plt.clf()