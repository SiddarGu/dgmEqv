
import matplotlib.pyplot as plt
import numpy as np

# transform the given data into three variables
data_labels = ['Staff Retention', 'Employee Satisfaction', 'Employee Development', 'Performance Evaluation', 'Recruitment']
data = np.array([25, 24, 23, 18, 10])
line_labels = [str(i) for i in range(1, 6)]

# Plot the data with the type of rings chart
# Create figure before plotting
fig, ax = plt.subplots()
ax.pie(data, labels=data_labels, startangle=90, counterclock=False)

# add a white circle to the center of the pie chart
centre_circle = plt.Circle((0, 0), 0.7, color='white')
ax.add_artist(centre_circle)

# Plot legend
ax.legend(data_labels, loc='upper right', fontsize=10)

# Use tight_layout() to automatically resize the image
plt.title('Human Resource Management - 2023', fontsize=12)
plt.tight_layout()

# save the figure
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_17.png')

# Clear the current image state
plt.clf()