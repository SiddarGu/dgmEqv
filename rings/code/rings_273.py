
import matplotlib.pyplot as plt
import numpy as np

#Transform the given data into three variables: data_labels, data, line_labels. Data_labels represents the labels of each column except the first column. Line_labels represents the labels of each row except the first row. Data represent the numerical array in the data.
data_labels = ['Renewables','Fossil Fuels','Nuclear Energy','Conservation','Efficiency']
line_labels = ['Category', 'ratio']
data = [[20,40,20,15,5]]

#Create figure before plotting, i.e., add_subplot() follows plt.figure().
fig, ax = plt.subplots(figsize=(9, 9))

#Plot the data with the type of rings chart.
#The plottig of different data lines should use different colors and do not use the white color.
#Create only one pie chart using the `ax.pie()` method and setting the `startangle` and `counterclock` parameters for better layout.
ax.pie(data[0], labels=data_labels, startangle=90, counterclock=False, colors=['#a5a1d6', '#ffd5a8', '#ffb0b6', '#fad8b2', '#eef9df'])

#To change the pie chart into a ring chart in your code, you need to correctly add a white circle to the center of the pie chart.
#After creating the circle with `plt.Circle`, you must add this circle to the axes using `ax.add_artist()`.
#You can adjust the radius of the inner circle to create different ring widths.
inner_circle = plt.Circle((0, 0), 0.60, color='white')
ax.add_artist(inner_circle)

#For the plot of legend, do not plot the legend of gridlines or the legend of ax.fill output, only the data_labels are needed to provide the legend, i.e., ax.legend(data_labels).
#The positioning of the legend should not interfere with the chart and title.
ax.legend(data_labels, loc='upper right', bbox_to_anchor=(1.25, 1), title=line_labels[0])

#Drawing techniques such as background grids can be used.
ax.grid(linestyle='--', linewidth=1, axis='both', alpha=0.3)

#The title of the figure should be  Energy and Utilities Usage Overview - 2023.
plt.title('Energy and Utilities Usage Overview - 2023')

#Automatically resize the image by tight_layout().
plt.tight_layout()

#The image must be saved as /cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-112353_131.png.
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-112353_131.png")

#Clear the current image state at the end of the code.
plt.clf()