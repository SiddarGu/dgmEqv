
import matplotlib.pyplot as plt # import the matplotlib library
import pandas as pd # import the pandas library

# Transform the given data into three variables: data_labels, data, line_labels. 
# Data_labels represents the labels of each column except the first column and Line_labels represents the labels of each row except the first row. Data represent the numerical array in the data.
data_labels = ["Raw Materials", "Production Efficiency", "Quality Control", "Logistics Management", "Inventory Management"]
data = [18, 33, 15, 17, 17]
line_labels = ["Category", "ratio"]

# create figure before plotting
plt.figure(figsize=(7,7))

# plot the data with the type of rings chart
ax = plt.subplot()
ax.pie(data, labels=data_labels, startangle=90, counterclock=False, autopct='%1.1f%%')

# add a white circle to the center of the pie chart to change the pie chart into a ring chart
inner_circle = plt.Circle((0, 0), 0.75, color='white')
ax.add_artist(inner_circle)

# plot the legend of data_labels
ax.legend(data_labels, loc='best', bbox_to_anchor=(1.0, 0.5))

# draw background grids
ax.grid()

# set the title of the figure
plt.title("Manufacturing & Production - 2023")

# resize the image
plt.tight_layout()

# save the image
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_28.png")

# clear the current image state
plt.clf()