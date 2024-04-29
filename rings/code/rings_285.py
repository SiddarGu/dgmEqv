
import matplotlib.pyplot as plt 
import numpy as np 

#Transform the given data into three variables: data_labels, data, line_labels. 
data_labels = ['Engagement', 'Reach', 'User Satisfaction', 'Content Quality', 'Traffic']
data = np.array([24, 13, 19, 22, 22])
line_labels = ['Category', 'ratio']

#Create figure before plotting, i.e., add_subplot() follows plt.figure().
fig, ax = plt.subplots(figsize=(8, 8))

#Plot the data with the type of rings chart. 
ax.pie(data, radius=1, startangle=90, counterclock=False, wedgeprops={'width': 0.5})

#To change the pie chart into a ring chart in your code, you need to correctly add a white circle to the center of the pie chart.
center_circle = plt.Circle((0, 0), 0.5, color='white')
ax.add_artist(center_circle)

#The plottig of different data lines should use different colors and do not use the white color.
ax.set_prop_cycle('color', ['red', 'blue', 'green', 'yellow', 'orange'])

#Create only one pie chart using the ax.pie() method and setting the startangle and counterclock parameters for better layout.
ax.pie(data, radius=1, startangle=90, counterclock=False, wedgeprops={'width': 0.5})

#For the plot of legend, do not plot the legend of gridlines or the legend of ax.fill output, only the data_labels are needed to provide the legend, i.e., ax.legend(data_labels). 
ax.legend(data_labels, bbox_to_anchor=(1.2, 1), loc="upper right", prop={'size': 14})

#Drawing techniques such as background grids can be used.
ax.grid(linestyle="--", linewidth=0.5, color='.25', zorder=-10)

#The title of the figure should be Social Media and Web Performance Analysis - 2023.
ax.set_title('Social Media and Web Performance Analysis - 2023', fontsize=20)

#The image must be saved as /cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-112353_147.png.
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-112353_147.png')

#Clear the current image state at the end of the code.
plt.cla()