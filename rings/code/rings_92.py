
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Research and Development', 'Innovation', 'Efficiency', 'Productivity', 'Safety']
data = [0.32, 0.30, 0.15, 0.16, 0.07]
line_labels = np.arange(len(data_labels))

# Create figure before plotting, i.e., add_subplot() follows plt.figure()
fig, ax = plt.subplots(figsize=(10,10))

# Plot the data with the type of rings chart
ax.pie(data, labels=data_labels, startangle=90, counterclock=False, colors=['#f45c42', '#1f77b4', '#fec44f', '#1ca086', '#4d9f8f'])

# To change the pie chart into a ring chart in your code, you need to correctly add a white circle to the center of the pie chart
centre_circle = plt.Circle((0,0), 0.5, color='white', fc='white', linewidth=0)
ax.add_artist(centre_circle)

# For the plot of legend, do not plot the legend of gridlines or the legend of ax.fill output, only the data_labels are needed to provide the legend
ax.legend(data_labels, loc='upper right')

# Drawing techniques such as background grids can be used
ax.grid(True)

# The title of the figure
plt.title('Science and Engineering Performance Evaluation - 2023')

# Automatically resize the image by tight_layout()
plt.tight_layout()

# The image must be saved
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_34.png')

# Clear the current image state at the end of the code
plt.clf()