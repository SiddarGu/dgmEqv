
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels.
data_labels = ["Arts Education", "Cultural Heritage", "Artistic Expression", "Community Participation", "Arts Funding"]
data = [24,19,21,21,15]
line_labels = ["Category", "ratio"]

# Plot the data with the type of rings chart. Create figure before plotting, i.e., add_subplot() follows plt.figure().
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)

# The plottig of different data lines should use different colors and do not use the white color.
colors = cm.rainbow(np.linspace(0, 1, len(data)))

# Create only one pie chart using the `ax.pie()` method and setting the `startangle` and `counterclock` parameters for better layout.
wedges, texts, autotexts = ax.pie(data, labels = data_labels, startangle = 90, counterclock = False, autopct = "%1.0f%%", colors = colors)

# To change the pie chart into a ring chart in your code, you need to correctly add a white circle to the center of the pie chart. After creating the circle with `plt.Circle`, you must add this circle to the axes using `ax.add_artist()`.
inner_circle = plt.Circle((0,0), 0.3, color = 'white')
ax.add_artist(inner_circle)

# For the plot of legend, do not plot the legend of gridlines or the legend of ax.fill output, only the data_labels are needed to provide the legend, i.e., ax.legend(data_labels). The positioning of the legend should not interfere with the chart and title.
ax.legend(data_labels, loc='upper center', bbox_to_anchor=(0.5, -0.2))

# Drawing techniques such as background grids can be used.
ax.grid(True, axis='y')

# The image must be saved as /cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-112353_114.png.
plt.title("Arts and Culture Development - 2023")
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-112353_114.png")

# Clear the current image state at the end of the code.
plt.clf()