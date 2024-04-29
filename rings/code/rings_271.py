
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Profit', 'Expenses', 'Investments', 'Revenue', 'Market Share']
data = [27, 52, 3, 16, 2]
line_labels = ['Category', 'ratio']

# Figure
fig = plt.figure(figsize=(8,8))
ax = plt.subplot()

# Plot the data with the type of rings chart
ax.pie(data, startangle=180, counterclock=False, labels=data_labels)

# Create a white circle to the center of the pie chart
circle = plt.Circle((0,0), 0.7, color='white')
ax.add_artist(circle)

# Legend
ax.legend(data_labels, loc='upper left', bbox_to_anchor=(-0.1, 1))

# Title
plt.title("Financial Performance Overview - 2021")

# Save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-112353_13.png', bbox_inches='tight')

# Clear the current image state
plt.clf()