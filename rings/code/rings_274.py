
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# Transform the given data into three variables
data_labels = ["Employee Retention", "Recruitment", "Training", "Performance Management", "Safety"]
data = np.array([31, 12, 25, 17, 15])
line_labels = ["Category", "Ratio"]

# Create figure and plot data
fig = plt.figure(figsize=(10, 8)) 
ax = fig.add_subplot()
ax.pie(data, startangle=90, counterclock=False, colors = ['#FF9F00', '#3399FF', '#FF0099', '#FFCC00', '#990099'])

# Create white circle
centre_circle = plt.Circle((0,0), 0.4, color='white')

# Add white circle to the pie chart
ax.add_artist(centre_circle)

# Add legend
ax.legend(data_labels, loc="best")

# Set title
ax.set_title("Human Resources and Employee Management - 2021")

# Resize image
plt.tight_layout()

# Save image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-112353_134.png')

# Clear current image state
plt.clf()