
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels. 
data_labels = ["Water Conservation","Renewable Energy","Waste Management","Air Quality","Recycling"]
data = [20,30,20,15,15]
line_labels = ["Category","ratio"]

# Create figure before plotting
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot()

# Plot the data with the type of rings chart.
ax.pie(data, labels=data_labels, startangle=90, counterclock=False,autopct='%1.1f%%')

# To change the pie chart into a ring chart, add a white circle to the center of the pie chart.
centre_circle = plt.Circle((0,0),0.7,fc='white')

# Add this circle to the axes using `ax.add_artist()`.
ax.add_artist(centre_circle)

# Create legend for the plot
ax.legend(data_labels,loc="upper right")

# Set title for the figure
ax.set_title("Sustainability - Global Overview - 2023")

# Automatically resize the image by tight_layout().
fig.tight_layout()

# The image must be saved as /cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-112353_144.png.
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-112353_144.png")

# Clear the current image state at the end of the code.
plt.clf()