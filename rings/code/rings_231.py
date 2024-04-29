
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Art Appreciation', 'Cultural Understanding', 'Music Appreciation', 'Creative Expression', 'Performance Arts']
data = [17, 17, 25, 20, 21]
line_labels = ['Category', 'ratio']

# Plot the data with the type of rings chart
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)
ax.pie(data, labels=data_labels, startangle=90, counterclock=False, colors=['#0D9EAD', '#E63C2E', '#F2E933', '#9E00A4', '#FF7800'])
# To change the pie chart into a ring chart
centre_circle = plt.Circle((0,0),0.75,fc='white')
ax.add_artist(centre_circle)
# For the plot of legend
ax.legend(data_labels, loc='upper right', bbox_to_anchor=(1, 0.5))
# Drawing techniques such as background grids can be used
ax.grid(True, linestyle='-',color='#C2C2C2', linewidth=1)
# The title of the figure
ax.set_title('Arts and Culture Appreciation - 2023')
# Automatically resize the image by tight_layout()
plt.tight_layout()
# The image must be saved as /cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_96.png.
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_96.png')
# Clear the current image state at the end of the code
plt.clf()