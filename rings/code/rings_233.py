
import matplotlib.pyplot as plt 
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels.
data_labels = ["Fossil Fuel", "Renewable Energy", "Nuclear Energy", "Electric Vehicle", "Energy Efficiency"]
data = np.array([34,6,20,25,15])
line_labels = ["Type", "ratio"]

# Plot the data with the type of rings chart.
plt.figure(figsize=(9,6))
ax = plt.subplot()
ax.pie(data, labels=data_labels, startangle=90, counterclock=False)

# To change the pie chart into a ring chart in your code, you need to correctly add a white circle to the center of the pie chart.
c = plt.Circle((0,0),0.7,color='white')
ax.add_artist(c)

# For the plot of legend, do not plot the legend of gridlines or the legend of ax.fill output, only the data_labels are needed to provide the legend, i.e., ax.legend(data_labels).
ax.legend(data_labels, loc="best", bbox_to_anchor=(1,0,0.5,1))

# Drawing techniques such as background grids can be used.
ax.grid()

# The title of the figure should be  Energy Utilization in 2023.
ax.set_title('Energy Utilization in 2023')

# If the string in the picture is too long, find a way for all characters to show and not be overwritten and stacked on top of each other
plt.tight_layout()

# The image must be saved as /cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_99.png.
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_99.png")

# Clear the current image state at the end of the code.
plt.clf()