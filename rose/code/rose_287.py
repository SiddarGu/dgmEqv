
import matplotlib.pyplot as plt
import numpy as np

#Transform the given data into three variables: data_labels, data, line_labels. 
#Data_labels represents the labels of each column except the first column. 
#Line_labels represents the labels of each row except the first row. 
#Data represent the numerical array in the data.
data_labels = ['Wheat','Rice','Soybeans','Corn','Potatoes','Tomatoes','Cabbage','Carrots','Spinach']
data = [120,150,100,175,140,110,90,70,50]
line_labels = ['Crop','Number of Farms']

#Plot the data with the type of rose chart. Create figure before plotting, i.e., add_subplot() follows plt.figure(). 
#Modify the axes to use polar coordinates with `polar=True` or 'projection='polar'. 
#This change will set up the axes in polar coordinates, which is necessary for creating a rose chart.
num_categories = len(data_labels)
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(1,1,1,projection='polar')
sector_angle = (2 * np.pi) / num_categories

#Different sectors represent different categories with the same angle, whose radius is proportional to the corresponding value, 
#and the angles of these sectors must add up to 360 degrees, i.e., use "sector_angle = (2 * np.pi) / num_categories" to calculate the sector angle 
#and draw sectors corresponding to different categories by making the width parameter in "ax.bar" sector_angle.
for i in range(len(data)):
    ax.bar(sector_angle * i, data[i], width=sector_angle, color=plt.cm.Set1(i/num_categories), label=data_labels[i])

#Assign a different color to each sector and add a legend next to the chart that clearly labels the category each sector represents, 
#ensuring that the legend does not obscure any part of the chart.
#You should use a loop to assign a label to each sector when you create them with `ax.bar`. 
#Then, when you call `ax.legend()`, it will display labels for all categories. 
ax.legend(data_labels, bbox_to_anchor=(1.2, 0.8))

#Make sure the legend is positioned in such a way that it doesn't overlap with the chart.
#Ensure that the number of ticks set with `ax.set_xticks()` matches exactly the number of categories or labels you have in `data_labels`.
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories, endpoint=False))

#Make sure that each category label is correctly positioned at the center of its corresponding sector. 
#This can be achieved by adjusting the angle parameters in the `ax.set_xticks` method. 
#Ensure that each angle parameter corresponds to the center position of each sector, and then use `ax.set_xticklabels` to set these category labels.
ax.set_xticklabels(data_labels, fontsize=14, color='black', rotation=45)

#The title of the figure should be  Farming of Major Crops in the US in 2021.
ax.set_title('Farming of Major Crops in the US in 2021', fontsize=20)

#Drawing techniques such as background grids can be used.
ax.grid(color='gray', linestyle=':', linewidth=1)

#The image must be saved as /cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-070122_9.png.
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-070122_9.png')

#Clear the current image state at the end of the code.
plt.clf()