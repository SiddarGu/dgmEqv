
import matplotlib.pyplot as plt
import numpy as np

# transform the given data into three variables: data_labels, data, line_labels
data_labels = ["Online Sales", "In-Store Sales", "Brand Awareness", "Advertising"]
data = np.array([47, 33, 12, 8])
line_labels = ["Category", "ratio"]

# create a figure
fig, ax = plt.subplots(figsize=(10, 5))

# plot the data with the type of rings chart
outer_radius = 1
inner_radius = 0.8
explode = [0, 0, 0, 0]
ax.pie(data, labels=data_labels, autopct='%1.1f%%', shadow=False, startangle=90,
       colors=['red', 'orange', 'green', 'blue'], explode=explode,
       radius = outer_radius, counterclock=False)
# add a circle to the center of the pie chart
center_circle = plt.Circle((0, 0), inner_radius, color='white', fc='white',
                           linewidth=0)
ax.add_artist(center_circle)

# plot the legend
ax.legend(data_labels, bbox_to_anchor=(1, 0.5), loc="center left")

# plot the title
ax.set_title("Retail and E-commerce Performance - 2023")

# adjust the radius of the inner circle to create different ring widths
center_circle.set_radius(0.45)

# draw background grids
ax.grid()

# resize the image
plt.tight_layout()

# save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_110.png')

# clear the current image state
plt.clf()