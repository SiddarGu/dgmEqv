
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

# Transform the given data into three variables: data_labels, data, line_labels. Data_labels represents the labels of each column except the first column. Line_labels represents the labels of each row except the first row. Data represent the numerical array in the data.
data_labels = ['Home Prices','Rent Prices','Home Equity','Home Ownership Rate','Mortgage Rates']
data = [36, 21, 14, 20, 9]
line_labels = ['Category', 'Ratio']

# Plot the data with the type of rings chart. Create figure before plotting, i.e., add_subplot() follows plt.figure().
fig, ax = plt.figure(figsize=(10, 10)), plt.subplot()

# The plottig of different data lines should use different colors and do not use the white color.
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Create only one pie chart using the `ax.pie()` method and setting the `startangle` and `counterclock` parameters for better layout.
ax.pie(data, startangle=90, counterclock=False, colors=colors, wedgeprops = {'linewidth': 2, 'edgecolor':"black"})

# To change the pie chart into a ring chart in your code, you need to correctly add a white circle to the center of the pie chart. After creating the circle with `plt.Circle`, you must add this circle to the axes using `ax.add_artist()`.
centre_circle = plt.Circle((0,0),0.5,color='white', fc='white',linewidth=0)

# You can adjust the radius of the inner circle to create different ring widths.
ax.add_artist(centre_circle)

# For the plot of legend, do not plot the legend of gridlines or the legend of ax.fill output, only the data_labels are needed to provide the legend, i.e., ax.legend(data_labels). The positioning of the legend should not interfere with the chart and title.
ax.legend(data_labels, loc="best")

# Drawing techniques such as background grids can be used.
ax.grid()

# The title of the figure should be  Real Estate and Housing Market Trends - 2023.
plt.title("Real Estate and Housing Market Trends - 2023")

# The image must be saved as /cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_34.png.
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_34.png')

# Clear the current image state at the end of the code.
plt.clf()