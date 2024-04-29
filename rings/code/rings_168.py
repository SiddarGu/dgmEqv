
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels. 
data_labels = ["Advertising", "Digital Presence", "Online Engagement", "Website Traffic"]
data = [17, 25, 23, 35]

# Plot the data with the type of rings chart. Create figure before plotting, i.e., add_subplot() follows plt.figure().
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)
ax.pie(data, startangle=90, counterclock=False, labels=data_labels, rotatelabels=True, textprops={'fontsize': 10}, wedgeprops={'linewidth':3})

# To change the pie chart into a ring chart in your code, you need to correctly add a white circle to the center of the pie chart. 
circle = plt.Circle((0,0), 0.5, color='white')
ax.add_artist(circle)

# For the plot of legend, do not plot the legend of gridlines or the legend of ax.fill output, only the data_labels are needed to provide the legend, i.e., ax.legend(data_labels).
ax.legend(data_labels, loc="upper right", bbox_to_anchor=(1, 0.8))

# Drawing techniques such as background grids can be used.
ax.grid(True)

# The title of the figure should be  Social Media and Web Performance - 2023.
ax.set_title("Social Media and Web Performance - 2023")

plt.tight_layout()

# The image must be saved as /cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_141.png.
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_141.png")

# Clear the current image state at the end of the code.
plt.clf()