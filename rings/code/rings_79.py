
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels.
data_labels = ['Renewable Energy Sources', 'Fossil Fuels', 'Water Supply', 'Electricity Generation']
data = [45, 20, 15, 20]
line_labels = ['Item', 'ratio']

# Plot the data with the type of rings chart.
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111)
ax.pie(data, labels = data_labels, startangle=180, counterclock=False,colors=('#989898','#FFD700','#00FFFF','#FF0000'))

# Change the pie chart into a ring chart
c = plt.Circle(xy=(0,0), radius=0.7, fc='white')
ax.add_artist(c)

# Provide the legend
ax.legend(data_labels, loc="center")

# Add a title
ax.set_title('Energy and Utilities Overview - 2023', fontsize=14)

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_148.png')

# Clear the current image state
plt.clf()