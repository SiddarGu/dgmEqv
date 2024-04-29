
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle

# Transform the given data into three variables: data_labels, data, line_labels.
data_labels = ['Education', 'Culture', 'Psychology', 'Economics', 'Politics']
data = np.array([32, 17, 25, 15, 11])
line_labels = ['Topic', 'ratio']

# Create figure before plotting
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)

# Plot the data with the type of rings chart
ax.pie(data, startangle = 90, counterclock = False, labels=data_labels, textprops={'fontsize': 15})

# To change the pie chart into a ring chart
center_circle = Circle((0, 0), 0.7, color='white')
ax.add_artist(center_circle)

# For the plot of legend, do not plot the legend of gridlines or the legend of ax.fill output
ax.legend(data_labels, loc='upper left', fontsize=14, bbox_to_anchor=(1.2, 1), ncol=1)

# Drawing techniques such as background grids can be used
ax.grid(axis='x',color='gray', linestyle='--', linewidth=0.5)

# The title of the figure
plt.title('Social Sciences and Humanities Overview - 2023', fontsize=20)

# Automatically resize the image
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-112353_107.png')

# Clear the current image state
plt.clf()