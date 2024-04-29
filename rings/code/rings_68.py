
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels. Data_labels represents the labels of each column except the first column. Line_labels represents the labels of each row except the first row. Data represent the numerical array in the data.
data_labels = ['Viewership','Participation','Media Coverage','Sponsorship', 'Revenues']
line_labels = ['Category']
data = np.array([35, 22, 21, 15, 7])

# Plot the data with the type of rings chart. Create figure before plotting, i.e., add_subplot() follows plt.figure().
fig, ax = plt.subplots(figsize=(12, 8))

# The plottig of different data lines should use different colors and do not use the white color.
colors = ['#F35F36', '#FFCA2A', '#8EC741', '#1D7A9A', '#3A3B98']

# Create only one pie chart using the `ax.pie()` method and setting the `startangle` and `counterclock` parameters for better layout.
ax.pie(data, startangle=90, counterclock=False, colors=colors)

# To change the pie chart into a ring chart in your code, you need to correctly add a white circle to the center of the pie chart. After creating the circle with `plt.Circle`, you must add this circle to the axes using `ax.add_artist()`.
inner_circle = plt.Circle((0, 0), 0.5, color='white')
ax.add_artist(inner_circle)

# For the plot of legend, do not plot the legend of gridlines or the legend of ax.fill output, only the data_labels are needed to provide the legend, i.e., ax.legend(data_labels). The positioning of the legend should not interfere with the chart and title.
plt.legend(data_labels, loc="best")

# Drawing techniques such as background grids can be used.
ax.grid(False)

# The title of the figure should be  Sports and Entertainment Performance - 2023.
plt.title('Sports and Entertainment Performance - 2023')

# If the text length of the label is too long, use the method of adding the parameter "rotation" or display label on separate lines seting “wrap=true”.
plt.tight_layout()

# The image must be saved as /cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_136.png.
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_136.png')

# Clear the current image state at the end of the code.
plt.cla()