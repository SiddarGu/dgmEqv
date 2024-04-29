
import numpy as np
import matplotlib.pyplot as plt

# Transform data
data_labels = ['Delivery Efficiency', 'Vehicle Maintenance', 'Supply Chain Management', 'Customer Service', 'Cost Control']
data = [55, 17, 15, 6, 7]
line_labels = ['Category', 'ratio']

# Create figure
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)

# Plot data
colors = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF']
ax.pie(data, labels=data_labels, colors=colors, startangle=90, counterclock=False)

# Add a white circle to the center of the pie chart to turn it into a ring chart
centre_circle = plt.Circle((0,0), 0.5, fc='white')
ax.add_artist(centre_circle)

# Plot legend
ax.legend(data_labels, loc="best")

# Set title
plt.title('Transportation and Logistics Efficiency - 2023')

# Adjust the radius of the inner circle to create different ring widths
inner_circle = plt.Circle((0,0), 0.3, fc='white')
ax.add_artist(inner_circle)

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_90.png')

# Clear the current image state
plt.cla()