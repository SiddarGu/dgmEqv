
import matplotlib.pyplot as plt
import numpy as np

#Transform the given data into three variables: data_labels, data, line_labels.
data_labels = ['Renewable Energy', 'Fossil Fuels', 'Nuclear Energy', 'Hydroelectricity', 'Natural Gas', 'Solar Energy', 'Wind Energy']
data = [80, 60, 40, 20, 15, 10, 5]
line_labels = ['Type of Energy', 'Number of Utilities']

#Plot the data with the type of rose chart. 
fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot(111, polar=True) # Create figure before plotting, i.e., add_subplot() follows plt.figure(). Modify the axes to use polar coordinates with `polar=True` or 'projection='polar'.
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories
for i, data_label in enumerate(data_labels):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_label, color=np.random.rand(3)) #Different sectors represent different categories with the same angle, whose radius is proportional to the corresponding value, and the angles of these sectors must add up to 360 degrees, i.e., use "sector_angle = (2 * np.pi) / num_categories" to calculate the sector angle and draw sectors corresponding to different categories by making the width parameter in "ax.bar" sector_angle.

ax.set_xticks(np.arange(0, 2*np.pi, sector_angle)) #Ensure that the number of ticks set with `ax.set_xticks()` matches exactly the number of categories or labels you have in `data_labels`.
ax.set_xticklabels(data_labels, ha='center') #Make sure each category label is correctly positioned at the center of its corresponding sector. 
ax.set_title("Number of Utilities Using Different Types of Energy in 2021") #Set the title of the figure.
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 0.9)) #Reposition the legend so that it does not cover any part of the chart.

plt.tight_layout() # Automatically resize the image by tight_layout().
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231225-125808_8.png') #Save the image.
plt.clf() #Clear the current image state.