
import matplotlib.pyplot as plt
import numpy as np

#Transform the given data into three variables: data_labels, data, line_labels. Data_labels represents the labels of each column except the first column. Line_labels represents the labels of each row except the first row. Data represent the numerical array in the data.
data_labels = ['Dairy', 'Bakery', 'Grains', 'Fruits', 'Vegetables', 'Beverages', 'Meat and Poultry', 'Seafood', 'Condiments']
data = np.array([90, 85, 80, 75, 70, 60, 50, 40, 30])
line_labels = ['Product Type', 'Number of Products']

#Plot the data with the type of rose chart. Create figure before plotting, i.e., add_subplot() follows plt.figure(). Modify the axes to use polar coordinates with `polar=True` or 'projection='polar'.
fig = plt.figure(figsize=(8,8))
ax = plt.subplot(111, projection='polar')

#You can use "import matplotlib.pyplot as plt" and "import numpy as np".
#There should be multiple sectors in the graph, each representing a different category, assign a different color to each sector, and add a legend next to the chart that clearly labels the category each sector represents, ensuring that the legend does not obscure any part of the chart.
#All sectors should cover the entire circumference evenly, and each sector should have the same angle.
num_categories = len(data)
sector_angle = (2 * np.pi) / num_categories
colors = ['b', 'y', 'c', 'm', 'r', 'g', 'k', '#800080', '#FFC0CB']

for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, color=colors[i], label=data_labels[i])

#Different sectors represent different categories with the same angle, whose radius is proportional to the corresponding value, and the angles of these sectors must add up to 360 degrees, i.e., use "sector_angle = (2 * np.pi) / num_categories" to calculate the sector angle and draw sectors corresponding to different categories by making the width parameter in "ax.bar" sector_angle.

#You should use a loop to assign a label to each sector when you create them with `ax.bar`. Then, when you call `ax.legend()`, it will display labels for all categories. Make sure the legend is positioned in such a way that it doesn't overlap with the chart.
#Ensure that the number of ticks set with `ax.set_xticks()` matches exactly the number of categories or labels you have in `data_labels`.
ax.set_xticks(np.arange(0, 2 * np.pi, sector_angle))
ax.set_xticklabels(data_labels, fontsize=12, va='center')

#Please modify the code to reposition the legend so that it does not cover any part of the chart. You can achieve this by adjusting the `bbox_to_anchor` parameter in the `ax.legend()` method. Try different values for `bbox_to_anchor` to find a position for the legend that is outside of the main chart area, such as at the top, bottom, or side of the chart. Ensure that the legend is clearly visible and does not overlap with the chart itself.
ax.legend(loc='upper left', bbox_to_anchor=(1.2, 1))

#Make sure that each category label is correctly positioned at the center of its corresponding sector. This can be achieved by adjusting the angle parameters in the `ax.set_xticks` method. Ensure that each angle parameter corresponds to the center position of each sector, and then use `ax.set_xticklabels` to set these category labels.
ax.set_theta_direction(-1)
ax.set_theta_zero_location('N')

#Drawing techniques such as background grids can be used.
ax.grid(True)

#The image must be saved as /cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_130.png.
plt.title('Number of Food and Beverage Products on the Market in 2021')
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_130.png')

#Clear the current image state at the end of the code.
plt.tight_layout()
plt.clf()