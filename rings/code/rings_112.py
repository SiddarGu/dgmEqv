
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels.
data_labels = ["Home Prices", "Mortgage Rates", "Home Sales", "Home Inventory", "Economic Growth"]
data = np.array([26, 25, 24, 15, 10])
line_labels = ["Category", "ratio"]

# Plot the data with the type of rings chart. Create figure before plotting, i.e., add_subplot() follows plt.figure().
fig = plt.figure(figsize=(14,14))
ax = fig.add_subplot(111)

# The plottig of different data lines should use different colors and do not use the white color.
colors = ['#FF5733', '#FFA500', '#FFD700', '#1E90FF', '#8A2BE2']
ax.pie(data, labels=data_labels, autopct='%1.1f%%', startangle=90, colors=colors)

# Create only one pie chart using the `ax.pie()` method and setting the `startangle` and `counterclock` parameters for better layout.
ax.pie(data, startangle=90, counterclock=False)

# To change the pie chart into a ring chart in your code, you need to correctly add a white circle to the center of the pie chart. After creating the circle with `plt.Circle`, you must add this circle to the axes using `ax.add_artist()`.
inner_circle = plt.Circle((0, 0), 0.5, color='white')
ax.add_artist(inner_circle)

# For the plot of legend, do not plot the legend of gridlines or the legend of ax.fill output, only the data_labels are needed to provide the legend, i.e., ax.legend(data_labels). The positioning of the legend should not interfere with the chart and title.
ax.legend(data_labels, loc='upper left', bbox_to_anchor=(-0.1, 1))

# Drawing techniques such as background grids can be used.
ax.grid(True)

# The title of the figure should be  Real Estate and Housing Market Trends - 2021.
plt.title('Real Estate and Housing Market Trends - 2021', fontsize=15)

# Automatically resize the image by tight_layout().
plt.tight_layout()

# The image must be saved as /cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_63.png.
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_63.png')

# Clear the current image state at the end of the code.
plt.clf()