
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ["Tourism Attraction","Hospitality Quality","Customer Satisfaction","Price Competitiveness","Brand Recognition"]
data = np.array([43,18,18,14,7])
line_labels = ["Category","Ratio"]

# Plot the data with the type of rings chart
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot()

# Use different colors and do not use the white color
ax.pie(data, explode=[0.05]*len(data), startangle=90, counterclock=False, colors=cm.rainbow(np.arange(len(data))/len(data)), autopct='%1.1f%%')

# Create a white circle to the center of the pie chart
circle = plt.Circle((0,0), 0.5, color='white')
ax.add_artist(circle)

# Plot the legend of data_labels
ax.legend(data_labels, bbox_to_anchor=(1, 0.8), loc="upper right")

# Add background grids 
ax.grid()
ax.set_title("Tourism and Hospitality Analysis - 2023")

# Automatically resize the image
plt.tight_layout()

# Save the image
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_21.png")

# Clear the current image state
plt.cla()