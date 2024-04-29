
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels.
data_labels = ['Academic Performance', 'Teacher Quality', 'Student Engagement', 'Technology Adoption', 'Facility Quality']
data = [25, 35, 15, 10, 15]
line_labels = ['Area', 'Ratio']

# Plot the data with the type of rings chart
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)

# Create only one pie chart using the ax.pie() method and setting the startangle and counterclock parameters for better layout.
cmap = plt.get_cmap("tab20c")
outer_colors = cmap(np.arange(5)*4)
inner_colors = cmap(np.array([1, 2, 5, 6, 9]))
ax.pie(data, radius=1.2, colors=outer_colors, startangle=90, counterclock=False,
       wedgeprops=dict(width=0.5, edgecolor='w'))

# To change the pie chart into a ring chart in your code, you need to correctly add a white circle to the center of the pie chart.
center_circle = plt.Circle((0,0),0.75,color='white')
ax.add_artist(center_circle)

# Plot the legend of data labels
handles = []
for i in range(5):
    patch = mpatches.Patch(color=outer_colors[i], label=data_labels[i])
    handles.append(patch)
ax.legend(handles=handles, loc='upper left')

# Drawing techniques such as background grids can be used.
plt.grid(True)

# The title of the figure should be Education Quality Index - 2023.
plt.title('Education Quality Index - 2023')

# Automatically resize the image by tight_layout().
plt.tight_layout()

# The image must be saved as /cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231225-122818_24.png.
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231225-122818_24.png')

# Clear the current image state at the end of the code.
plt.clf()