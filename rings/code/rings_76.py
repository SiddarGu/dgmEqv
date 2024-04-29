
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 

#transform the given data into three variables
data_labels=['Renewable Energy','Oil and Gas','Electricity','Nuclear Power','Other Resources']
data=[17,37,25,14,7]
line_labels=['Category','ratio']

#plot the data with the type of rings chart
fig, ax = plt.subplots(figsize=(12,6))
pie_wedge_collection = ax.pie(data, labels=data_labels, startangle=90, counterclock=False, wedgeprops=dict(width=0.3))

#add the white circle to the center of the pie chart
center_circle = plt.Circle((0,0),0.7,color='white')
ax.add_artist(center_circle)

#plot the legend
ax.legend(data_labels)

#draw the background grids
ax.grid()

#set the title of the figure
ax.set_title('Energy and Utilities Utilisation - 2023')

#resize the image
plt.tight_layout()

#save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_145.png')

#clear the current image state
plt.cla()