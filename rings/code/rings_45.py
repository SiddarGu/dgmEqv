
import matplotlib.pyplot as plt 
import numpy as np 

# Transform the given data into three variables: data_labels, data, line_labels 
data_labels = ['Renewable Energy', 'Fossil Fuels', 'Nuclear Power', 'Hydroelectric Power', 'Natural Gas'] 
data = [30, 20, 10, 15, 25] 
line_labels = ['Category', 'ratio'] 

# Plot the data with the type of rings chart 
fig = plt.figure(figsize=(10, 6)) 
ax = fig.add_subplot(111) 
ax.pie(data, labels=data_labels, startangle=90, counterclock=False, autopct='%.1f%%') 

# To change the pie chart into a ring chart in your code, you need to correctly add a white circle to the center of the pie chart 
centre_circle = plt.Circle((0, 0), 0.4, color='white') 
ax.add_artist(centre_circle) 

# Create only one pie chart using the `ax.pie()` method and setting the `startangle` and `counterclock` parameters for better layout 
ax.legend(data_labels,loc='upper center', bbox_to_anchor=(0.5, -0.1)) 

# Adjust the radius of the inner circle to create different ring widths 
inner_circle = plt.Circle((0, 0), 0.2, color='white') 
ax.add_artist(inner_circle) 

# For the plot of legend, do not plot the legend of gridlines or the legend of ax.fill output, only the data_labels are needed to provide the legend, i.e., ax.legend(data_labels) 
ax.set_title("Energy and Utilities - 2023 Overview") 

# Automatically resize the image by tight_layout() 
plt.tight_layout() 

# The image must be saved as /cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_106.png 
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_106.png') 

# Clear the current image state at the end of the code 
plt.clf()